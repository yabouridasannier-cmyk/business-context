# ROADMAP — Industrialisation de l'algorithme de qualification
> Créé le 25 février 2026 — Yanis / Projet Lyon Prospects

---

## 1. PROBLÈME DU CHAT — EXPLICATION

**Ce que tu observes** (texte qui disparaît, réponses qui réapparaissent) n'est pas un bug. C'est la **compaction de contexte** de Claude Code.

**Mécanisme** : quand une conversation dépasse ~90-100k tokens, Claude Code crée automatiquement un résumé condensé et repart sur ce résumé. Pendant cette transition, l'interface peut afficher brièvement l'ancien texte puis le nouveau. C'est normal, pas une perte de données.

**Solutions pratiques** :
- Pour les runs longs (`session 30`), démarrer un **nouveau chat** plutôt que de continuer un ancien — tu maximises le budget de tokens disponibles pour le travail réel
- Le CLAUDE.md + Supabase + le skill sont ta **mémoire persistante** — chaque nouveau chat repart avec le contexte complet
- Cowork = PC doit rester allumé, mais le contexte lui survit via les fichiers

---

## 2. ÉTAT ACTUEL — CE QUI EXISTE (V1)

### Architecture
```
Toi (Yanis) → tape "session 5" dans Cowork
      ↓
Claude lit CLAUDE.md + CALIBRATION_LOG.md + SKILL.md
      ↓
Claude recherche des prospects (Google, pappers, GMaps)
      ↓
4 gates binaires → scoring V3 (100 pts)
      ↓
Résultats écrits dans Supabase (anti-doublons automatiques)
      ↓
Synthèse en mode éco → CRM (structur-a-lead.vercel.app)
```

### Ce qui fonctionne
- ✅ Grille V3 calibrée (3 sessions + coach AGS)
- ✅ Supabase avec 13 prospects historisés
- ✅ Anti-doublons 3 niveaux (URL, SIRET, fuzzy name)
- ✅ CRM Kanban opérationnel
- ✅ CALIBRATION_LOG.md — mémoire des corrections coach

### Limites actuelles
- ❌ Runs manuels (tu dois taper la commande)
- ❌ PC doit être allumé + Cowork ouvert
- ❌ ~1 prospect/2 min → 30 prospects = ~60-90 min
- ❌ Pas d'interface partageable avec le coach / les membres AGS

---

## 3. COMMENT UTILISER CLAUDE AU MAXIMUM — CONSEILS PRATIQUES

### 3.1 — Commandes à maîtriser

| Commande | Résultat | Durée estimée |
|---|---|---|
| `session 3` | 3 qualifiés, calibration rapide | 20-30 min |
| `session 10` | 10 qualifiés, run standard | 60-90 min |
| `session 30` | 30 qualifiés, run complet | 2h30-3h |
| `session 30 mode éco` | 30 qualifiés, pas de DOCX | 1h30-2h |

**Règle** : toujours démarrer un **nouveau chat** pour les sessions longues.

### 3.2 — Maximiser la qualité des résultats

- **Feedback immédiat** : après chaque run, donner les corrections dans le même chat → Claude met à jour CALIBRATION_LOG.md et SKILL.md en live
- **Cas de référence** : les 5 qualifiés en base + les 7 disqualifiés sont les "exemples d'entraînement" — plus tu en as, plus Claude calibre juste
- **Zones** : respecter la séquence dans STRATEGY_V1.md (Part-Dieu en premier, densité entreprises maximale)

### 3.3 — Gestion des tokens (plan Pro vs Max)

| Usage | Tokens/run | Runs/mois pour mission AGS | Plan recommandé |
|---|---|---|---|
| `session 5` | ~15-20k | 3 runs = 15 qualifiés | Pro (20€) suffisant |
| `session 10` | ~30-40k | 2 runs = 20 qualifiés | Pro suffisant |
| `session 30` | ~80-130k | 1-2 runs/semaine | Max (~80€) conseillé |
| Shortcut auto 5j/7 | ~80k × 20 = 1.6M/mois | — | Max obligatoire |

---

## 4. ÉTAPE SUIVANTE — SHORTCUT PLANIFIÉ (V1.5)

### Objectif
Run automatique **lundi → vendredi, 8h00**, sans que tu aies à taper quoi que ce soit.

### Prérequis
- PC allumé et Cowork ouvert à 8h00
- Plan Max Claude (sinon le shortcut rate la limite tokens)

### Création du shortcut
Dans Cowork, taper : `crée un shortcut planifié qui lance "session 10" tous les matins lun-ven à 8h00`

### Ce que le shortcut fait
1. Lit Supabase → identifie la zone suivante non couverte
2. Qualifie 10 prospects
3. Écrit dans Supabase (anti-doublons)
4. Ajoute les qualifiés dans le CRM
5. Envoie un email récap à yabouridasannier@gmail.com

### Résultat
- 10 qualifiés/jour × 5 jours = **50 prospects/semaine**
- Zone Lyon complète (59 communes) couverte en **3-4 semaines**
- Coût : ~Max (80€/mois) + temps zéro de ta part

---

## 5. V2 — EXTERNALISATION SUR SERVEUR (Claude Code + API)

### Problème V1.5 résolu : plus besoin du PC allumé

### Architecture V2
```
Serveur (VPS 5-10€/mois)
      ↓
Claude Code CLI (cron job, 8h00 lun-ven)
      ↓
Script de qualification (Node.js ou Python)
  → Appel API Anthropic (claude-sonnet-4-5)
  → Recherche web (Serper API ou Brave Search API)
  → Lecture/écriture Supabase
  → Notification email (Resend ou Mailgun)
      ↓
CRM mis à jour automatiquement
```

### Coût mensuel V2 estimé
| Composant | Coût |
|---|---|
| VPS (Hetzner ou OVH) | 4-6€/mois |
| API Claude (Sonnet 4.5, 10 runs × 30 prospects) | ~8-12€/mois |
| API recherche web (Serper) | 5-10€/mois |
| Supabase (Free tier suffisant) | 0€ |
| **Total** | **~20-30€/mois** |

vs. Plan Max Cowork = 80€/mois → **économie de 50-60€/mois**

### Comment externaliser le "cerveau" (le playbook)
Le playbook est dans SKILL.md. Pour l'API, il devient le **system prompt** :
```
SYSTEM PROMPT = contenu complet de SKILL.md
USER MESSAGE = "Analyse ce prospect : [données scrappées]"
RÉPONSE = verdict JSON {gate_0, gate_1, ..., score, final_status, notes}
```

C'est le même algorithme, juste livré via l'API plutôt que via Cowork.

---

## 6. V3 — SAAS MULTI-UTILISATEURS (potentiel AGS)

### Vision
Une application web où **chaque membre d'AGS** (30+ personnes) a son propre compte, sa propre zone géographique, son propre CRM — alimenté par le même moteur de qualification.

### Architecture V3
```
Interface web (Next.js)
  ├── Dashboard prospects (par utilisateur)
  ├── CRM léger intégré
  ├── Statistiques de zone
  └── Export CSV/PDF des fiches

      ↓

API backend (Node.js ou Python FastAPI)
  ├── /qualify — lance un run pour un user
  ├── /prospects — liste les prospects d'un user
  └── /admin — dashboard AGS global

      ↓

Moteur de qualification (Claude API)
  ├── System prompt = SKILL.md (partagé entre tous)
  ├── Personnalisable par zone/secteur par user
  └── Résultats stockés par user_id dans Supabase

      ↓

Supabase (multi-tenant)
  ├── users (user_id, zone, plan)
  ├── prospects (user_id, données)
  └── sessions (user_id, stats)
```

### Modèle économique
| Tier | Prix | Inclus |
|---|---|---|
| Solo (Yanis) | 0€ | Usage interne |
| Membre AGS | 150€/mois | 10 runs/mois, 1 zone, CRM |
| Pro | 250€/mois | Runs illimités, multi-zones |
| Agence | 500€/mois | 5 users, toutes zones France |

**Potentiel immédiat** : 30 membres AGS × 150€ = **4 500€/mois**
**Coût de service** : ~300-500€/mois (API Claude + infra) = **marge ~90%**

---

## 7. ORDRE D'EXÉCUTION — CE QU'IL FAUT FAIRE ET DANS QUEL ORDRE

```
MAINTENANT (cette semaine)
├── Finir la mission coach AGS : 15 qualifiés validés
├── Sessions d'entraînement : affiner calibration V3
└── Commencer à collecter des cas référence (50+ en base = bon étalon)

COURT TERME (2-4 semaines)
├── Créer le shortcut planifié (V1.5)
├── Valider la qualité sur 3-4 runs automatiques
└── Upgrade plan Max si runs quotidiens lancés

MOYEN TERME (1-3 mois)
├── Externaliser sur serveur (V2)
│   → Libère le PC, réduit les coûts
│   → Claude Code CLI + cron + API Anthropic
├── Construire l'interface web minimale (dashboard prospects)
└── Tester avec 2-3 membres AGS en beta

LONG TERME (3-6 mois)
├── SaaS complet (V3)
├── Onboarding membres AGS
├── Extension géographique (autres villes)
└── Personnalisation par secteur/zone
```

---

## 8. COMMENT PACKAGER L'ALGORITHME POUR LE VENDRE

### Ce que tu as construit (la vraie valeur)

Ce n'est pas juste un script — c'est un **playbook de qualification entraîné** :

1. **Les règles** (SKILL.md) = le "cerveau" — 4 gates + scoring + anti-hallucination
2. **Les cas de référence** (Supabase) = les "données d'entraînement"
3. **CALIBRATION_LOG.md** = l'historique des corrections = la "mémoire du modèle"
4. **Le CRM** = l'interface de travail

### Ce qui rend l'algorithme exportable

Pour un membre AGS à Bordeaux ou Marseille, tu changes **uniquement** :
- La zone géographique (paramètre dans la commande)
- Le playbook reste identique

Pour un secteur spécifique (ex : uniquement restaurants), tu ajoutes :
- Un filtre Gate 0 sectoriel (paramètre)
- Des cas référence du secteur

### Formats de livraison possibles

| Format | Effort | Prix potentiel |
|---|---|---|
| **Accès SaaS** (V3 ci-dessus) | Élevé | 150-500€/mois récurrent |
| **Plugin Cowork** | Moyen | 50-100€/mois par user |
| **Prompt pack + guide** | Faible | 200-500€ une fois |
| **Formation + setup** | Faible | 500-1000€ par membre |

**Recommandation court terme** : commencer par **plugin Cowork** (tu peux le créer toi-même dans Cowork) → livré à chaque membre AGS avec leur config zone → 50€/mois × 30 membres = 1 500€/mois récurrent sans développement lourd.

---

## 9. RÉSUMÉ — LES 3 PROCHAINES ACTIONS

1. **Finir mission AGS** : lancer `session 5` × 3 runs pour avoir 15 qualifiés validés coach
2. **Créer le shortcut** : une fois les 15 qualifiés livrés, créer le shortcut planifié (30 min de setup)
3. **Proposer à Valentin** : un plugin Cowork "clé en main" pour les membres AGS — package = plugin + guide + 1h d'onboarding

---
*Généré le 25/02/2026 — à mettre à jour après chaque milestone*
