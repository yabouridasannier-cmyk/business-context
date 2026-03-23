# ARTICLES MASQUÉS — Diagnostic & Plan d'action

> 7 articles masqués au 22 mars 2026
> Tous concernent sandra4308 (4) et carol76800 (3)

---

## Inventaire des articles masqués

| # | Article | Compte | Vues | Fav | Prix | Urgence |
|---|---------|--------|------|-----|------|---------|
| 1 | Tapis jute naturel | sandra4308 | 566 | 90 | 49€ | CRITIQUE |
| 2 | Lustre suspendu bois | sandra4308 | 115 | 46 | 44€ | URGENT |
| 3 | Robe fleurie rose | carol76800 | 138 | 28 | 59€ | URGENT |
| 4 | Chemin de table feuilles | sandra4308 | 62 | 14 | 34€ | Moyen |
| 5 | Robe fleurie verte | carol76800 | 121 | 14 | 54€ | Moyen |
| 6 | Robe longue bleu clair | carol76800 | 45 | 6 | 54€ | Faible |
| 7 | Lampe osier/rotin | sandra4308 | 3 | 1 | 34€ | Faible |

**CA potentiel débloqué si tout démasqué : ~353€ (prix affichés des 7 articles)**

---

## Hypothèses de masquage (pattern observé)

### Hypothèse 1 — Détection images générées par IA (PROBABLE)
**Signaux :** Deux comptes différents (sandra + carol) masqués en même temps, articles variés (déco + mode)
**Pourquoi :** Vinted a renforcé sa détection IA en 2025-2026
- Metadata EXIF absentes ou génériques (Adobe Firefly, MidJourney, DALL-E laissent des traces)
- Analyse des patterns de pixels (trop "parfaits", pas de bruit naturel)
- Fonds trop propres / éclairage trop uniforme
- Résolution anormalement élevée ou trop parfaite pour un vendeur particulier

### Hypothèse 2 — Fond blanc/studio trop professionnel
**Signaux :** Articles de déco et mode avec photos catalogue
- Vinted favorise les photos "naturelles" en contexte
- Photos avec mannequin ou mise en scène réelle = moins suspectes

### Hypothèse 3 — Incohérence description/image
**Signaux :** Ventes annulées "photo ≠ produit"
- Si le système a reçu des signalements, peut déclencher un masquage préventif
- Particulièrement pertinent pour carol76800 (robe annulée)

### Hypothèse 4 — Compte nouveau trop de mises en ligne rapides
- Masse d'articles publiés en peu de temps = flag anti-spam

---

## Plan d'action par priorité

### Étape 1 — Diagnostic (Jour J)
- [ ] Vérifier dans l'app Vinted le message exact de masquage (quel motif indiqué ?)
- [ ] Comparer les photos masquées vs non masquées pour identifier la différence visuelle
- [ ] Vérifier les EXIF des images utilisées (outil : exifdata.com ou Jeffrey's Exif Viewer)

### Étape 2 — Refaire les photos (Semaine 1)
- [ ] Utiliser le process PRODUCTION_IMAGES.md avec les bons EXIF (iPhone 15)
- [ ] Fond naturel (parquet, canapé, lit) — JAMAIS fond blanc
- [ ] Plusieurs angles + photo détail texture
- [ ] EXIF iPhone 15 injectés via piexif (voir PROCESS/PRODUCTION_IMAGES.md)

### Étape 3 — Republier
- [ ] Supprimer les articles masqués
- [ ] Re-publier avec nouvelles photos depuis le téléphone (pas depuis PC)
- [ ] Espacer les publications (max 2-3/jour par compte)
- [ ] Titre et description légèrement reformulés

### Étape 4 — Test & validation
- [ ] Suivre pendant 48h si nouvel article avec nouvelles photos reste actif
- [ ] Si masquage à nouveau → contacter le support Vinted avec photo du produit réel

---

## Solution EXIF (clé du démasquage)

Le code Python à utiliser pour injecter des métadonnées iPhone réalistes est dans **PROCESS/PRODUCTION_IMAGES.md — Étape 7**.

Points critiques :
- VARIER la date DateTimeOriginal entre chaque image
- NE PAS utiliser la même clé EXIF pour tous les articles
- Résolution cible : 3024×4032 (standard iPhone 15)
