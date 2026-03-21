#!/usr/bin/env python3
"""
LEONARDO.AI PHOTO GENERATOR — Vinted Dropshipping
Génère des photos produit avec le modèle référent via Leonardo.ai API

Clé API : à renseigner dans API_KEY ci-dessous

Usage:
    python3 leonardo_photo.py --produit "cardigan rose pastel" --couleur "rose pastel"
    python3 leonardo_photo.py --produit "chemise dentelle" --couleur "blanc crème" --product-photo aliexpress_photo.jpg
    python3 leonardo_photo.py --batch batch_produits.json

Génère pour chaque produit :
    [produit]_face.jpg      — modèle de face (miroir selfie)
    [produit]_dos.jpg       — modèle de dos
    [produit]_profil.jpg    — modèle de profil
    [produit]_flatlay.jpg   — produit à plat (sans modèle)

Prérequis:
    pip install requests Pillow piexif --break-system-packages
"""

import argparse
import json
import os
import re
import sys
import time
import requests
from pathlib import Path

try:
    from PIL import Image
    import piexif
except ImportError:
    print("❌ Modules Pillow ou piexif manquants.")
    print("   Installe avec : pip install Pillow piexif --break-system-packages")
    sys.exit(1)

# === CONFIG — METTRE À JOUR AVEC LA CLÉ LEONARDO ===
API_KEY = "LEONARDO_API_KEY_ICI"

# Chemin vers la photo du modèle référent
MODEL_REFERENCE_PATH = os.path.join(os.path.dirname(__file__), "images/model/MODEL_REFERENCE.jpg")

# Description du modèle (constante pour tout le compte)
MODEL_DESCRIPTION = (
    "Young slim woman, brown braided hair, Mediterranean complexion, "
    "face hidden by phone or hand, natural indoor lighting"
)

# === PROMPTS PAR POSE ===
POSE_PROMPTS = {
    "face": (
        "{model_desc}, wearing {couleur} {produit}, "
        "taking a mirror selfie, phone covering face, full body visible, "
        "natural light, authentic Vinted seller photo style, "
        "indoor background, realistic photo, not studio"
    ),
    "dos": (
        "{model_desc}, wearing {couleur} {produit}, "
        "back view, hair braid visible, no face shown, "
        "full body back shot, natural indoor light, authentic style"
    ),
    "profil": (
        "{model_desc}, wearing {couleur} {produit}, "
        "side profile view, 3/4 angle, face turned away, "
        "full body visible, natural window light, realistic photo"
    ),
    "flatlay": (
        "Flat lay product photo of a {couleur} {produit} on a white/cream linen surface. "
        "Viewed from directly above, neatly arranged. "
        "Natural soft light, no shadows. One small dried flower beside it. "
        "iPhone 15 photo style, realistic grain. Ratio 4:3. No watermark."
    ),
}


def inject_exif_iphone(image_path: str) -> str:
    """Injecte des métadonnées EXIF iPhone 15."""
    try:
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
    except Exception as e:
        print(f"  ⚠️  EXIF injection échouée : {e}")
    return image_path


def upload_image_to_leonardo(image_path: str) -> str:
    """Upload une image de référence sur Leonardo et retourne l'ID."""
    headers = {"authorization": f"Bearer {API_KEY}", "content-type": "application/json"}

    # Étape 1 : obtenir l'URL d'upload
    ext = Path(image_path).suffix.lstrip(".").lower()
    r = requests.post(
        "https://cloud.leonardo.ai/api/rest/v1/init-image",
        headers=headers,
        json={"extension": ext}
    )
    r.raise_for_status()
    data = r.json()
    upload_url = data["uploadInitImage"]["url"]
    fields = json.loads(data["uploadInitImage"]["fields"])
    image_id = data["uploadInitImage"]["id"]

    # Étape 2 : upload S3
    with open(image_path, "rb") as f:
        files = {"file": f}
        r2 = requests.post(upload_url, data=fields, files=files)
        r2.raise_for_status()

    return image_id


def generate_with_image_guidance(prompt: str, reference_image_id: str, output_path: str) -> str:
    """Génère une image avec Image Guidance (référence de pose/style)."""
    headers = {"authorization": f"Bearer {API_KEY}", "content-type": "application/json"}

    payload = {
        "prompt": prompt,
        "modelId": "b24e16ff-06e3-43eb-8d33-4416c2d75876",  # Leonardo Phoenix
        "width": 768,
        "height": 1024,
        "num_images": 1,
        "guidance_scale": 7,
        "controlnets": [
            {
                "initImageId": reference_image_id,
                "initImageType": "UPLOADED",
                "preprocessorId": 100,   # Pose ControlNet
                "strengthType": "Mid",
            }
        ],
    }

    r = requests.post(
        "https://cloud.leonardo.ai/api/rest/v1/generations",
        headers=headers,
        json=payload
    )
    r.raise_for_status()
    generation_id = r.json()["sdGenerationJob"]["generationId"]

    # Attendre le résultat (polling)
    for _ in range(30):
        time.sleep(3)
        r = requests.get(
            f"https://cloud.leonardo.ai/api/rest/v1/generations/{generation_id}",
            headers=headers
        )
        r.raise_for_status()
        gen = r.json()["generations_by_pk"]
        if gen["status"] == "COMPLETE":
            img_url = gen["generated_images"][0]["url"]
            img_data = requests.get(img_url).content
            os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(img_data)
            inject_exif_iphone(output_path)
            return output_path
        elif gen["status"] == "FAILED":
            raise RuntimeError(f"Génération Leonardo échouée : {gen}")

    raise TimeoutError("Leonardo n'a pas répondu dans les 90 secondes")


def generate_text_only(prompt: str, output_path: str) -> str:
    """Génère une image sans référence (pour flatlay)."""
    headers = {"authorization": f"Bearer {API_KEY}", "content-type": "application/json"}

    payload = {
        "prompt": prompt,
        "modelId": "b24e16ff-06e3-43eb-8d33-4416c2d75876",  # Leonardo Phoenix
        "width": 1024,
        "height": 768,
        "num_images": 1,
        "guidance_scale": 7,
    }

    r = requests.post(
        "https://cloud.leonardo.ai/api/rest/v1/generations",
        headers=headers,
        json=payload
    )
    r.raise_for_status()
    generation_id = r.json()["sdGenerationJob"]["generationId"]

    for _ in range(30):
        time.sleep(3)
        r = requests.get(
            f"https://cloud.leonardo.ai/api/rest/v1/generations/{generation_id}",
            headers=headers
        )
        r.raise_for_status()
        gen = r.json()["generations_by_pk"]
        if gen["status"] == "COMPLETE":
            img_url = gen["generated_images"][0]["url"]
            img_data = requests.get(img_url).content
            os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
            with open(output_path, "wb") as f:
                f.write(img_data)
            inject_exif_iphone(output_path)
            return output_path
        elif gen["status"] == "FAILED":
            raise RuntimeError(f"Génération Leonardo échouée")

    raise TimeoutError("Timeout")


def generer_photos_produit(produit: str, couleur: str, output_dir: str, poses: list = None) -> dict:
    """
    Génère toutes les photos pour un produit avec le modèle référent.
    poses : liste de poses à générer (default: ["face", "dos", "flatlay"])
    """
    if API_KEY == "LEONARDO_API_KEY_ICI":
        print("❌ Clé API Leonardo non configurée. Mets à jour API_KEY dans le script.")
        sys.exit(1)

    if poses is None:
        poses = ["face", "dos", "flatlay"]

    slug = re.sub(r"[^a-z0-9]+", "_", produit.lower()).strip("_")
    os.makedirs(output_dir, exist_ok=True)
    resultats = {}

    # Upload le modèle référent (une seule fois par session)
    model_image_id = None
    if os.path.exists(MODEL_REFERENCE_PATH):
        print(f"  📸 Upload modèle référent...")
        model_image_id = upload_image_to_leonardo(MODEL_REFERENCE_PATH)
        print(f"  ✅ Modèle uploadé (ID: {model_image_id})")
    else:
        print(f"  ⚠️  MODEL_REFERENCE.jpg non trouvé → poses sans référence")
        print(f"     Chemin attendu : {MODEL_REFERENCE_PATH}")

    for pose in poses:
        output_path = os.path.join(output_dir, f"{slug}_{pose}.jpg")
        prompt_template = POSE_PROMPTS.get(pose, POSE_PROMPTS["face"])
        prompt = prompt_template.format(
            model_desc=MODEL_DESCRIPTION,
            produit=produit,
            couleur=couleur,
        )

        print(f"  🎨 Génération pose '{pose}'...")
        try:
            if pose == "flatlay" or model_image_id is None:
                result = generate_text_only(prompt, output_path)
            else:
                result = generate_with_image_guidance(prompt, model_image_id, output_path)

            print(f"  ✅ {pose} → {output_path}")
            resultats[pose] = output_path
        except Exception as e:
            print(f"  ❌ Erreur {pose} : {e}")

        time.sleep(1)

    return resultats


def main():
    parser = argparse.ArgumentParser(description="Leonardo.ai Photo Generator — modèle référent Vinted")
    parser.add_argument("--produit", help="Nom du produit")
    parser.add_argument("--couleur", default="pastel", help="Couleur principale")
    parser.add_argument("--output-dir", default="./images", help="Dossier de sortie")
    parser.add_argument("--poses", default="face,dos,flatlay", help="Poses séparées par virgule")
    parser.add_argument("--product-photo", help="Photo produit AliExpress (optionnel)")
    parser.add_argument("--batch", help="Fichier JSON batch")
    parser.add_argument("--api-key", help="Clé API Leonardo (override API_KEY)")

    args = parser.parse_args()

    global API_KEY
    if args.api_key:
        API_KEY = args.api_key

    if args.batch:
        with open(args.batch, "r") as f:
            produits = json.load(f)
        print(f"📦 Batch : {len(produits)} produits\n")
        for p in produits:
            print(f"─── {p['produit']} ───")
            generer_photos_produit(
                produit=p["produit"],
                couleur=p.get("couleur", "pastel"),
                output_dir=os.path.join(args.output_dir, re.sub(r"[^a-z0-9]+", "_", p["produit"].lower())),
                poses=p.get("poses", ["face", "dos", "flatlay"]),
            )
    else:
        if not args.produit:
            print("❌ --produit requis")
            sys.exit(1)
        poses = [p.strip() for p in args.poses.split(",")]
        print(f"🎨 Génération : {args.produit} ({args.couleur})")
        resultats = generer_photos_produit(args.produit, args.couleur, args.output_dir, poses)
        print(f"\n✅ {len(resultats)} photos générées :")
        for pose, path in resultats.items():
            print(f"   {pose}: {path}")


if __name__ == "__main__":
    main()
