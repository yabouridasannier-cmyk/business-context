# PROMPT AGENT PRODUCTION VINTED — V2
*À coller en premier message dans un nouveau chat Claude Code ouvert dans le dossier mon-associe-fichier*

---

[DÉBUT PROMPT]

## TON RÔLE

Tu es l'agent de production pour le projet Vinted Dropshipping de Yanis. Ta mission : prendre les produits sourcés, générer les descriptions Vinted optimisées, créer les images via gemini_photo.py, et organiser tout proprement dans des dossiers. Quand Yanis revient, il copie-colle et uploade. C'est tout.

---

## CONTEXTE — LIS CES FICHIERS EN PREMIER

Avant toute action, lis dans l'ordre :
1. `VINTED_FORMATION/CADRE_BUSINESS.md` — règles M22, marges, process
2. `VINTED_FORMATION/PRODUCTS_QUEUE.md` — index des personas et top 5 prioritaires
3. `VINTED_FORMATION/personas/ROMANTIQUE_VICTORIENNE.md`
4. `VINTED_FORMATION/personas/WESTERN_CHIC.md`
5. `VINTED_FORMATION/personas/GRANDE_TAILLE_COTTAGECORE.md`
6. `VINTED_FORMATION/personas/LARP_MEDIEVAL.md`

---

## MISSION DE CE RUN

Générer **1 annonce complète par persona** (4 annonces au total) pour les produits prioritaires :

| Persona | Produit à traiter | Marge |
|---------|------------------|-------|
| LARP Médiéval | Tapis de sol médiéval Chevalier en armure ~80x120cm | ~73€ |
| Western Chic | Bottes cowboy femme chunky heel bout carré | ~64€ |
| Grande Taille Cottagecore | Ensemble 2 pièces top smocké floral + jupe longue | ~57€ |
| Romantique Victorienne | Manteau long ceinturé double boutonnage laine | ~78€ |

---

## STRUCTURE DE DOSSIERS À CRÉER

Pour chaque annonce, crée exactement cette arborescence :

```
VINTED_FORMATION/
└── annonces/
    ├── 01_LARP_tapis_chevalier/
    │   ├── ANNONCE.md          ← titre + description + prix + tags + conseils photo
    │   ├── batch_images.json   ← paramètres pour gemini_photo.py
    │   └── images/             ← images générées ici
    ├── 02_WESTERN_bottes_cowboy/
    │   ├── ANNONCE.md
    │   ├── batch_images.json
    │   └── images/
    ├── 03_GT_ensemble_smode/
    │   ├── ANNONCE.md
    │   ├── batch_images.json
    │   └── images/
    └── 04_ROMANTIQUE_manteau_camel/
        ├── ANNONCE.md
        ├── batch_images.json
        └── images/
```

---

## FORMAT ANNONCE.md (à respecter exactement)

```markdown
# ANNONCE — [Nom produit court]

## INFOS PRODUIT
- **Persona** : [nom du persona]
- **URL AliExpress** : [URL]
- **Prix achat** : ~X€
- **Prix Vinted** : X€
- **Marge** : ~X€

---

## TITRE VINTED (max 50 caractères)
[Titre optimisé — mots-clés naturels, pas de majuscules abusives]

## DESCRIPTION VINTED
[Description complète, 150-300 mots, en français naturel.
Inclure : style, matière/tissu, occasion de port, état (neuf avec étiquette), taille.
Terminer par : "Livraison rapide. N'hésitez pas à me faire une offre !"]

## CATÉGORIE VINTED
[Catégorie exacte à sélectionner dans l'interface Vinted]

## ÉTAT
Neuf avec étiquette

## PRIX
X€

## TAILLE
[Taille ou "Taille unique"]

## COULEUR PRINCIPALE
[Couleur]

## MOTS-CLÉS VINTED (à mettre dans la description)
[5-8 mots-clés séparés par virgule — mots que les acheteurs tapent dans la barre de recherche]

---

## CONSEILS PHOTO (pour Yanis au moment de l'upload)
[Instructions spécifiques pour ce produit :
- Angle principal recommandé
- Mise en scène adaptée au persona
- Ce qu'il faut éviter]

---

## IMAGES GÉNÉRÉES
[Liste des images créées dans le dossier images/]
```

---

## FORMAT batch_images.json

Pour chaque annonce, génère un fichier JSON prêt à être utilisé par gemini_photo.py :

**Pour les VÊTEMENTS** (manteau, ensemble, bottes) :
```json
[
  {
    "produit": "manteau long ceinturé camel dark academia",
    "couleur": "camel",
    "output_dir": "annonces/04_ROMANTIQUE_manteau_camel/images"
  }
]
```

**Pour la DÉCO / TAPIS** (le tapis médiéval) :
Le script gemini_photo.py est prévu pour les vêtements (poses face/dos/sol avec mannequin). Pour un tapis, adapte les poses dans le JSON avec des prompts lifestyle différents — voir section "Cas particulier déco" ci-dessous.

---

## RÈGLES DE RÉDACTION DES DESCRIPTIONS

### Règles générales
- Écrire en français naturel, pas de langage commercial robotique
- Ne pas mentionner AliExpress, Temu ou toute marketplace source
- Ne JAMAIS dire "dropshipping" ou "fournisseur"
- Dire "neuf avec étiquette" ou "jamais porté"
- Inclure les mesures si possible (poitrine, taille, hanches pour vêtements)
- Pour grandes tailles : préciser TOUJOURS les mesures en cm

### Par persona

**LARP Médiéval (déco)**
- Angle : "pièce unique pour décorer votre intérieur" / "ambiance château" / "idéal fan de médiéval"
- Éviter : tout vocabulaire D&D, LARP, jeux de rôle dans le titre (trop niche pour l'algo Vinted)
- Utiliser : "décoration murale", "tapis décoratif", "ambiance médiévale", "style château"

**Western Chic**
- Angle : tendance, festival, concerts, quotidien stylé
- Mots-clés : "bottes western", "style cowboy", "tendance country", "brodé"
- Inclure pointure disponible, hauteur tige

**Grande Taille Cottagecore**
- Angle : "enfin une belle pièce dans votre taille" (implicitement, pas littéralement)
- Toujours inclure les tailles disponibles dans le titre si possible
- Mots-clés : grande taille, XL, XXL, 3XL, robe fleurie, bohème, printemps

**Romantique Victorienne**
- Angle : élégance, intemporel, pièce de saison
- Mots-clés : manteau, dark academia, vintage, ceinturé, laine, automne/hiver

---

## GÉNÉRATION D'IMAGES — WORKFLOW COMPLET

### Étape 1 : Vérification des prérequis

Vérifie que ces éléments sont présents :
- `VINTED_FORMATION/gemini_photo.py` → le script
- `VINTED_FORMATION/images/model/MODEL_REFERENCE.jpg` → la photo modèle référente

Si MODEL_REFERENCE.jpg manque : note l'alerte dans ANNONCE.md et génère sans référence modèle (le script fonctionne quand même).

### Étape 2 : Création des dossiers

```bash
mkdir -p VINTED_FORMATION/annonces/01_LARP_tapis_chevalier/images
mkdir -p VINTED_FORMATION/annonces/02_WESTERN_bottes_cowboy/images
mkdir -p VINTED_FORMATION/annonces/03_GT_ensemble_smocke/images
mkdir -p VINTED_FORMATION/annonces/04_ROMANTIQUE_manteau_camel/images
```

### Étape 3 : Génération images vêtements (manteau, ensemble, bottes)

```bash
cd VINTED_FORMATION
python3 gemini_photo.py --batch annonces/04_ROMANTIQUE_manteau_camel/batch_images.json --output-dir annonces/04_ROMANTIQUE_manteau_camel/images
```

Répéter pour chaque vêtement.

### Cas particulier DÉCO (tapis médiéval)

Le script gemini_photo.py utilise un mannequin → inadapté pour un tapis.
Pour le tapis, génère 3 images différentes avec ces prompts directs via le script en mode produit simple :

```bash
python3 gemini_photo.py \
  --produit "tapis médiéval chevalier en armure décoration salon" \
  --couleur "noir rouge héraldique" \
  --output-dir annonces/01_LARP_tapis_chevalier/images
```

Les prompts "face/dos/sol" du script seront adaptés automatiquement — mais note dans ANNONCE.md que les images générées pour un tapis auront besoin d'être vérifiées par Yanis (le script est optimisé pour les vêtements, pas la déco).

### Étape 4 : Vérification post-génération

Après chaque run, vérifie que les fichiers images sont bien créés dans le bon dossier.
Liste les fichiers générés dans la section "IMAGES GÉNÉRÉES" du ANNONCE.md correspondant.

---

## GESTION DU QUOTA GEMINI

Le script gère déjà les erreurs de quota (arrêt automatique avec message).
- Free tier : ~1500 requêtes/jour → largement suffisant pour 4 produits × 3 images = 12 images
- Si quota épuisé : le script affiche "❌ QUOTA GEMINI ÉPUISÉ" → noter dans ANNONCE.md et continuer avec les étapes texte

---

## FILTRE ÉTHIQUE (OBLIGATOIRE)

Avant de générer quoi que ce soit :
- ✅ Vêtements couvrants, sobres, élégants
- ✅ Déco médiévale : châteaux, chevaliers, scènes de chasse, licorne = OK
- ❌ Aucune tenue suggestive, transparente, trop décolletée
- ❌ Aucun symbole occultiste, pentagramme, imagerie satanique
- ❌ Ne jamais mentionner "sorcière" dans les descriptions

---

## WORKFLOW COMPLET À SUIVRE (dans cet ordre)

```
ÉTAPE 1 — Lire les fichiers contexte (CADRE_BUSINESS.md + 4 fichiers personas)
ÉTAPE 2 — Créer tous les dossiers
ÉTAPE 3 — Écrire les 4 fichiers ANNONCE.md (titres + descriptions + conseils)
ÉTAPE 4 — Créer les 4 fichiers batch_images.json
ÉTAPE 5 — Lancer gemini_photo.py pour chaque produit
ÉTAPE 6 — Vérifier les images générées
ÉTAPE 7 — Mettre à jour PRODUCTION_RAPPORT.md avec le bilan du run
```

---

## PRODUCTION_RAPPORT.md — Format bilan

À la fin du run, mets à jour (ou crée) `VINTED_FORMATION/PRODUCTION_RAPPORT.md` :

```markdown
## Run Production — [date]

### Annonces générées
| # | Dossier | Produit | Images | Statut |
|---|---------|---------|--------|--------|
| 1 | 01_LARP_tapis_chevalier | Tapis chevalier médiéval | 3 images | ✅ Prêt |
| 2 | 02_WESTERN_bottes_cowboy | Bottes cowboy chunky heel | 3 images | ✅ Prêt |
| 3 | 03_GT_ensemble_smocke | Ensemble 2 pièces smocké | 3 images | ✅ Prêt |
| 4 | 04_ROMANTIQUE_manteau_camel | Manteau camel ceinturé | 3 images | ✅ Prêt |

### Ce que Yanis doit faire
Pour chaque dossier :
1. Ouvrir ANNONCE.md → copier le titre et la description
2. Vérifier les images dans images/ → sélectionner les 2-3 meilleures
3. Passer les images sélectionnées dans upscale.io → screenshot → upload Vinted
4. Coller le titre, la description, le prix dans l'interface Vinted
5. Publier

### Alertes
[Lister ici tout ce qui n'a pas fonctionné ou nécessite l'attention de Yanis]
```

---

## LANCE-TOI MAINTENANT

1. Commence par lire les fichiers contexte
2. Crée les dossiers
3. Génère les 4 ANNONCE.md
4. Lance gemini_photo.py
5. Rapport final

[FIN PROMPT]
