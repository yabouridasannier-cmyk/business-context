#!/usr/bin/env python3
"""
TEMU IMAGE DOWNLOADER — Récupère l'image principale de chaque produit Temu
Lit le fichier batch_temu_19mars.json et télécharge product_reference.jpg dans chaque output_dir.

Usage:
    python3 download_temu_images.py

Prérequis:
    pip3 install playwright
    python3 -m playwright install chromium
"""

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("Playwright manquant. Lance: pip3 install playwright && python3 -m playwright install chromium")
    sys.exit(1)

# === CONFIG ===
BASE_DIR = Path(__file__).parent
BATCH_FILE = BASE_DIR / "batch_temu_19mars.json"
GOODS_IDS = {
    "T01": "601104737281058",  # Robe longue fleurie
    "T02": "601104437271347",  # Pochette florale
    "T03": "601105232373234",  # Robe rose col V
    "T04": "606564220018921",  # Prunier blanc
    "T05": "601102915448307",  # Lampe plumes
    "T06": "601101595249269",  # Nappe dentelle
    "T07": "605649056427971",  # Robe blanche soirée
    "T08": "601100307307721",  # Tapis peluche
    "T09": "601101276070647",  # Ensemble chemise+jupe
    "T10": "601100062305755",  # Table chevet ours
    "T11": "601101608521864",  # Tapis salon crème
    "T12": "601100848196298",  # Diffuseur bois LED
    "T13": "601105433182787",  # Toile moderne
    "T14": "601104264518568",  # Tapis ananas
    "T15": "605602717784721",  # Abat-jour rotin
    "T16": "601104450967442",  # Tapis nordique
    "T17": "601101613847946",  # Hirondelles dorées
    "T18": "603729239628713",  # Support fleurs
    "T19": "601102292340053",  # Panier chanvre
    "T20": "601105315512770",  # Jeans AC
    "T21": "601105610017168",  # Chaussures skate
    "T22": "605755423999598",  # Veste capuche
    "T23": "605644493012013",  # Ensemble bomber
    "T24": "606121771241326",  # Ensemble top+pantalon
}

EXTRACT_JS = """
() => {
    // Wait until product images appear in the top zone
    const imgs = [...document.querySelectorAll('img')]
        .filter(i => {
            const s = i.src || '';
            return s.includes('img.kwcdn.com/product/')
                && !s.includes('fancy/c83e5236')  // exclude generic temu icon
                && i.naturalWidth > 200;
        })
        .sort((a, b) => {
            const aTop = a.getBoundingClientRect().top;
            const bTop = b.getBoundingClientRect().top;
            return aTop - bTop;
        });
    if (imgs.length === 0) return null;
    return imgs[0].src.split('?')[0];
}
"""


def download_image(url: str, save_path: str) -> bool:
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, "wb") as f:
                f.write(resp.read())
        return True
    except Exception as e:
        print(f"    [ERREUR DL] {e}")
        return False


def get_image_url(page, goods_id: str):
    url = f"https://www.temu.com/fr/goods.html?goods_id={goods_id}"
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=20000)
        # Wait for product images to appear
        page.wait_for_function(
            """() => {
                const imgs = [...document.querySelectorAll('img')]
                    .filter(i => i.src && i.src.includes('img.kwcdn.com/product/') && i.naturalWidth > 200);
                return imgs.length > 0;
            }""",
            timeout=15000
        )
        img_url = page.evaluate(EXTRACT_JS)
        return img_url
    except PlaywrightTimeout:
        # Try anyway — maybe some images loaded
        try:
            img_url = page.evaluate(EXTRACT_JS)
            return img_url
        except:
            return None
    except Exception as e:
        print(f"    [ERREUR PAGE] {e}")
        return None


def main():
    # Load batch
    with open(BATCH_FILE) as f:
        batch = json.load(f)

    print(f"[START] {len(batch)} produits à traiter\n")

    results = {"ok": [], "failed": []}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            locale="fr-FR",
            viewport={"width": 1280, "height": 900}
        )
        page = context.new_page()

        # Load Temu once to get cookies
        print("[INIT] Chargement initial de Temu...")
        try:
            page.goto("https://www.temu.com/fr", wait_until="domcontentloaded", timeout=15000)
        except:
            pass

        for i, item in enumerate(batch):
            num = f"T{str(i+1).zfill(2)}"
            goods_id = list(GOODS_IDS.values())[i]
            output_dir = BASE_DIR / item["output_dir"]
            save_path = str(output_dir / "product_reference.jpg")
            produit = item["produit"][:50]

            print(f"[{i+1:02d}/24] {num} — {produit}")

            # Skip if already downloaded
            if os.path.exists(save_path):
                print(f"    [SKIP] Déjà téléchargé")
                results["ok"].append(num)
                continue

            img_url = get_image_url(page, goods_id)

            if img_url:
                print(f"    [IMG] {img_url[-60:]}")
                ok = download_image(img_url, save_path)
                if ok:
                    print(f"    [OK] Sauvegardé → {item['output_dir']}/product_reference.jpg")
                    results["ok"].append(num)
                else:
                    results["failed"].append((num, goods_id))
            else:
                print(f"    [FAIL] Aucune image trouvée pour goods_id={goods_id}")
                results["failed"].append((num, goods_id))

        browser.close()

    print(f"\n{'='*50}")
    print(f"[DONE] {len(results['ok'])}/24 images téléchargées")
    if results["failed"]:
        print(f"[FAIL] {len(results['failed'])} échecs :")
        for num, gid in results["failed"]:
            print(f"   {num} — goods_id={gid}")
        print("\nPour les relancer manuellement, ajoute goods_id= dans le navigateur et screenshot le produit.")


if __name__ == "__main__":
    main()
