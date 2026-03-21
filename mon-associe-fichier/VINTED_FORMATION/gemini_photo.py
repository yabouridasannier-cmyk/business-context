#!/usr/bin/env python3
"""
GEMINI PHOTO GENERATOR — Vinted Dropshipping (V2 — Persona-Aware)
Génère des photos produit réalistes via Gemini API, adaptées à chaque persona.

Usage:
    # Vêtement avec persona
    python3 gemini_photo.py --produit "robe maxi fleurie" --couleur "vert prairie" --persona cottagecore_gt --output-dir images/

    # Chaussures avec persona
    python3 gemini_photo.py --produit "bottes cowboy chunky heel" --couleur "noir cuir" --persona western --type chaussures --output-dir images/

    # Déco (tapis, tapisserie)
    python3 gemini_photo.py --produit "tapis chevalier médiéval" --couleur "noir rouge héraldique" --persona larp_deco --type deco --output-dir images/

    # Sans persona (mode legacy)
    python3 gemini_photo.py --produit "cardigan pastel rose" --couleur "rose pastel" --output-dir images/

Prérequis:
    pip install google-genai Pillow piexif --break-system-packages
"""

import argparse
import base64
import json
import os
import re
import sys
import time
from pathlib import Path

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Module google-genai manquant.")
    print("   Installe avec : pip install google-genai --break-system-packages")
    sys.exit(1)

try:
    from PIL import Image
    import piexif
except ImportError:
    print("Modules Pillow ou piexif manquants.")
    print("   Installe avec : pip install Pillow piexif --break-system-packages")
    sys.exit(1)

# === CONFIG ===
API_KEY = "AIzaSyCGVwWF9ZZ5lzcPf_q2fBRiQWTJWAbi_gA"
MODEL = "gemini-2.5-flash-image"

# === DESCRIPTION MODÈLE RÉFÉRENT (défaut legacy) ===
MODEL_DESCRIPTION = (
    "slim young woman, brown braided hair, Mediterranean complexion, "
    "face hidden behind phone taking mirror selfie"
)
DEFAULT_SETTING = "cozy indoor room, natural window light, warm tones"

# === CONFIGS PAR PERSONA ===
# RÈGLE CLÉ : le décor = intérieur de maison NORMAL avec juste 1-2 petits détails persona.
# Jamais de décor immersif (pas de ranch, pas de jardin cottage, pas de château).
# Ça doit ressembler à une vraie vendeuse Vinted qui prend des photos chez elle.
PERSONA_CONFIGS = {
    "western": {
        "model_desc": (
            "young woman, 26, tan skin, wavy brown hair, athletic build, "
            "face COMPLETELY HIDDEN behind smartphone taking mirror selfie, "
            "you cannot see her face at all — phone covers it entirely"
        ),
        "setting": (
            "normal bedroom or hallway at home, full-length mirror, "
            "small western touch in background — maybe a horseshoe on the wall or a cowboy hat hanging on a hook, "
            "messy real bedroom, unmade bed or clothes on a chair visible, "
            "warm indoor lighting from a window, casual home environment"
        ),
    },
    "cottagecore_gt": {
        "model_desc": (
            "plus-size woman, size 2XL-3XL, 26, curly light brown hair, "
            "curvy body with wide hips and full figure, NOT slim, clearly plus-size, "
            "thick arms, soft belly visible through fabric drape, "
            "face COMPLETELY HIDDEN behind smartphone taking mirror selfie, "
            "you cannot see her face at all — phone covers it entirely"
        ),
        "setting": (
            "normal apartment bedroom, full-length mirror on the wall or leaning against wall, "
            "small plant or dried flowers on a shelf in background, "
            "a few books stacked, warm natural light from window, "
            "casual lived-in home, maybe a rug on the floor, nothing fancy"
        ),
    },
    "romantique": {
        "model_desc": (
            "slim woman, 25, dark hair in low bun, pale complexion, "
            "face COMPLETELY HIDDEN behind smartphone taking mirror selfie, "
            "you cannot see her face at all — phone covers it entirely"
        ),
        "setting": (
            "normal apartment living room or bedroom, full-length mirror, "
            "bright natural daylight from large windows with sheer curtains, "
            "light wood floor visible, maybe a desk or chair in background, "
            "bright airy home interior, not moody, not dim — lots of natural light"
        ),
    },
    "larp_costume": {
        "model_desc": (
            "young person, 24, medium build, brown hair, "
            "face COMPLETELY HIDDEN behind smartphone taking mirror selfie, "
            "you cannot see her face at all — phone covers it entirely"
        ),
        "setting": (
            "normal apartment room, full-length mirror, "
            "maybe a sword replica or a small shield on the wall in background, "
            "normal home with warm lighting, casual environment"
        ),
    },
    "larp_deco": {
        "model_desc": None,
        "setting": (
            "normal living room, warm lamp light, a bookshelf or TV stand visible, "
            "couch in background, lived-in apartment feel, "
            "nothing fancy — just a regular home where someone put this item"
        ),
    },
    "stockholm": {
        "model_desc": (
            "slim young woman, 25, blonde or light brown hair, Scandinavian look, "
            "face COMPLETELY HIDDEN behind smartphone taking mirror selfie, "
            "you cannot see her face at all — phone covers it entirely"
        ),
        "setting": (
            "minimal Scandinavian apartment, clean white or light grey walls, "
            "full-length mirror, simple light wood furniture visible in background, "
            "a small plant on a shelf, natural diffuse light from a large window, "
            "very tidy and uncluttered — no decor overload, Scandi home feel"
        ),
    },
    "urban_streetwear": {
        "model_desc": (
            "young person, 22, mixed ethnicity, athletic slim build, "
            "face COMPLETELY HIDDEN behind smartphone taking mirror selfie, "
            "you cannot see the face at all — phone covers it entirely"
        ),
        "setting": (
            "urban apartment, exposed concrete wall or plain white wall, "
            "full-length mirror, a pair of sneakers on the floor, "
            "maybe a cap or a small skateboard leaning against the wall, "
            "moody indoor lighting, cool and minimal urban home"
        ),
    },
}

# === 3 POSES STANDARD VÊTEMENTS ===
# Pose 1: face miroir (téléphone cache le visage)
# Pose 2: dos (pas de visage)
# Pose 3: vêtement posé au sol à plat
POSE_PROMPTS = {
    "face": (
        "Generate a realistic iPhone photo of {model_desc} wearing the {couleur} {produit}. "
        "Mirror selfie in a {setting}. The phone COMPLETELY covers her face — NO face visible at all. "
        "Full body visible in the mirror, head to feet. "
        "CRITICAL: The garment color must be EXACTLY '{couleur}' — vivid, accurate, true-to-life color. NOT faded, NOT desaturated, NOT vintage-toned. The exact color as it would appear on the real item. "
        "Casual amateur photo — slightly tilted angle, not perfectly centered. "
        "Bright natural daylight from windows. Real phone photo quality with slight grain. "
        "NOT professional, NOT studio, NOT AI-looking. Like a real girl took this for Vinted."
    ),
    "dos": (
        "Generate a realistic iPhone photo of {model_desc} wearing the {couleur} {produit}. "
        "Back view, she is turned away from camera, NO face visible. Hair visible, back of garment shown fully. "
        "Standing in a {setting}. "
        "CRITICAL: The garment color must be EXACTLY '{couleur}' — vivid, accurate, true-to-life color. NOT faded, NOT desaturated. "
        "Casual amateur photo — not perfectly framed, slightly off-center. "
        "Bright natural daylight. Real phone photo with grain. "
        "NOT professional, NOT a studio shot. Like a real Vinted seller photo."
    ),
    "sol": (
        "Generate a realistic iPhone photo of the {couleur} {produit} laid flat on a wooden floor or on a bed. "
        "The garment is neatly spread out to show its full shape, pattern and color. "
        "CRITICAL: The garment color must be EXACTLY '{couleur}' — vivid, accurate, true-to-life color. NOT faded, NOT desaturated. "
        "Flatlay style but casual — not perfectly arranged, slightly wrinkled naturally. "
        "Setting: {setting} — floor or bed visible. "
        "Shot from directly above, bright natural daylight. Real phone photo quality. "
        "NOT a catalog photo. Like a Vinted seller quickly laid it out and snapped a pic."
    ),
}

# === 3 POSES CHAUSSURES ===
# Pose 1: paire posée au sol
# Pose 2: portées (jambes seulement, pas de visage)
# Pose 3: détail/zoom
SHOE_PROMPTS = {
    "sol_paire": (
        "Generate a realistic iPhone photo of a pair of {couleur} {produit} "
        "placed on the floor in a {setting}. Shoes at a casual angle, not perfectly aligned. "
        "Natural indoor light from a window. Visible texture and stitching. "
        "Casual amateur Vinted seller photo — not a product shoot. "
        "Real phone photo quality with grain. Floor is normal home floor (wood or tile)."
    ),
    "portee": (
        "Generate a realistic iPhone photo showing legs from knee down only, NO face, "
        "wearing the {couleur} {produit}. Standing on floor in a {setting}. "
        "Paired with dark jeans. Natural indoor lighting. "
        "Casual selfie angle — she pointed the phone down at her feet. "
        "Real phone photo, slightly blurry, not perfect. Like a real Vinted photo."
    ),
    "detail": (
        "Generate a realistic iPhone close-up photo of one {couleur} {produit}. "
        "Close-up on the stitching, heel, and material texture. "
        "Held in hand or on a table in a {setting}. "
        "Natural light, slight shallow depth of field. "
        "Real phone macro shot — casual, not professional."
    ),
}

# === 3 POSES DÉCO ===
# Pose 1: produit dans la pièce
# Pose 2: zoom détail
# Pose 3: vue large de la pièce avec le produit
DECO_PROMPTS = {
    "ambiance": (
        "Generate a realistic iPhone photo of a {couleur} {produit} "
        "displayed in a {setting}. The item is clearly visible and is the subject. "
        "Warm indoor lamp light. "
        "Casual phone photo — someone just hung/placed it and took a pic to sell on Vinted. "
        "Not staged, not professional. Real home environment."
    ),
    "detail": (
        "Generate a realistic iPhone close-up photo of the {couleur} {produit}. "
        "Zoom on the most detailed area — texture, print quality, colors. "
        "{setting} blurred in background. "
        "Natural light from the side. Phone macro shot, casual quality."
    ),
    "contexte": (
        "Generate a realistic iPhone wide shot of a normal room with the "
        "{couleur} {produit} visible as decoration. {setting}. "
        "Room looks lived-in — remote on couch, mug on table, shoes by the door. "
        "The product is there but it is a normal home, not a showroom. "
        "Casual wide phone photo, slightly tilted."
    ),
}


def inject_exif_iphone(image_path: str) -> str:
    """Injecte des métadonnées EXIF iPhone 15 sur l'image."""
    img = Image.open(image_path)
    exif_dict = {
        "0th": {
            piexif.ImageIFD.Make: b"Apple",
            piexif.ImageIFD.Model: b"iPhone 15",
            piexif.ImageIFD.Software: b"17.4.1",
        },
        "Exif": {
            piexif.ExifIFD.LensModel: b"iPhone 15 back camera 6.86mm f/1.78",
            piexif.ExifIFD.FocalLength: (686, 100),
            piexif.ExifIFD.FNumber: (178, 100),
        },
        "GPS": {},
    }
    exif_bytes = piexif.dump(exif_dict)
    img.save(image_path, exif=exif_bytes)
    return image_path


def generate_image(client: genai.Client, prompt: str, output_path: str,
                   model_photo: str = None, product_photo: str = None) -> str:
    """Génère une image avec Gemini."""
    contents = []
    if model_photo and os.path.exists(model_photo):
        contents.append(Image.open(model_photo))
    if product_photo and os.path.exists(product_photo):
        contents.append(Image.open(product_photo))
    contents.append(prompt)

    response = client.models.generate_content(
        model=MODEL,
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
        ),
    )

    for part in response.candidates[0].content.parts:
        if part.inline_data is not None:
            raw = part.inline_data.data
            image_data = raw if isinstance(raw, bytes) else base64.b64decode(raw)
            # Determine correct extension from mime type
            mime = part.inline_data.mime_type or "image/png"
            ext = ".png" if "png" in mime else ".jpg"
            if not output_path.endswith(ext):
                output_path = os.path.splitext(output_path)[0] + ext

            os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(image_data)

            # Convert PNG to JPEG and inject EXIF (Vinted expects phone photos)
            if ext == ".png":
                jpg_path = os.path.splitext(output_path)[0] + ".jpg"
                img = Image.open(output_path).convert("RGB")
                img.save(jpg_path, "JPEG", quality=92)
                os.remove(output_path)
                output_path = jpg_path

            inject_exif_iphone(output_path)
            print(f"  [OK] {os.path.basename(output_path)}")
            return output_path

    return None


def get_prompts_for_type(product_type: str) -> dict:
    """Retourne le bon jeu de prompts selon le type de produit."""
    if product_type == "chaussures":
        return SHOE_PROMPTS
    elif product_type == "deco":
        return DECO_PROMPTS
    else:
        return POSE_PROMPTS


def generer_images(produit: str, couleur: str, output_dir: str,
                   persona: str = None, product_type: str = "vetement",
                   product_photo: str = None, model_photo: str = None) -> dict:
    """
    Génère 3 images pour un produit, adaptées au persona et au type de produit.

    Args:
        produit: nom du produit
        couleur: couleur principale
        output_dir: dossier de sortie
        persona: clé dans PERSONA_CONFIGS (western, cottagecore_gt, romantique, larp_costume, larp_deco)
        product_type: "vetement", "chaussures", ou "deco"
        product_photo: photo AliExpress du produit (optionnel)
        model_photo: photo modèle référent (optionnel)
    """
    client = genai.Client(api_key=API_KEY)
    slug = re.sub(r"[^a-z0-9]+", "_", produit.lower()).strip("_")
    os.makedirs(output_dir, exist_ok=True)

    # Résoudre persona
    if persona and persona in PERSONA_CONFIGS:
        config = PERSONA_CONFIGS[persona]
        model_desc = config["model_desc"] or "no person in the image"
        setting = config["setting"]
    else:
        model_desc = MODEL_DESCRIPTION
        setting = DEFAULT_SETTING

    # Modèle référent par défaut (seulement pour vêtements)
    if model_photo is None and product_type == "vetement":
        default_model = os.path.join(os.path.dirname(__file__), "images/model/MODEL_REFERENCE.jpg")
        model_photo = default_model if os.path.exists(default_model) else None

    # Sélectionner les bons prompts
    prompts = get_prompts_for_type(product_type)

    resultats = {}
    for pose_name, prompt_template in prompts.items():
        prompt = prompt_template.format(
            produit=produit,
            couleur=couleur,
            model_desc=model_desc,
            setting=setting,
        )
        output_path = os.path.join(output_dir, f"{slug}_{pose_name}.jpg")
        print(f"  [GEN] Pose '{pose_name}'...")

        try:
            # Envoyer la photo produit sur TOUTES les poses pour fidélité maximale
            use_product_photo = product_photo
            use_model_photo = model_photo if product_type == "vetement" else None

            result = generate_image(client, prompt, output_path,
                                    model_photo=use_model_photo,
                                    product_photo=use_product_photo)
            if result:
                resultats[pose_name] = result
        except Exception as e:
            err_str = str(e)
            if "RESOURCE_EXHAUSTED" in err_str or "limit: 0" in err_str or "quota" in err_str.lower():
                print("\n[ERREUR] QUOTA GEMINI EPUISE")
                print("   -> Vérifier billing sur aistudio.google.com")
                print("   -> Ou créer nouvelle clé API depuis projet avec billing actif")
                sys.exit(2)
            print(f"  [ERREUR] Pose {pose_name} : {e}")

        time.sleep(2)

    return resultats


# Rétro-compatibilité
def generer_3_poses(produit, couleur, output_dir, product_photo=None, model_photo=None):
    """Legacy wrapper — appelle generer_images sans persona."""
    return generer_images(produit, couleur, output_dir,
                          product_photo=product_photo, model_photo=model_photo)


def download_aliexpress_image(url: str, save_path: str) -> str:
    """Télécharge la première image d'un lien AliExpress."""
    import urllib.request
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as r:
        os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(r.read())
    return save_path


def main():
    parser = argparse.ArgumentParser(description="Gemini Photo Generator V2 — Persona-Aware")
    parser.add_argument("--produit", required=False, default="", help="Nom du produit")
    parser.add_argument("--couleur", default="pastel", help="Couleur principale")
    parser.add_argument("--output-dir", default="./images", help="Dossier de sortie")
    parser.add_argument("--persona", choices=list(PERSONA_CONFIGS.keys()),
                        help="Persona (western, cottagecore_gt, romantique, larp_costume, larp_deco)")
    parser.add_argument("--type", dest="product_type", default="vetement",
                        choices=["vetement", "chaussures", "deco"],
                        help="Type de produit (vetement, chaussures, deco)")
    parser.add_argument("--product-photo", help="Chemin vers photo AliExpress du produit")
    parser.add_argument("--aliexpress-url", help="URL image AliExpress (téléchargement auto)")
    parser.add_argument("--model-photo", help="Photo modèle référent")
    parser.add_argument("--batch", help="Fichier JSON batch")

    args = parser.parse_args()

    product_photo = args.product_photo

    # Télécharger depuis AliExpress si URL fournie
    if args.aliexpress_url and not product_photo:
        slug = re.sub(r"[^a-z0-9]+", "_", args.produit.lower())
        product_photo = f"/tmp/{slug}_aliexpress.jpg"
        print(f"[DL] Téléchargement photo AliExpress...")
        try:
            download_aliexpress_image(args.aliexpress_url, product_photo)
            print(f"  [OK] Photo téléchargée")
        except Exception as e:
            print(f"  [WARN] Téléchargement échoué ({e}) — génération sans référence produit")
            product_photo = None

    if args.batch:
        with open(args.batch) as f:
            produits = json.load(f)
        for p in produits:
            print(f"\n{'='*50}")
            print(f"  {p['produit']}")
            print(f"{'='*50}")
            # Résoudre la photo produit : fichier local > téléchargement image_url > rien
            pp = p.get("product_photo", product_photo)
            if not pp and p.get("image_url"):
                import tempfile
                slug = re.sub(r"[^a-z0-9]+", "_", p["produit"].lower())[:40]
                tmp = os.path.join(tempfile.gettempdir(), f"{slug}_ref.jpg")
                if os.path.exists(tmp):
                    pp = tmp
                    print(f"  [CACHE] Image référence déjà téléchargée")
                else:
                    print(f"  [DL] Téléchargement image de référence CDN...")
                    try:
                        download_aliexpress_image(p["image_url"], tmp)
                        pp = tmp
                        print(f"  [OK] Image référence prête")
                    except Exception as e:
                        print(f"  [WARN] Téléchargement échoué ({e}) — génération sans référence")
                        pp = None
            generer_images(
                p["produit"],
                p.get("couleur", "pastel"),
                p.get("output_dir", args.output_dir),
                persona=p.get("persona", args.persona),
                product_type=p.get("type", args.product_type),
                product_photo=pp,
                model_photo=args.model_photo
            )
    else:
        persona_label = f" [{args.persona}]" if args.persona else ""
        type_label = f" ({args.product_type})" if args.product_type != "vetement" else ""
        print(f"[START] {args.produit} ({args.couleur}){persona_label}{type_label}")
        resultats = generer_images(
            args.produit, args.couleur, args.output_dir,
            persona=args.persona,
            product_type=args.product_type,
            product_photo=product_photo,
            model_photo=args.model_photo
        )
        total = len(get_prompts_for_type(args.product_type))
        print(f"\n[DONE] {len(resultats)}/{total} images générées :")
        for pose, path in resultats.items():
            print(f"   {pose}: {path}")


if __name__ == "__main__":
    main()
