# Process de Production d'Images Vinted

> LE FICHIER LE PLUS IMPORTANT — contient tout le process pour générer des annonces parfaites

---

## Prérequis

- **API Gemini :** clé `AIzaSyCGVwWF9ZZ5lzcPf_q2fBRiQWTJWAbi_gA`
- **Modèle :** `gemini-2.5-flash-image`
- **Dépendances :**
  ```bash
  pip install google-genai piexif Pillow --break-system-packages
  ```

---

## Étape 1 — Identifier les articles dans le panier Temu

- Ouvrir le panier Temu (compte **Logipro** sur Chrome)
- Articles **DÉCOCHÉS** = pas encore publiés
- Articles **COCHÉS** = déjà traités
- Lister avec : nom + goods_id + catégorie (vêtement ou déco)

---

## Étape 2 — Trier par compte/persona

| Style du produit | Compte cible |
|-----------------|--------------|
| Dark chic, élégant, noir | janne78550 |
| Minimaliste, neutre, casual | eva_76800 |
| Romantique, floral, bohème | carol76800 |
| Déco, maison, luminaires | sandra4308 |

**TOUJOURS présenter le plan AVANT d'exécuter** (quel article → quel compte → pourquoi)

---

## Étape 3 — Anti-doublon (OBLIGATOIRE)

1. Ouvrir le profil Vinted du compte cible
2. Scanner TOUS les articles déjà postés (voir DATA/STATS_COMPTES.md)
3. Vérifier qu'aucun article similaire n'existe déjà
4. Noter le type de modèle du compte (blonde/brune) pour cohérence des images

---

## Étape 4 — Capturer les photos fournisseur

**RÈGLE ABSOLUE : JAMAIS générer sans photo fournisseur**

1. Ouvrir la page Temu du produit via le goods_id
2. Vérifier que l'article EST dans le panier Temu (sinon → ajouter d'abord)
3. Capturer minimum 2-3 photos : face, dos, détail matière
4. **NETTOYER les captures** : cropper pour enlever TOUT élément d'interface Temu
   - Supprimer : boutons play, vignettes de navigation, barres d'interface, icônes
   - Garder : uniquement le produit et son fond

---

## Étape 5 — Générer Image 1 (face)

### Pour les VÊTEMENTS

Charger les photos fournisseur nettoyées comme références.

Le prompt DOIT contenir :
- Description **EXACTE** de chaque détail du produit (couleur précise, liseré, boutons, coupe, longueur, matière)
- `"Mirror selfie, PHONE HELD IN FRONT OF FACE hiding the face"`
- `"Un bras levé tient le téléphone, l'autre détendu le long du corps"`
- `"Full body photo showing the entire garment from head to toe"`
- Description du décor selon le persona du compte (voir PERSONAS/)
- `"Casual amateur photo, NOT professional, NOT editorial, like a real Vinted listing"`
- `"Smartphone camera quality, slight grain, natural lighting"`

### Pour la DÉCO

- Photo 1 = produit **ÉTEINT / PAS INSTALLÉ**
- Style "je viens de recevoir mon colis et je prends une photo rapide"
- Décor : comptoir de cuisine ou table normale
- Lumière du jour naturelle
- PAS de fumée/vapeur pour les diffuseurs
- PAS de mise en scène pro/catalogue
- Éventuellement : carton ou papier d'emballage visible à côté

---

## Étape 6 — Générer Image 2 (dos)

### Pour les VÊTEMENTS

Charger : photos fournisseur (2-3) + **IMAGE 1 GÉNÉRÉE comme 4e référence**.

Le prompt DOIT contenir :
- `"EXACT SAME person as in the previous image"`
- `"SAME hair color, SAME face shape, SAME body type, SAME build"`
- `"SAME room, SAME lighting, SAME mirror"`
- `"Seen from BEHIND — back facing camera — NOT a 3/4 angle"`
- Décrire les détails visibles de dos (coutures, fermeture, coupe)
- `"Mirror selfie from behind"`

### Pour la DÉCO

- Photo 2 = produit posé par terre OU en légère utilisation
- Pour les suspensions lumineuses : posé par terre ou tenu en main (PAS accroché de façon magazine)
- Pour les diffuseurs : LED allumée doucement, PAS de fumée
- Pas de mains visibles sauf si nécessaire pour montrer l'échelle
- NO watermarks, NO timestamps, NO UI elements

---

## Étape 7 — Post-traitement EXIF (OBLIGATOIRE)

Injecter des métadonnées iPhone 15 réalistes sur chaque image générée.

```python
from PIL import Image
import piexif

def inject_exif(input_path, output_path, date_str="2026:03:21 16:42:08"):
    """
    date_str format: "YYYY:MM:DD HH:MM:SS"
    VARIER la date entre chaque image (±quelques heures/jours)
    """
    img = Image.open(input_path)

    zeroth_ifd = {
        piexif.ImageIFD.Make: b"Apple",
        piexif.ImageIFD.Model: b"iPhone 15",
        piexif.ImageIFD.Software: b"17.4.1",
        piexif.ImageIFD.Orientation: 1,
    }
    exif_ifd = {
        piexif.ExifIFD.LensMake: b"Apple",
        piexif.ExifIFD.LensModel: b"iPhone 15 back camera 6.765mm f/1.6",
        piexif.ExifIFD.FocalLength: (6765, 1000),
        piexif.ExifIFD.FNumber: (16, 10),
        piexif.ExifIFD.ISOSpeedRatings: 100,
        piexif.ExifIFD.ExposureTime: (1, 125),
        piexif.ExifIFD.DateTimeOriginal: date_str.encode(),
        piexif.ExifIFD.ColorSpace: 1,
    }
    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd}
    exif_bytes = piexif.dump(exif_dict)
    img.save(output_path, "JPEG", quality=95, exif=exif_bytes)

# Exemple d'utilisation
inject_exif("image1_raw.jpg", "image1_final.jpg", "2026:03:19 14:23:11")
inject_exif("image2_raw.jpg", "image2_final.jpg", "2026:03:19 14:25:47")
```

**Règles EXIF :**
- VARIER la date DateTimeOriginal entre chaque image (décalage de quelques minutes à quelques jours)
- NE PAS utiliser exactement la même date pour tous les articles
- Résolution idéale en sortie : 3024×4032 ou 4032×3024

---

## Étape 8 — Fiche produit

### Titre
- Max **50 caractères**
- Accrocheur, mentionner "Neuf" ou "Neuve"
- Exemple : `Robe fleurie longue bohème Neuve M` (36 chars)

### Description
- Style naturel (comme une vraie vendeuse, pas un catalogue)
- Mentionner : matière + couleur exacte + détails + taille + état (neuf)
- 3-5 phrases, pas de majuscules abusives
- Exemple : `Magnifique robe longue fleurie, portée jamais. Tissu léger et fluide, imprimé floral multicolore. Taille 38 (M). Idéale pour l'été, se porte avec des sandales ou des mules.`

### Hashtags
- 15 à 20 hashtags pertinents
- Mélanger : style + couleur + matière + occasion + saison

### Marque
- Toujours : **"Sans marque"**
- JAMAIS mentionner Temu ou AliExpress

### Prix
- Marge ×3 à ×4 sur le prix fournisseur
- Respecter la grille (voir STRATEGIE/PRICING.md)

---

## ERREURS À NE JAMAIS REPRODUIRE

| # | Erreur | Solution |
|---|--------|----------|
| 1 | 2 modèles différents entre image 1 et 2 | Toujours passer image 1 comme référence pour image 2 |
| 2 | Vue 3/4 au lieu du dos | Prompt : "BACK facing camera, NOT 3/4 angle" |
| 3 | Selfie avec visage visible | Prompt : "PHONE IN FRONT OF FACE, hiding the face" |
| 4 | Générer sans photo fournisseur | INTERDIT — toujours capturer d'abord |
| 5 | Photos déco trop pro/catalogue | Prompt : "amateur smartphone photo, NOT professional" |
| 6 | Artefacts Temu (bouton play, icônes) | Nettoyer/cropper les captures AVANT génération |
| 7 | Fumée/vapeur sur diffuseurs | JAMAIS — photo produit éteint ou LED discrète |
| 8 | Produit déco parfaitement installé | Montrer comme "déballé" ou "posé par terre" |
| 9 | Même date EXIF sur tous les articles | VARIER les dates de ±quelques heures/jours |
| 10 | Fond blanc studio | JAMAIS — décor naturel selon persona |

---

## Checklist finale avant publication

- [ ] Photo fournisseur capturée et nettoyée
- [ ] Plan présenté (article → compte → justification)
- [ ] Anti-doublon vérifié
- [ ] Image 1 générée avec décor persona correct
- [ ] Image 2 générée avec image 1 comme référence (cohérence modèle)
- [ ] EXIF iPhone 15 injectés avec date variée
- [ ] Titre ≤ 50 caractères
- [ ] Description naturelle (pas catalogue)
- [ ] 15-20 hashtags
- [ ] Marque = "Sans marque"
- [ ] Prix dans la grille
- [ ] Publication depuis app Vinted mobile
- [ ] Vérification statut "Actif" sous 24h
