# PRODUCTION RAPPORT

## Run Production — 18 mars 2026

### Annonces générées

| # | Dossier | Produit | Images | Statut |
|---|---------|---------|--------|--------|
| 1 | 01_LARP_tapis_chevalier | Tapis chevalier médiéval 80x120cm | ⚠️ À faire manuellement | ✅ Texte prêt |
| 2 | 02_WESTERN_bottes_cowboy | Bottes cowboy chunky heel bout carré | ⚠️ Quota API épuisé | ✅ Texte prêt |
| 3 | 03_GT_ensemble_smocke | Ensemble 2 pièces smocké floral XL-3XL | ⚠️ Quota API épuisé | ✅ Texte prêt |
| 4 | 04_ROMANTIQUE_manteau_camel | Manteau camel ceinturé double boutonnage | ⚠️ Quota API épuisé | ✅ Texte prêt |

---

### Ce que Yanis doit faire

**ÉTAPE 1 — Débloquer les images (URGENT) :**

Le quota Gemini image est à **0 requêtes/jour** sur le free tier — la génération d'images nécessite la facturation activée :

1. Aller sur [aistudio.google.com](https://aistudio.google.com)
2. Créer un **nouveau projet Google Cloud** avec facturation activée (ou activer billing sur le projet existant)
3. Générer une **nouvelle clé API**
4. Remplacer `API_KEY` dans `VINTED_FORMATION/gemini_photo.py` ligne 49
5. Lancer les 3 vêtements :

```bash
cd VINTED_FORMATION
python3 gemini_photo.py --produit "manteau long ceinturé double boutonnage laine dark academia" --couleur "camel" --output-dir "annonces/04_ROMANTIQUE_manteau_camel/images"
python3 gemini_photo.py --produit "bottes cowboy chunky heel bout carré style western" --couleur "noir cuir" --output-dir "annonces/02_WESTERN_bottes_cowboy/images"
python3 gemini_photo.py --produit "ensemble 2 pièces top smocké floral jupe longue fluide grande taille" --couleur "rose fleuri" --output-dir "annonces/03_GT_ensemble_smocke/images"
```

6. Pour le **tapis médiéval** : gemini_photo.py n'est PAS adapté (optimisé vêtements). Faire les photos manuellement — tapis posé sur parquet, lumière chaude, zoom détail motif.

> Coût si billing activé : ~$0.02-0.04/image × 9 images = **moins de 0,40$**

---

**ÉTAPE 2 — Uploader les annonces :**

Pour chaque dossier :
1. Ouvrir `ANNONCE.md` → copier le **titre** et la **description**
2. Sélectionner 2-3 meilleures images dans `images/`
3. Passer dans **upscale.io** → screenshot → upload Vinted
4. Coller titre, description, prix dans l'interface Vinted
5. Publier

---

### Note technique

Le modèle `gemini-2.0-flash` dans gemini_photo.py ne supporte pas la génération d'images (erreur 400 INVALID_ARGUMENT). Il a été mis à jour vers `gemini-2.5-flash-image` — correct, mais bloqué par quota free tier = 0. Une fois billing activé sur la clé API, le script fonctionnera directement.

---

### Alertes

- ⚠️ **CRITIQUE** : Quota image Gemini free tier = 0 → activer billing avant de relancer
- ⚠️ Tapis médiéval (01) : script optimisé vêtements — photos manuelles obligatoires pour ce produit
- ⚠️ Ensemble grande taille (03) : mannequin slim par défaut, non représentatif — compléter avec photos réelles si possible
- ✅ Toutes les URLs AliExpress à vérifier en live avant commande (note, avis, prix actuel, couleurs)
- ✅ Wakala : envoyer message accord dropshipping aux fournisseurs avant toute commande

---

### Prix et marges

| Annonce | Prix Vinted | Marge |
|---------|-------------|-------|
| Tapis chevalier | 95€ | ~73€ |
| Bottes cowboy chunky | 90€ | ~64€ |
| Ensemble smocké GT | 75€ | ~57€ |
| Manteau camel | 110€ | ~78€ |
| **Total si tout vendu** | **370€** | **~272€** |
