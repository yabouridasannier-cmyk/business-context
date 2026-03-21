# WORKFLOW COMPLET — Système Vinted Dropshipping M22
*Créé le 18 mars 2026 — Vue globale des 2 agents + processus manuels*

---

## CARTE MENTALE — VUE D'ENSEMBLE

```
                    ┌─────────────────────────────────────┐
                    │         YANIS (Décideur)             │
                    │  - Valide les liens AliExpress       │
                    │  - Publie sur Vinted                 │
                    │  - Répond aux acheteurs              │
                    │  - Déclare les ventes (review J+3)   │
                    │  - Lives M22 = nouvelles niches      │
                    └──────────┬──────────┬───────────────┘
                               │          │
              ┌────────────────┘          └────────────────┐
              ▼                                            ▼
┌──────────────────────────┐            ┌──────────────────────────────┐
│   🔍 AGENT SOURCING      │            │   🏭 AGENT PRODUCTION        │
│   (PROMPT V2)             │            │   (PROMPT V4)                │
│                           │            │                              │
│ 1. Lit personas/*.md      │────────▶   │ 1. Lit personas/*.md         │
│ 2. Cherche AliExpress     │  produits  │ 2. Lit CADRE_BUSINESS.md     │
│ 3. Vérifie liens ⚠️       │  sourcés   │ 3. Génère ANNONCE.docx       │
│ 4. Compare fournisseurs   │            │ 4. Génère images (Gemini)    │
│ 5. Envoie liens à Yanis   │            │ 5. Classe dans annonces/     │
│    pour double check       │            │ 6. Rapport de production     │
└──────────────────────────┘            └──────────────────────────────┘
```

---

## PHASE 1 — SOURCING (Agent Sourcing V2)

```
┌──────────────────────────────────────────────────────────────────┐
│                     FLUX SOURCING                                │
│                                                                  │
│  ENTRÉE                                                          │
│  ├── personas/*.md          (profil + produits existants)        │
│  ├── CADRE_BUSINESS.md      (règles marges, x3-x5, min 40€)    │
│  └── PRODUCTS_QUEUE.md      (index des personas)                │
│                                                                  │
│  PROCESSUS                                                       │
│  ├── 1. Identifier les catégories manquantes                    │
│  │      └── Règle diversité : TOP 5 = 5 catégories ≠           │
│  ├── 2. Recherche AliExpress (WebSearch)                        │
│  │      └── Objectif : liens DIRECTS /item/100500XXXXX          │
│  │      └── ⚠️ PAS de liens /w/wholesale/ (recherches)          │
│  ├── 3. Vérification métriques (SEUILS BAS — voir note)         │
│  │      ├── Note ≥ 3.5★ (le minimum, pas un critère fort)      │
│  │      ├── Avis ≥ 5                                            │
│  │      └── Vendus ≥ 50                                         │
│  │      └── ⚠️ Métriques = qualité fournisseur, PAS potentiel  │
│  │          produit. Un 3.5★ peut être un produit gagnant !     │
│  ├── 4. Calcul marge                                            │
│  │      ├── Prix achat (produit + livraison FR)                 │
│  │      ├── Prix Vinted (x3 à x5)                               │
│  │      └── Marge nette ≥ 40€ obligatoire                       │
│  └── 5. ✅ NOUVEAU : Envoi liens à Yanis pour double check     │
│                                                                  │
│  SORTIE                                                          │
│  ├── personas/*.md MISE À JOUR (nouveaux produits ajoutés)      │
│  ├── Tableau récap avec liens cliquables                        │
│  └── Statut de chaque lien (✅/⚠️/❌)                           │
│                                                                  │
│  DÉCLENCHEUR COMPARAISON FOURNISSEURS                           │
│  └── Quand un article est VENDU sur Vinted                      │
│      ├── Chercher sur : AliExpress, Temu, DHgate, Shein, 1688  │
│      ├── Comparer : prix + livraison FR                         │
│      └── Format : tableau comparatif + ✅ MOINS CHER            │
└──────────────────────────────────────────────────────────────────┘
```

---

## PHASE 2 — PRODUCTION (Agent Production V4)

```
┌──────────────────────────────────────────────────────────────────┐
│                     FLUX PRODUCTION                              │
│                                                                  │
│  ENTRÉE                                                          │
│  ├── personas/*.md                (produits validés par Yanis)  │
│  ├── CADRE_BUSINESS.md            (règles photos, descriptions) │
│  ├── CYCLE_3_JOURS.md             (combien de quoi produire)   │
│  └── PRODUITS_GAGNANTS/README.md  (variantes à créer)          │
│                                                                  │
│  PROCESSUS                                                       │
│  ├── 1. Créer dossier annonces/NN_PERSONA_produit/              │
│  ├── 2. Générer ANNONCE.docx                                    │
│  │      ├── Titre (max 50 chars)                                │
│  │      ├── Tableau infos (URL, prix, marge)                    │
│  │      ├── Description persona-adaptée                         │
│  │      ├── Paramètres Vinted (catégorie, état, taille)         │
│  │      ├── Mots-clés SEO                                       │
│  │      └── Conseils photo                                       │
│  ├── 3. Générer images via gemini_photo.py                      │
│  │      ├── 3 poses : face + dos + sol                          │
│  │      ├── Style amateur (pas trop pro)                        │
│  │      ├── FIDÈLE au produit réel (pas d'invention)            │
│  │      └── Si échec → images/_archive/ (jamais supprimer)      │
│  └── 4. Créer FICHE_COMPLETE.md (liens + images + Vinted URL)  │
│                                                                  │
│  SORTIE                                                          │
│  ├── annonces/NN_PERSONA_produit/                               │
│  │   ├── ANNONCE.docx         ← copier-coller Vinted           │
│  │   ├── ANNONCE.md           ← référence markdown              │
│  │   ├── FICHE_COMPLETE.md    ← tout centralisé                │
│  │   └── images/                                                 │
│  │       ├── *_face.jpg                                         │
│  │       ├── *_dos.jpg                                          │
│  │       └── *_sol.jpg                                          │
│  └── PRODUCTION_RAPPORT.md (mis à jour)                         │
└──────────────────────────────────────────────────────────────────┘
```

---

## PHASE 3 — CYCLE 3 JOURS (Boucle continue)

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   JOUR 1-3 : Yanis publie 5 annonces/jour × 4 comptes = 20/jour  │
│   ├── Compte 1 : Romantique Victorienne                            │
│   ├── Compte 2 : Western Chic                                      │
│   ├── Compte 3 : Grande Taille Cottagecore                         │
│   └── Compte 4 : LARP Médiéval                                    │
│   (+ futurs : Style Stockholm, Vintage Rétro)                      │
│                                                                     │
│   JOUR 3 : Review — Yanis déclare les ventes                      │
│   │                                                                 │
│   ├── ❌ Article NON vendu après 3 jours                           │
│   │   └──▶ annonces/_archive/[date]/                               │
│   │       └── Dossier entier déplacé (JAMAIS supprimé)             │
│   │                                                                 │
│   └── ✅ Article VENDU (= produit gagnant)                         │
│       ├──▶ PRODUITS_GAGNANTS/[nom_produit]/                        │
│       │   ├── FICHE_PRODUIT.md (original + historique ventes)      │
│       │   ├── VARIANTES.md (2-3 couleurs différentes)              │
│       │   └── annonces/[couleur]/ (ANNONCE.docx + images)          │
│       └──▶ Déclencheur : comparaison fournisseurs multi-plateforme │
│                                                                     │
│   NOUVEAU CYCLE : Composition des 5 annonces suivantes             │
│   ┌───────────────────┬──────────────────┬───────────────────┐     │
│   │ Gagnants cumulés  │ Variantes        │ Nouveaux articles │     │
│   ├───────────────────┼──────────────────┼───────────────────┤     │
│   │ 0 (démarrage)     │ 0                │ 5                 │     │
│   │ 2                 │ 2                │ 3                 │     │
│   │ 3                 │ 3                │ 2                 │     │
│   │ 5                 │ 4                │ 1                 │     │
│   │ Mature            │ 5                │ 0                 │     │
│   └───────────────────┴──────────────────┴───────────────────┘     │
│                                                                     │
│   Objectif : converger vers 100% variantes de gagnants             │
└─────────────────────────────────────────────────────────────────────┘
```

---

## STRUCTURE FICHIERS COMPLÈTE

> **PRINCIPE CLÉ : Niche > Persona > Annonces**
> Chaque persona EST un dossier complet : le fichier .md de sourcing + les annonces produites vivent ENSEMBLE.

```
VINTED_FORMATION/
│
├── 📋 FICHIERS RÉFÉRENCE (read-only, rarement modifiés)
│   ├── CADRE_BUSINESS.md           ← Règles M22, marges, process photos
│   ├── CYCLE_3_JOURS.md            ← Système rotation gagnants/nouveaux
│   ├── WORKFLOW_COMPLET.md         ← CE FICHIER (carte mentale)
│   ├── PROMPT_AGENT_SOURCING_V2.md ← Prompt pour lancer l'agent sourcing
│   ├── PROMPT_AGENT_PRODUCTION_V4.md ← Prompt pour lancer l'agent production
│   └── PRODUCTS_QUEUE.md           ← Index des personas actifs
│
├── 👤 personas/ (TOUT vit ici — sourcing + annonces)
│   │
│   ├── ROMANTIQUE_VICTORIENNE/              ← 1 DOSSIER = 1 NICHE COMPLÈTE
│   │   ├── ROMANTIQUE_VICTORIENNE.md        ← Fichier sourcing (produits, liens, marges)
│   │   └── annonces/                        ← Annonces de cette niche
│   │       ├── 04_manteau_camel/
│   │       │   ├── ANNONCE.docx
│   │       │   ├── FICHE_COMPLETE.md
│   │       │   └── images/
│   │       ├── 05_manteau_bordeaux/         ← 🔥 1er gagnant !
│   │       │   ├── ANNONCE.docx
│   │       │   ├── FICHE_COMPLETE.md
│   │       │   └── images/
│   │       └── _archive/                    ← Annonces non vendues J+3
│   │
│   ├── WESTERN_CHIC/
│   │   ├── WESTERN_CHIC.md
│   │   └── annonces/
│   │       ├── 02_bottes_cowboy/
│   │       └── _archive/
│   │
│   ├── GRANDE_TAILLE_COTTAGECORE/
│   │   ├── GRANDE_TAILLE_COTTAGECORE.md
│   │   └── annonces/
│   │       ├── 03_ensemble_smocke/
│   │       └── _archive/
│   │
│   ├── LARP_MEDIEVAL/
│   │   ├── LARP_MEDIEVAL.md
│   │   └── annonces/
│   │       ├── 01_tapis_chevalier/
│   │       └── _archive/
│   │
│   ├── STYLE_STOCKHOLM/
│   │   ├── STYLE_STOCKHOLM.md
│   │   └── annonces/                       ← Vide (pas encore de production)
│   │
│   └── VINTAGE_RETRO/
│       ├── VINTAGE_RETRO.md
│       └── annonces/                       ← Vide (pas encore de production)
│
├── 🏆 PRODUITS_GAGNANTS/ (articles ayant vendu ≥ 1 fois)
│   ├── README.md                   ← Liste et statut de tous les gagnants
│   ├── _template/
│   │   └── FICHE_PRODUIT.md        ← Template pour nouveaux gagnants
│   └── [NOM_PRODUIT]/              ← 1 dossier par produit gagnant
│       ├── FICHE_PRODUIT.md        ← Original + historique ventes
│       ├── VARIANTES.md            ← Variantes couleurs à lancer
│       └── annonces/
│           └── [couleur]/
│               ├── ANNONCE.docx
│               └── images/
│
├── 📊 RAPPORTS
│   ├── PRODUCTION_RAPPORT.md       ← Mis à jour à chaque run production
│   ├── SOURCING_RAPPORT.md         ← Historique des runs sourcing
│   └── PRODUCTION_STATE.md         ← État actuel du stock
│
├── 🖼️ gemini_photo.py              ← Script génération images (Gemini 2.5 Flash)
│
├── 📚 _archive/                    ← Anciens fichiers système (jamais supprimés)
│   ├── annonces_ancien_format_18mars/ ← Ancien format annonces/ flat (migré)
│   ├── CADRE_BUSINESS.md           ← Anciennes versions
│   ├── leonardo_photo.py           ← Ancien script images (abandonné)
│   └── [anciens fichiers]...
│
└── 📜 HISTORIQUE
    ├── SESSION_M22_17mars2026.md
    ├── PREP_SESSION_M22.md
    └── MIGGY_PROMPT_VINTED.md
```

---

## RÈGLES ABSOLUES (MÉMORISÉES)

```
┌────────────────────────────────────────────────────────────────┐
│                    RÈGLES INVIOLABLES                          │
│                                                                │
│  🔴 ON NE SUPPRIME JAMAIS RIEN                                │
│     └── Tout → _archive/ (annonces, images, fichiers)         │
│                                                                │
│  🔴 MARGE MINIMUM 40€ PAR ARTICLE                             │
│     └── Sinon → bundle ou accessoire uniquement                │
│                                                                │
│  🔴 TOP 5 LANCEMENT = 5 CATÉGORIES DIFFÉRENTES                │
│     └── Variantes = APRÈS première vente seulement             │
│                                                                │
│  🔴 IMAGES FIDÈLES AU PRODUIT RÉEL                             │
│     └── Jamais inventer ceinture, accessoire, détail absent    │
│                                                                │
│  🔴 PHOTOS STYLE AMATEUR                                       │
│     └── Pas trop pro (surtout déco/LARP)                       │
│                                                                │
│  🔴 VÉRIFIER LIENS + ENVOYER À YANIS                          │
│     └── Chaque fin de sourcing → tableau liens + statut        │
│     └── Yanis double-check AVANT toute commande                │
│                                                                │
│  🔴 FILTRE ÉTHIQUE / ISLAMIQUE                                 │
│     └── Pas de tenues suggestives/transparentes                │
│     └── Pas de symboles occultistes                            │
│     └── Jamais écrire "sorcière"                               │
│                                                                │
│  🔴 1 COMPTE = 1 NICHE = 1 PERSONA                            │
│     └── Jamais mélanger les styles sur un même compte          │
│                                                                │
│  🔴 ANNONCES EN .docx (PAS seulement .md)                     │
│     └── Format copier-coller direct pour Vinted                │
└────────────────────────────────────────────────────────────────┘
```

---

## LIAISON ENTRE LES 2 AGENTS

```
                    ┌──────────────────┐
                    │    YANIS          │
                    │  "Je veux 2       │
                    │   nouveaux        │
                    │   articles pour   │
                    │   Western"        │
                    └────────┬─────────┘
                             │
                             ▼
              ┌──────────────────────────┐
              │  🔍 AGENT SOURCING (V2)  │
              │                          │
              │  Input:                  │
              │  ├── personas/           │
              │  │   WESTERN_CHIC.md     │
              │  └── CADRE_BUSINESS.md   │
              │                          │
              │  Process:                │
              │  ├── WebSearch AliExpress │
              │  ├── Vérifie liens       │
              │  ├── Calcule marges      │
              │  └── Compare fournisseurs│
              │                          │
              │  Output:                 │
              │  ├── personas/ mis à jour│
              │  └── Tableau liens       │
              │      pour Yanis          │
              └────────┬─────────────────┘
                       │
                       ▼
              ┌──────────────────────────┐
              │  ✅ YANIS VALIDE         │
              │                          │
              │  "OK, les liens marchent,│
              │   lance la production"   │
              └────────┬─────────────────┘
                       │
                       ▼
              ┌──────────────────────────┐
              │  🏭 AGENT PRODUCTION (V4)│
              │                          │
              │  Input:                  │
              │  ├── personas/           │
              │  │   (produits validés)  │
              │  ├── CADRE_BUSINESS.md   │
              │  └── CYCLE_3_JOURS.md    │
              │                          │
              │  Process:                │
              │  ├── Crée dossier annonce│
              │  ├── Génère ANNONCE.docx │
              │  ├── Génère 3 images     │
              │  │   (gemini_photo.py)   │
              │  └── FICHE_COMPLETE.md   │
              │                          │
              │  Output:                 │
              │  ├── annonces/NN_xxx/    │
              │  └── PRODUCTION_RAPPORT  │
              └────────┬─────────────────┘
                       │
                       ▼
              ┌──────────────────────────┐
              │  📱 YANIS PUBLIE         │
              │                          │
              │  1. Copie ANNONCE.docx   │
              │  2. Upload images        │
              │  3. Publie sur Vinted    │
              │  4. Relance favoris J+3  │
              └────────┬─────────────────┘
                       │
                       ▼
              ┌──────────────────────────┐
              │  📊 REVIEW J+3           │
              │                          │
              │  Yanis déclare :         │
              │  "Article X vendu,       │
              │   Article Y pas vendu"   │
              └────────┬────────┬────────┘
                       │        │
            ┌──────────┘        └──────────┐
            ▼                              ▼
  ┌───────────────────┐      ┌───────────────────────┐
  │ ❌ PAS VENDU      │      │ ✅ VENDU (GAGNANT)     │
  │                   │      │                        │
  │ annonces/         │      │ PRODUITS_GAGNANTS/     │
  │  _archive/        │      │  [produit]/            │
  │   [date]/         │      │   FICHE_PRODUIT.md     │
  │    [dossier]      │      │   VARIANTES.md         │
  │                   │      │                        │
  │ Dossier complet   │      │ + Comparaison prix     │
  │ préservé          │      │   multi-plateforme     │
  │ Jamais supprimé   │      │                        │
  └───────────────────┘      │ + 2-3 variantes        │
                             │   couleurs sourcées    │
                             │                        │
                             │ + Annonces .docx       │
                             │   + images générées    │
                             │   pour chaque variante │
                             └────────────────────────┘
                                        │
                                        ▼
                             ┌────────────────────────┐
                             │ CYCLE SUIVANT           │
                             │                         │
                             │ 5 annonces = mix de :   │
                             │ ├── Variantes gagnants  │
                             │ └── Nouveaux articles   │
                             │                         │
                             │ Ratio évolue →          │
                             │ converge vers 100%      │
                             │ variantes gagnantes     │
                             └────────────────────────┘
```

---

## CAS SPÉCIFIQUES

### Image ratée / rejetée
```
annonces/NN_produit/images/image_ratee.jpg
        └──▶ annonces/NN_produit/images/_archive/image_ratee.jpg
        + Relancer gemini_photo.py pour régénérer
```

### Annonce remplacée par variante
```
annonces/NN_produit/  (ancien)
        └──▶ annonces/_archive/NN_produit/  (archivé)
```

### Quota Gemini épuisé (erreur 429)
```
→ Vérifier billing sur console.cloud.google.com
→ Projet = celui qui possède la clé API (ligne 49 de gemini_photo.py)
→ Modèle = gemini-2.5-flash-image
```

### Produit marge < 40€
```
→ Ne PAS vendre seul
→ Utiliser en BUNDLE avec un produit principal
→ Marquer "Accessoire bundle" dans le statut persona
```

### Lien AliExpress mort / indisponible
```
→ Marquer ❌ dans le persona
→ Chercher un produit de remplacement (même catégorie)
→ NE PAS produire d'annonce tant que le lien n'est pas confirmé par Yanis
```

---

## COMPTES ACTIFS + PERSONAS

```
┌──────────────────────────────────────────────────────────┐
│  COMPTES VINTED ACTIFS                                   │
│                                                          │
│  Compte 1 → Romantique Victorienne  🟡 En cours         │
│  Compte 2 → Western Chic            🟡 En cours         │
│  Compte 3 → Grande Taille Cottagecore 🟡 En cours       │
│  Compte 4 → LARP Médiéval           🟡 En cours         │
│                                                          │
│  PERSONAS EN PRÉPARATION (pas encore de compte)          │
│  ├── Style Stockholm          (15 produits, URLs à      │
│  │                             sourcer en liens directs) │
│  └── Vintage Rétro            (2 produits sourcés)       │
│                                                          │
│  STOCK ACTUEL                                            │
│  ├── 5 annonces prêtes (docx + images)                  │
│  ├── 1 produit gagnant (manteau bordeaux)                │
│  └── Objectif : 120 annonces d'avance (6 jours)         │
└──────────────────────────────────────────────────────────┘
```

---

## CHECKLIST VÉRIFICATION LIENS (NOUVEAU)

À chaque fin de run sourcing, l'agent DOIT produire ce tableau :

| # | Produit | Lien AliExpress | Statut lien | Note★ | Avis | Vendus | Action Yanis |
|---|---------|-----------------|-------------|-------|------|--------|-------------|
| 1 | ... | [lien cliquable] | ✅ Accessible / ⚠️ Non vérifiable / ❌ Mort | ... | ... | ... | Vérifier / Commander / Remplacer |

**Yanis ouvre CHAQUE lien et confirme AVANT que l'agent production ne crée les annonces.**

---

*Ce fichier est la référence globale du système. À relire en début de chaque session.*
