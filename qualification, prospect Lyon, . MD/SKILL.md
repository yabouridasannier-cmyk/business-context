# SKILL.md — Qualification Prospects Lyon V5.3
> Version : V5.3 — 09/03/2026 · R33 session X = X callable (06/07) · R31 CRM=06/07 only · Colonnes contact structurées · Pas de double vérif
> Lire AVANT chaque run. Process Swarm et injection CRM = dans STRATEGY_V1.md (pas ici).

---

## OBJECTIF
Identifier des PME locales (Lyon + 59 communes, ~30 km) avec un site médiocre/absent ET CA ≥ 70k€ ET signaux de croissance. Cible idéale = fort standing + site qui ne lui rend pas justice.

---

## PRÉ-FILTRE (avant Gates — ordre strict)

### Étape 0 — Téléphone (R28v2) 📞 NON BLOQUANT
Chercher un numéro dans les sources habituelles (Google Maps, Pages Jaunes, site, societe.com, pappers, LinkedIn).
- **06/07 ou ligne directe** = HAUTE VALEUR → noter dans BLOC 1
- **01/02/03/04/05/09** = standard/secrétariat = INUTILE (redirige vers mail/LinkedIn) → ne PAS noter comme téléphone utile
- **Aucun 06/07 trouvé** → canal de contact = LinkedIn + email. Le prospect reste qualifiable, injection CRM possible sans tél.

### Étape 1 — Site internet (R5/R5b)
- **Pas de site** → EXCLU sauf **métiers d'appel** (R5b) : garages, plombiers, serruriers, électriciens, couvreurs, maçons, climaticiens, dératiseurs, artisans BTP → GARDER, angle "Création site"
- **Site 404** → Métier d'appel = prospect en or (GARDER). Autre = EXCLU si preuve abandon prolongé (R6)
- **Site existant** → Étape 2

### Étape 2 — Visite WebFetch obligatoire (R7)
Visiter le site via WebFetch. Évaluer visuel + fonctionnel.

**Échelle visuelle 1-5 :**
1 = très moche/vieillot · 2 = moche/amateur · 3 = passable/neutre · 4 = bien/moderne · 5 = très bien/soigné

→ Cibles : **1-2**. Note 3 = Gate 3 tranche. **Note 4-5 = EXCLU (R4).**

**Copyright pied de page :** ©2025-2026 = refait récemment → EXCLU (R11). Exception : ©2026 mais tellement moche que l'écart est flagrant → GARDER.
©2022 et avant = bon signal.

### Niches exclues
Boulangeries, coiffeurs, cafés/bars, petits commerces (tabac, kebabs, snacks). Exception : multi-sites ou CA > 300k€ confirmé.

---

## RÈGLES CLÉS (R8-R15)

| Règle | Résumé |
|-------|--------|
| R8 | "Design" seul ≠ axe valide. Vrais axes = 404, non responsive, CTA cassé, site ≤2/5 |
| R9 | Site ≥ 3/5 → preuves techniques obligatoires (404, CTA absent, non responsive) sinon STOP |
| R10 | CTA absent/défaillant = axe majeur (peut sauver un prospect même site 4/5) |
| R11 | ©2025-2026 = STOP. Exception : ©2026 mais très moche = GARDER |
| R12 | Vérifier activité réelle sur le site, pas juste Google/Pappers |
| R13 | Réalisations, certifications, SEO seuls ≠ axes. Complément uniquement |
| R14 | Tester URLs avant insertion Supabase |
| R15 | Temps chargement > 3s = levier commercial majeur ("70% partent après 3s") |
| R18 | Sans site + aucune preuve croissance = DISQUALIFIÉ ; avec preuves = GARDER |
| R25 | Accroche = obligatoire dans CRM (bloc 3) |
| R27 | Arguments factuels > critiques design ("on ne critique pas le design" — coach) |
| R28v2 | Seuls 06/07 comptent. Standard (01-05/09) = inutile. Sans 06/07 → canal LinkedIn/email (non bloquant) |
| R31 | **CRM = UNIQUEMENT si 06/07 dirigeant.** Tous les qualifiés → Supabase (colonnes structurées). Sans 06/07 → Supabase only, machine secrétariat récupère. |
| R32 | **PAS de double vérification séparée.** La machine qualifie → Supabase/CRM. Yanis vérifie au moment du GK2 (30s/prospect), pas avant. |
| R33 | **`session X` = X prospects CALLABLE (06/07 dirigeant).** La machine ne s'arrête pas tant que le quota callable n'est pas atteint. Qualifiés sans 06/07 → Supabase only, ne comptent pas dans le quota. |

---

## 10 AXES D'AMÉLIORATION PRIORITAIRES
1. Temps chargement > 3s (R15)
2. CTA absent (R10)
3. CTA défaillant (bouton cassé, formulaire daté)
4. Erreurs 404 internes
5. Design très daté ≤ 2/5
6. Pages internes cassées (liens morts, sections vides)
7. Non responsive mobile
8. Copyright ancien (≤ 2022)
9. Gmail comme email pro
10. Zéro copywriting

⚠️ NE SONT PAS des axes seuls : design subjectif (R8), réalisations, certifications, SEO (R13).

---

## 4 GATES BINAIRES (ordre strict — 1er échec = STOP)

**Gate 0 — Clientèle** : B2C local = PASS. B2B avec image + taille = PASS. B2B pur opaque = STOP.

**Gate 1 — Secteurs exclus** : alcool, porc, drogues, adulte = STOP.

**Gate 2 — CA ≥ 70k€** : Binaire. Jamais dans le scoring. CA confidentiel → signaux indirects, sinon STOP.

**Gate 3 — ≥ 3 axes flagrants** : Minimum 3 axes distincts. 2 très graves peut valoir 3 moyens. < 3 axes = STOP.

---

## SCORING V4 — 100 POINTS (si pré-filtre + 4 gates passés)

| Dimension | Pts | Ce qu'on mesure |
|-----------|-----|-----------------|
| **Écart Site/Standing** | 0-50 | Écart entre qualité site et standing réel. 40-50=catastrophique, 28-39=fort, 15-27=moyen, 0-14=faible |
| **Besoins digitaux** | 0-25 | SEO inexistant (0-10), Ads absent (0-8), réseaux absents (0-4), GMB mal config (0-3) |
| **Croissance** | 0-15 | CA croissant (0-5), employés↑ (0-4), ancienneté stable (0-3), ambition (0-3) |
| **Contactabilité** | 0-10 | Dirigeant trouvable (0-4), LinkedIn trouvé (0-3), tél 06/07 direct (0-3) |

**Verdict :** ≥ 70 = QUALIFIÉ · 55-69 = INCERTAIN · < 55 = NON QUALIFIÉ

---

## DESTINATION DES QUALIFIÉS (R31 — V5.2)

**Tous les qualifiés → Supabase** (colonnes structurées, TOUJOURS).
**CRM → UNIQUEMENT si `phone_mobile` = 06/07 du dirigeant identifié.**
Sans 06/07 → Supabase only. La machine secrétariat piochera dans Supabase pour enrichir les contacts.

### Colonnes Supabase contact (V5.2 — structurées, plus de vrac)
| Colonne | Contenu |
|---------|---------|
| `contact_name` | Nom complet dirigeant (prénom + nom) |
| `phone_mobile` | 06/07 dirigeant — SEUL critère injection CRM |
| `phone_main` | Standard fixe — NON utilisé pour qualification |
| `linkedin_url` | URL LinkedIn dirigeant |
| `email` | Email pro dirigeant |
| `accroche` | Template utilisée (A/B/C/D/E) |
| `axes_amelioration` | Axes factuels numérotés (stockés proprement) |

### FORMAT CRM — 4 BLOCS (si injection CRM = 06/07 trouvé)

**BLOC 1 — 📞 CONTACT** : Dirigeant (prénom+nom) + Tél 06/07 + LinkedIn/Email
**BLOC 2 — 🎯 ANGLES + AXES** : Angle (Refonte/Création site/Multi/Image de Marque/SEO) + Axes majeurs numérotés (factuels, pas design subjectif)
**BLOC 3 — 📣 ACCROCHE** : Phrase concrète que Yanis dit au téléphone (template A-E ci-dessous)
**BLOC 4 — 🔗 IMPLICATION** : Concurrent mieux positionné / Nom dirigeant / Fait marquant
**Secondaires** : CA + SIRET, LinkedIn dirigeant, résumé court

⚠️ JAMAIS d'injection CRM sans 06/07 dirigeant (R31). Sans 06/07 = Supabase only.

### Templates accroches (R26)
**A — Site récent mais très moche (exception R11)** : « Vos concurrents [X] et [Y] récupèrent vos clients. Votre site manque de structuration et de CTA — ça change tout pour la conversion. »
**B — Sans site, métier d'appel (R5b)** : « Vous êtes [MÉTIER] sans site. Vos concurrents sur Google récupèrent les clients que vous ne voyez pas. Un site bien fait = [X] appels en plus/mois. »
**C — Site ancien + gros CA** : « Vous faites [CA]€ depuis [ANNÉE], mais votre site [PROBLÈME FACTUEL]. L'écart entre votre envergure et votre présence web est énorme. »
**D — Erreur technique flagrante** : « Votre site a [ERREUR : SSL/404/non responsive/formulaire cassé]. Les clients qui essaient de vous contacter partent chez le concurrent. »
**E — Template générique/daté** : « Votre site utilise un template de [ANNÉE] — même design que des centaines d'autres. Après [X] ans d'activité, vous méritez un site qui vous ressemble. »

---

## ANTI-HALLUCINATION (ABSOLU)
Chaque info étiquetée : **Confirmé** (source officielle) · **Probable** (signaux indirects convergents) · **Déduit** (logique mais non vérifiable — TOUJOURS explicité)

## SOURCES (ordre de priorité)
Site officiel (WebFetch) → Google Maps → pappers.fr/societe.com → réseaux sociaux → Meta Ads Library → Pages Jaunes

---

## 25 NICHES À FORT POTENTIEL (source Valentin/AGS)
Explorer systématiquement dans chaque zone. Tout secteur B2C/B2B local reste éligible si gates passent.

| # | Niche | CA cible | Panier site |
|---|-------|----------|-------------|
| 1 | Paysagistes particuliers | > 300k€ | 2 500–6 000€ |
| 2 | Rénovation générale | > 300k€ | 3 000–6 000€ |
| 3 | Architectes (petits/moyens) | > 300k€ ou ≥3 emp | 2 500–5 000€ |
| 4 | Expertise-comptable indép. | > 400k€ | 3 000–6 000€ |
| 5 | Cabinets recrutement spé. | ≥3 emp | 3 000–6 000€ |
| 6 | Cliniques dentaires indép. | ≥4 emp | 3 000–6 000€ |
| 7 | Cliniques privées/esthétiques | ≥4 emp | 4 000–8 000€ |
| 8 | Centres formation privés | ≥5 emp | 3 500–7 000€ |
| 9 | Bureaux d'études | > 300k€ | 3 000–6 000€ |
| 10 | Cabinets conseil B2B | > 300k€ | 3 500–7 000€ |
| 11 | Couvreurs | > 500k€ | 2 500–5 000€ |
| 12 | Gestion patrimoine (CGP) | ≥3 emp | 4 000–8 000€ |
| 13 | Kiné multi-praticiens | > 300k€ | 2 500–4 500€ |
| 14 | Salles sport premium | > 500k€ | 2 500–5 000€ |
| 15 | Dératisation/désinsectisation | > 500k€ | 2 500–4 500€ |
| 16 | Transport B2B | > 500k€ | 3 000–6 000€ |
| 17 | Climatisation/chauffage | > 300k€ | 2 500–5 000€ |
| 18 | Hôtels 4★+ | > 500k€ | 4 000–8 000€ |
| 19 | Services animaux | > 300k€ | 2 000–4 000€ |
| 20 | Coachs (sport/business/santé) | > 300k€ | 2 500–5 000€ |
| 21 | Escape games/loisirs | > 300k€ | 3 000–6 000€ |
| 22 | SaaS/startups matures | > 300k€ | 4 000–10 000€ |
| 23 | Agences branding/comm print | > 300k€ | 3 500–7 000€ |
| 24 | Menuiserie haut de gamme | > 300k€ | 3 000–6 000€ |
| 25 | Isolation/rénovation énergétique | > 300k€ | 2 500–5 000€ |

**Upsells :** SEO local, Google Ads, GMB/avis, Meta Ads, LinkedIn Ads (B2B), landing pages, branding, email marketing.

---

## SUPABASE — VALEURS ENUM (référence technique)
- `angle` : 'SEO', 'Ads', 'Refonte', 'Création site', 'Image de Marque', 'Multi'
- `ca_proof_level` : 'Confirmé', 'Probable', 'Déduit'
- `final_status` : 'candidate', 'qualified', 'uncertain', 'disqualified', 'error'
- `phase` : 'found', 'pre_analyzed', 'chrome_visited', 'scored', 'crm_injected'
- `elimination_gate` : INTEGER (0=général, 3=Gate3, 5=R5)
- `total_score` : GENERATED column (ne pas insérer)
- Colonnes contact V5.2 : `contact_name`, `phone_mobile`, `phone_main`, `linkedin_url`, `email`, `accroche`, `axes_amelioration`

---

## RÈGLE DE SESSION — QUOTA CALLABLE (R33 — V5.3)

`session X` = la machine tourne jusqu'à avoir **X qualifiés CALLABLE** (= `phone_mobile` 06/07 du dirigeant identifié).

**Logique d'arrêt :**
- Le compteur qui déclenche l'arrêt = nombre de qualifiés avec `phone_mobile` rempli (06/07)
- Qualifiés sans 06/07 → Supabase only, NE COMPTENT PAS dans le quota
- Incertains, disqualifiés → Supabase comme d'habitude
- La machine continue de piocher dans le pool / sourcer tant que le quota callable n'est pas atteint
- Si le pool est épuisé ET quota non atteint → signaler à Yanis avec le décompte (ex: "8/10 callable trouvés, pool vide")

**Requête de suivi en cours de run :**
```sql
SELECT COUNT(*) FROM prospects
WHERE session_id = '[SESSION_ID]'
  AND final_status = 'qualified'
  AND phone_mobile IS NOT NULL
  AND phone_mobile ~ '^0[67]';
```

**Résumé fin de session :**
- X/X callable → CRM (objectif atteint)
- Y qualifiés sans 06/07 → Supabase only (machine secrétariat)
- Z disqualifiés / W incertains → Supabase

---

## POOL CANDIDATS — RÈGLES DE RUN (V5.1)

### R29 — Skip Phase 1 si candidats existants
Avant de lancer un run, vérifier le pool :
```sql
SELECT COUNT(*) FROM prospects WHERE final_status = 'candidate' AND phase = 'found';
```
- **Pool > 0** → NE PAS chercher de nouveaux candidats. Piocher directement dans le pool existant et passer à Phase 2 (pré-analyse).
- **Pool = 0** → Phase 1 classique (sourcing Google Maps / scraper).

### R30 — Anti-doublon zones obligatoire
Avant tout sourcing (Phase 1), vérifier les villes déjà couvertes :
```sql
SELECT DISTINCT city FROM prospects ORDER BY city;
```
Ne JAMAIS sourcer une ville qui a déjà des prospects (quel que soit leur statut). Prioriser les villes de l'aire métropolitaine Lyon non présentes dans cette liste.

> Process Swarm (Phases 1-6), injection CRM (script JS), et protocole anti-fuite → voir STRATEGY_V1.md
