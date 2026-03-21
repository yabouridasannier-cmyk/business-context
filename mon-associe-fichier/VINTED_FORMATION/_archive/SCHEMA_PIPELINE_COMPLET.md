# PIPELINE VINTED — SCHÉMA COMPLET + ÉTAT DES TUYAUX

> Dernière MAJ : 14 mars 2026

---

## LE CIRCUIT COMPLET

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  ÉTAPE 1 — AGENT SOURCING (programmé)                              │
│  ┌─────────────────────────────────────┐                           │
│  │ • Lit SOURCING_CONFIG.md            │                           │
│  │ • Analyse niches (mode 1)           │                           │
│  │ • Recherche produits (mode 2)       │                           │
│  │ • Écrit → SOURCING_RESULTATS.md     │                           │
│  └──────────────┬──────────────────────┘                           │
│                 │                                                    │
│                 ▼ (fichier partagé)                                  │
│                                                                     │
│  ÉTAPE 2 — AGENT PRODUCTION (programmé)                            │
│  ┌─────────────────────────────────────┐                           │
│  │ • Lit SOURCING_RESULTATS.md         │                           │
│  │ • Pour chaque produit :             │                           │
│  │   → Génère photos via Gemini API    │                           │
│  │   → Génère description Vinted       │                           │
│  │   → Assemble fiche complète         │                           │
│  │ • Écrit → PRODUCTION_ANNONCES.md    │                           │
│  │ • Photos → /images/                 │                           │
│  └──────────────┬──────────────────────┘                           │
│                 │                                                    │
│                 ▼ (fichier partagé + images)                        │
│                                                                     │
│  ÉTAPE 3 — PUBLICATION (Claude in Chrome)                          │
│  ┌─────────────────────────────────────┐                           │
│  │ • Lit PRODUCTION_ANNONCES.md        │                           │
│  │ • Ouvre Vinted sur Chrome normal     │                           │
│  │ • Pour chaque annonce :             │                           │
│  │   → Upload photos                   │                           │
│  │   → Remplit titre, description,     │                           │
│  │     prix, taille, état, catégorie   │                           │
│  │   → Publie                          │                           │
│  │   → Attend 3-5 min (rythme humain) │                           │
│  │ • Log → PUBLICATION_LOG.md          │                           │
│  └─────────────────────────────────────┘                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ÉTAT DE CHAQUE TUYAU — CE QUI MARCHE vs CE QUI MANQUE

### TUYAU 1 : SOURCING → RESULTATS

| Élément | État | Détail |
|---------|------|--------|
| Agent sourcing créé | ✅ OK | Tâche programmée existante |
| SOURCING_CONFIG.md | ✅ OK | Config avec niches + paramètres |
| Mode ANALYSE_NICHES | ✅ OK | Premier run fait — top 10 scoré |
| SOURCING_RESULTATS.md | ✅ OK | 10 niches, 50 produits listés |
| Mode RECHERCHE_PRODUITS | ⚠️ PAS TESTÉ | Existe mais jamais lancé — à tester après choix niche |
| Liens AliExpress concrets | ❌ MANQUE | Les résultats ont des fourchettes de prix mais PAS de liens produits AliExpress réels |

**Action requise :** Lancer l'agent sourcing en mode RECHERCHE_PRODUITS sur la niche choisie (Coquette) pour obtenir des liens AliExpress concrets avec prix réels.

---

### TUYAU 2 : RESULTATS → PHOTOS + DESCRIPTIONS

| Élément | État | Détail |
|---------|------|--------|
| Agent production créé | ✅ OK | Tâche programmée existante |
| Script gemini_photo.py | ✅ OK | Script Python prêt, 3 modes (single/référence/batch) |
| google-genai installé | ✅ OK | Installé dans cette session |
| Clé API Gemini | ❌ MANQUE | Yanis doit la créer sur aistudio.google.com/apikey |
| Test génération photo | ❌ MANQUE | Impossible sans la clé API |
| Prompts photo optimisés | ⚠️ BASIQUES | Prompts par défaut dans le script — Yanis a des prompts M22 meilleurs à intégrer |
| TOOL_DESCRIPTIONS_VINTED.md | ✅ OK | Templates descriptions par type de produit |
| PRODUCTION_ANNONCES.md | ❌ N'EXISTE PAS | Sera créé par l'agent production quand il tournera |
| Agent sait appeler gemini_photo.py | ❌ PAS CONFIGURÉ | L'agent production doit être mis à jour pour appeler le script Python avec la clé API |

**Actions requises :**
1. Yanis crée la clé API Gemini et me la donne
2. On teste 1 photo pour valider
3. On met à jour l'agent production pour qu'il appelle gemini_photo.py
4. Yanis partage ses prompts M22 (si meilleurs que les basiques)

---

### TUYAU 3 : ANNONCES → VINTED (publication)

| Élément | État | Détail |
|---------|------|--------|
| Claude in Chrome | ✅ INSTALLÉ | Fonctionne sur Chrome normal |
| Compte Vinted | 🔄 EN COURS | Yanis le crée maintenant |
| PROCESS_PUBLICATION_CHROME.md | ✅ OK | Workflow étape par étape documenté |
| Capacité upload photos | ❓ PAS TESTÉ | Claude in Chrome peut-il uploader des images sur Vinted ? À tester |
| Rythme humain (3-5 min) | ✅ DOCUMENTÉ | Règle anti-détection en place |
| PUBLICATION_LOG.md | ❌ N'EXISTE PAS | Sera créé au premier post |
| Test publication réelle | ❌ PAS FAIT | Premier test quand compte + annonces prêts |

**Actions requises :**
1. Yanis finit de créer le compte Vinted
2. On teste Claude in Chrome → poster 1 annonce manuelle
3. On valide que l'upload photo fonctionne
4. On documente les sélecteurs Vinted (catégories, tailles, etc.)

---

## RÉSUMÉ — LISTE COMPLÈTE DE CE QUI MANQUE

### Bloquants (sans ça, rien ne tourne)

| # | Quoi | Qui | Temps estimé |
|---|------|-----|-------------|
| 1 | **Clé API Gemini** | Yanis | 2 min |
| 2 | **Compte Vinted créé** | Yanis | 5 min |
| 3 | **Test 1 photo Gemini** | Miggy (dès qu'on a la clé) | 2 min |
| 4 | **Test 1 publication Vinted via Claude in Chrome** | Miggy + Yanis | 10 min |

### Importants (pipeline fonctionne sans, mais en mode dégradé)

| # | Quoi | Qui | Temps estimé |
|---|------|-----|-------------|
| 5 | Configurer agent production pour appeler gemini_photo.py | Miggy | 15 min |
| 6 | Lancer agent sourcing mode RECHERCHE_PRODUITS (niche Coquette) | Agent sourcing | 10 min |
| 7 | Intégrer prompts M22 si meilleurs | Yanis fournit → Miggy intègre | 5 min |
| 8 | Tester upload photo via Claude in Chrome | Miggy | 10 min |

### Nice to have (optimisation après validation)

| # | Quoi | Qui |
|---|------|-----|
| 9 | Liens AliExpress réels par produit | Agent sourcing |
| 10 | PUBLICATION_LOG.md auto-généré | Agent publication |
| 11 | Scheduler daily pour agents | Miggy |
| 12 | Multi-comptes Chrome normal | Après premières ventes |

---

## NICHE PREMIER COMPTE : COQUETTE AESTHETIC

Déjà décidé par l'analyse sourcing (score 89/100).

**5 premiers produits à poster :**

| Produit | Prix achat estimé | Prix vente Vinted | Marge |
|---------|-------------------|-------------------|-------|
| Chemise dentelle puff sleeves | 4-6€ | 28-35€ | ~480% |
| Jupe plissée satin | 5-8€ | 30-40€ | ~450% |
| Crop top puff sleeves | 3-5€ | 22-30€ | ~520% |
| Cardigan pastel léger | 6-8€ | 32-42€ | ~425% |
| Ruban/bow clips | 1-2€ | 10-15€ | ~650% |

> Ces produits seront affinés avec des liens AliExpress réels quand l'agent sourcing tournera en mode RECHERCHE_PRODUITS.

---

## ORDRE DES OPÉRATIONS CE SOIR

```
Yanis maintenant :
  ├── Créer compte Vinted (Chrome normal) ← EN COURS
  └── Créer clé API Gemini (aistudio.google.com/apikey)

Dès que clé API reçue :
  ├── Test photo Gemini (Miggy)
  └── Config agent production (Miggy)

Dès que compte Vinted OK :
  ├── Test publication Claude in Chrome (Miggy + Yanis)
  └── Si OK → lancer agent sourcing RECHERCHE_PRODUITS

Demain :
  └── Premières vraies annonces (5-10 produits Coquette)
```
