# PRODUCTION CONFIG — Instructions pour l'Agent Production
Dernière mise à jour : 15 mars 2026

---

## COMPTE VINTED ACTIF

**Profil Chrome :** Vinted Niche 3
**Email :** billyprofil1@gmail.com
**Niche :** Coquette Aesthetic (printemps 2026)

⚠️ L'agent production ne poste QUE sur ce compte. Jamais un autre.

---

## CHEMINS FICHIERS

- **Input :** /mnt/mon-associe-fichier/VINTED_FORMATION/SOURCING_RESULTATS.md
- **Output :** /mnt/mon-associe-fichier/VINTED_FORMATION/PRODUCTION_ANNONCES.md
- **Photos :** /mnt/mon-associe-fichier/VINTED_FORMATION/images/
- **Clé API Gemini :** AIzaSyBfHkhEPQusg76hLXMBkS4ra-PzDcl9Nn4
- **Script photo :** /mnt/mon-associe-fichier/VINTED_FORMATION/gemini_photo.py
- **Templates descriptions :** /mnt/mon-associe-fichier/VINTED_FORMATION/TOOL_DESCRIPTIONS_VINTED.md

---

## PROCESS POUR CHAQUE PRODUIT

1. Lire le produit dans SOURCING_RESULTATS.md
2. Générer la photo via Gemini API (script gemini_photo.py)
   - Ratio 4:3 obligatoire
   - Fond blanc, mannequin invisible ou flatlay
   - Style RND : Réaliste, Naturel, Démarqué
3. Générer la description Vinted (templates dans TOOL_DESCRIPTIONS_VINTED.md)
   - Varier les formulations (anti-détection)
   - Mentionner toujours : taille, état, matière estimée
   - Pas de fausse marque
4. Assembler la fiche complète dans PRODUCTION_ANNONCES.md

---

## FORMAT PRODUCTION_ANNONCES.md

Pour chaque annonce :
```
---
PRODUIT : [nom]
COMPTE : billyprofil1@gmail.com (Vinted Niche 3)
PHOTO : images/[nom_fichier].png
TITRE VINTED : [max 60 caractères]
CATÉGORIE : [catégorie Vinted]
TAILLE : [S/M/L/etc.]
ÉTAT : Neuf avec étiquette
PRIX : [€]
DESCRIPTION :
[texte complet]
---
```

---

## RÈGLES ANTI-DÉTECTION

- Jamais les mêmes photos que d'autres comptes
- Varier les descriptions même pour produits similaires
- Délai entre posts : 3-5 minutes minimum
- Max 10 annonces par jour sur ce compte au départ

---

## OBJECTIF CE RUN

Produire 10 annonces Coquette Aesthetic prêtes à poster.
Prix minimum : 45€. Marge minimum : x3.

---

## INJECTION EXIF (OBLIGATOIRE sur chaque photo générée)

Après génération de chaque image, injecter des métadonnées iPhone réalistes :

```python
import piexif, struct
from PIL import Image

def inject_exif(image_path):
    img = Image.open(image_path)
    exif_dict = {
        '0th': {
            piexif.ImageIFD.Make: b'Apple',
            piexif.ImageIFD.Model: b'iPhone 15',
            piexif.ImageIFD.Software: b'17.4.1',
        },
        'Exif': {
            piexif.ExifIFD.LensModel: b'iPhone 15 back camera 6.86mm f/1.78',
            piexif.ExifIFD.FocalLength: (686, 100),
            piexif.ExifIFD.FNumber: (178, 100),
        },
        'GPS': {}
    }
    exif_bytes = piexif.dump(exif_dict)
    img.save(image_path, exif=exif_bytes)
```

Appeler inject_exif(path) sur chaque image avant de l'inclure dans l'annonce.
Installer si besoin : pip install piexif --break-system-packages
