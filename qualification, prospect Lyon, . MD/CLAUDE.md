# CLAUDE.md — Briefing long-terme pour reprises de contexte
> Dernière mise à jour : 9 mars 2026 (V5.3 — 51 qualifiés, 199 prospects + 1598 candidats pool, CRM 64 leads, R33 quota callable, R31 CRM=06/07 only, colonnes contact structurées)
> Ce fichier est ta mémoire principale. Lis-le en premier à chaque nouvelle session.

---

## QUI EST YANIS

- **Métier** : Entrepreneur — vend des sites web (vitrine, one-page, multipages, e-commerce) + SEO/GEO + Google Ads
- **Zone** : Lyon et aire métropolitaine (~30 km, 59 communes)
- **Email** : yabouridasannier@gmail.com
- **Plan Claude** : Pro (20€/mois) — à surveiller pour les runs intensifs, passage Max (~100€) envisagé
- **Supabase** : ✅ CONFIGURÉ — projet `ngewdelqytymolemrkcc` — voir STRATEGY_V1.md pour les credentials

---

## CE QU'ON A CONSTRUIT

### Fichiers dans ce dossier
| Fichier | Contenu | Statut |
|---|---|---|
| `Document sans titre.docx` | Playbook de qualification original (source de vérité absolue) | ✅ Référence |
| `FICHE_PROSPECT_JEB_Agencement.docx` | Premier test — JEB Agencement ⚠️ FAUX POSITIF (reclassifié DISQUALIFIÉ en session 6 — site moderne) | ✅ Livré |
| `RAPPORT_Methodo_et_Automatisation.docx` | Rapport 22 pages : méthodo + plan automatisation V1 | ✅ Livré |
| `STRATEGY_V1.md` | Architecture technique Swarm V4.3 complète — Phases 1-6, CRM injection, anti-fuite, R33 quota callable (réécrit 09/03/2026) | ✅ Référence V5.3 |
| `CALIBRATION_LOG.md` | Journal de calibration — tous les feedbacks coach + règles extraites | ✅ Référence V4 |
| `SKILL.md` | Règles complètes de qualification V5.3 (~200 lignes, R33 quota callable) — à lire avant chaque run | ✅ Référence V5.3 |
| `FICHE_ART_Paysage_Elagage_QUALIFIE_76.docx` | Test blind — ART Paysage (faux positif, score 76/100) | ✅ Livré |
| `SYNTHESE_TEST_BLIND_24022026.docx` | Synthèse des 6 prospects du test blind | ✅ Livré |
| `RAPPORT_Qualification_V4.docx` | Rapport complet mode de fonctionnement V4 (9 chapitres, 473 paragraphes) | ✅ Livré |

### Skill Cowork — ⚠️ À CRÉER
- **`qualification-prospects-lyon`** — skill prévu avec toutes les règles, gates, scoring, anti-hallucination, format DOCX, logique Supabase et séquence zones. Emplacement cible : `/mnt/.claude/skills/qualification-prospects-lyon/` — **N'existe pas encore.**

### Scripts générateurs (dans la VM — à recréer si session reset)
- `fiche_prospect.js` — générateur DOCX fiche individuelle (Node.js + docx)
- `rapport_v4.js` — générateur DOCX rapport mode de fonctionnement V4
- Skill à lire avant tout travail DOCX : `/mnt/.skills/skills/docx/SKILL.md`

---

## STATUT ACTUEL DU PROJET

**Phase : V5.3 — R33 quota callable, STRATEGY_V1.md réécrit (Swarm V4.3 complet), SKILL.md ~200 lignes — prêt pour sessions rapides**

**Fait :**
- ✅ Playbook lu et intégré (toutes les règles maîtrisées)
- ✅ Premier test JEB Agencement — ⚠️ faux positif historique (90/100, site non visité, reclassifié DISQUALIFIÉ en session 6)
- ✅ Rapport méthodologie + automatisation livré (22 pages, 859 paragraphes)
- ✅ Supabase configuré — schéma SQL déployé (23/02/2026)
- ✅ Session 5 partielle (EMH Plomberie 73/100 qualifié, L'Atelier du Print 61/100 incertain)
- ✅ Test blind 6 prospects (24/02/2026) — résultat : 1 qualifié sur 6 (ART Paysage 76/100)
- ✅ Calibration V2→V3 (25/02/2026) — feedbacks coach reçus (3 faux négatifs, 1 faux positif), R1-R4 extraites, grilles intermédiaires déployées
- ✅ CALIBRATION_LOG.md créé — journal d'apprentissage persistant
- ✅ Supabase corrigé (25/02/2026) : statuts coach appliqués, colonne `angle` ajoutée, migration contraintes V3
- ✅ Session 6 (26/02/2026) — 6 nouveaux qualifiés insérés, 15/15 atteint, revue des sites Yanis
- ✅ Overhaul V4 déclenché (26/02/2026) — 4 faux positifs détectés (JEB, EMH, Garage Valette, Atouts Peinture), reclassifiés DISQUALIFIÉ
- ✅ Grille V4 déployée (26/02/2026) — WebFetch obligatoire, sans site = exclu, scoring 50/25/15/10
- ✅ Mode écho SUPPRIMÉ (26/02/2026) — cause racine de tous les faux positifs (sites non visités)
- ✅ CALIBRATION_LOG.md mis à jour V4 — R5, R6, R7 ajoutées, JEB retiré comme référence
- ✅ SKILL.md V4 créé — processus complet avec pré-filtre, WebFetch, grille 50/25/15/10
- ✅ État Supabase : 11 qualifiés / 11 disqualifiés / 1 incertain (23 total, 26/02/2026)
- ✅ 25 niches AGS ajoutées dans SKILL.md (27/02/2026) — source Valentin Heinly
- ✅ Niches exclues ajoutées (boulangeries, coiffeurs, petits commerces) — décision Yanis 27/02/2026
- ✅ Session 7 Lyon 7e (27/02/2026) — 2 qualifiés (Franck Brévi 74, Le Framboisier 84) → reclassifiés DISQUALIFIÉ (niches exclues)
- ✅ R5b créée (27/02/2026) — exception métiers d'appel : sans site = GARDER (garages, plombiers, serruriers…)
- ✅ R6 mise à jour (27/02/2026) — site 404 métiers d'appel = prospect en or, GARDER obligatoirement
- ✅ Cafés/bars ajoutés aux niches exclues (27/02/2026)
- ✅ Angle "Création site" ajouté aux valeurs Supabase
- ✅ État Supabase : 11 qualifiés / 27 disqualifiés / 3 incertains (41 total, 27/02/2026)
- ✅ Workflow Swarm V4.1 documenté dans SKILL.md (27/02/2026) — multi-agents parallèles, gain ~65% temps
- ✅ API CRM découverte et testée (27/02/2026) — injection directe via Supabase REST depuis Chrome
- ✅ Schéma d'insertion CRM complet documenté dans SKILL.md
- ✅ Concordance Supabase↔CRM mise en place (27/02/2026) — 8 qualifiés ajoutés au CRM, EMH+JEB à supprimer par Yanis
- ✅ V4.2 déployée (27/02/2026) — DOCX supprimé, CRM = livrable unique avec notes détaillées (dirigeant LinkedIn, angle, axes)
- ✅ Format `notes` CRM enrichi : dirigeant+LinkedIn, angle d'attaque, axes d'amélioration, CA, SIRET, résumé
- ✅ Session 8 Swarm V4.2 (27/02/2026) — zones : Quincieux, Albigny, Solaize, Saint-Genis, Grigny, Genay, Genas, Vernaison, Francheville, Décines
- ✅ 3 nouveaux qualifiés : BG-BTP (76), SLDC (75), ALLOIN Concept Bâtiment (70)
- ✅ 6 incertains ajoutés : Cabinet Desbois (68), Muré Paysage (68), André Vaganay (66), CSCZ Plomberie (65), Bourdin Peinture (58), ALLOIN initialement
- ✅ 2 disqualifiés R4 : Cloisor (Genay, site 4-4.5/5), OCCEN (Lyon, site 3.5-4/5)
- ✅ CRM injecté : 3 qualifiés → 35 leads total, 25 PROSPECT IDENTIFIÉ
- ✅ Session 8b — revue incertains (28/02/2026) : 4 promus qualifiés (KPN Renovation, Easy Clim, CDA Auto, Serrurerie Fidésienne), 3 disqualifiés R4 (Verneil Formation, SVH & Associés, Phébus), 5 restent incertains
- ✅ Session 8c — revue incertains suite (28/02/2026) : 3 promus qualifiés (André Vaganay, IDFacade, DGN Maçonnerie), 6 disqualifiés (Cabinet Desbois, Muré Paysage, AD Auto Pros, La Nuelloise, L'Atelier du Print, Bourdin Peinture)
- ✅ R14 créée (28/02/2026) — toujours tester URLs avant insertion Supabase
- ✅ R15 créée (28/02/2026) — temps de chargement = levier commercial majeur (>3s = 70% utilisateurs partent)
- ✅ Axes d'amélioration prioritaires formalisés (liste de 10 dans SKILL.md)
- ✅ R11 renforcé — double-check copyright obligatoire (2 prospects ©2026 avaient échappé : Muré Paysage, Bourdin Peinture)
- ✅ Concordance Supabase↔CRM vérifiée — 5 manquants rattrapés (BG-BTP, SLDC, Simonetti SA, Menuiserie Sornay, ALLOIN)
- ✅ État Supabase : 33 qualifiés / 8 incertains / 46 disqualifiés (87 total, 28/02/2026)
- ✅ État CRM : 38 PROSPECT IDENTIFIÉ (inclut ~5 anciens disqualifiés que Yanis doit supprimer manuellement)
- ✅ Session 25 SWARM (28/02/2026) — zones : Vaulx-en-Velin, Villeurbanne, Meyzieu, Rillieux-la-Pape, Caluire, Pierre-Bénite, Chaponnay
- ✅ 3 nouveaux qualifiés R5b (sans site, métiers d'appel) : La Rhodanienne de Carrelage (80), Roque Plomberie (70), Persico et Bornier (67)
- ✅ 6 disqualifiés : Nicolas Peinture (R4), Les Menuisiers du Rhône (R4), Muré Energies (R4/filiale), Galien Toitures (R11), Plomberie du Rhône (groupe GAP), RFL Ravalement (R4)
- ✅ 8 incertains ajoutés : IPEL Fluides (69), BGP Plomberie (68), SLPIB (65), Jean Rivière (62), MG BAT (61), Entreprise Mancini (60), BCCA2 (58), CEDDIA TP (57)
- ✅ Concordance finale : 3 manquants CRM rattrapés (Le Clocher, Valente SAS, Ducret Bois)
- ✅ État Supabase (pré-session test) : 36 qualifiés / 16 incertains / 52 disqualifiés (104 total, 28/02/2026)
- ✅ **V4.3 anti-fuite déployée (28/02/2026)** — nouveau statut `candidate` + colonne `phase` (found→pre_analyzed→chrome_visited→scored→crm_injected)
- ✅ Migration Supabase `add_candidate_status_and_phase` appliquée
- ✅ SKILL.md mis à jour — workflow Swarm V4.3 avec agent CHECKPOINT + protocole de reprise après saturation
- ✅ **Session test V4.3 RÉUSSIE (28/02/2026)** — 25 candidats, 6 qualifiés, 5 incertains, 14 disqualifiés, **ZÉRO FUITE**
- ✅ Zones session test : Neuville-sur-Saône, Fontaines-sur-Saône, Jonage, Pusignan, Tassin-la-Demi-Lune, Craponne, La Mulatière, Marcy-l'Étoile, Champagne-au-Mont-d'Or, Saint-Didier-au-Mont-d'Or, Limonest, Saint-Forgeux, L'Arbresle
- ✅ 6 nouveaux qualifiés : Echo Garage (82), Jury et Fils (76), Electriklim (75), PZS Sébastien Nicolas (74), Goin Nicolas Fils TP (72), FM Façadier (70)
- ✅ 5 incertains : KD Rénov (67), CTM Bire et Fils (66), 2B Construction Bois (66), Soly Renov (60), AMB Propreté (53)
- ✅ CRM injecté : 6 qualifiés → 50 leads total CRM
- ✅ État Supabase : **42 qualifiés / 21 incertains / 66 disqualifiés (129 total, 28/02/2026)**
- ✅ Concordance Supabase↔CRM vérifiée — 6/6 présents
- ⚠️ Note technique : `elimination_gate` = INTEGER (0=général R4/R11, 3=Gate3, 5=R5), `total_score` = GENERATED column, `crm_status` = enum (new/contacted/ignored), `angle` = enum (Création site/Refonte/Multi/Image de Marque/SEO)
- ⚠️ Note technique : `ca_proof_level` = enum FRANÇAIS ('Confirmé', 'Probable', 'Déduit') — PAS d'anglais
- ✅ **Session Monts d'Or/Ouest/Sud V4.3 (28/02/2026)** — 22 candidats, session `03338ce1`
- ✅ Zones : Collonges-au-Mont-d'Or, Couzon-au-Mont-d'Or, Fleurieu-sur-Saône, Charbonnières-les-Bains, La Tour-de-Salvagny, Lissieu, Chaponost, Millery, Communay, Ternay, Toussieu, Sainte-Consorce, Charly, Saint-Cyr-au-Mont-d'Or
- ✅ 6 nouveaux qualifiés : SABEKO (77), Charly Automobiles (73), Math SARL (72, R5b sans site), BH Plomberie (70), La Solution Climatique (70), JE DIS VERT (70)
- ✅ 8 incertains : Curtet et Blazy (66), STPML (66), ECEC (64), Brocard Durand (61), Decock Audric (61), Matthieu Bertrand (61), Garage Des Monts D'Or (56), Les Règles de l'Art (55)
- ✅ 8 disqualifiés : Ateliers Charignon (R4), Atelier des Gambins (R4 ©2025), Menuiserie Delandrea (R4 ©2024), Franck Planet Paysage (R4 ©2026), AS Depann (R4 ©2024), Grévon Frères (R4 ©2026) + 2 R5 pré-filtre
- ✅ CRM injecté : 6 qualifiés → **56 leads total CRM**
- ✅ Concordance Supabase↔CRM vérifiée — 22/22 zéro fuite
- ✅ **État Supabase : 48 qualifiés / 29 incertains / 74 disqualifiés (151 total, 28/02/2026)**
- ✅ **Session restructuration CRM V4.4 (01/03/2026)** — refonte complète du CRM
- ✅ Recherche contacts : 25/28 téléphones trouvés, 22 dirigeants identifiés (pappers, societe.com, Google Maps)
- ✅ Restructuration 45 leads CRM au format V4.4 — 3 blocs : 📞 Contact / 🎯 Angles+Axes / 🔗 Implication
- ✅ Double-check 8 prospects restants : 3 gardés (BH Plomberie, La Solution Climatique, Roque Plomberie — preuves croissance), FM Façadier qualifié direct, 4 disqualifiés (Goin Nicolas, Math SARL, Persico et Bornier, JE DIS VERT)
- ✅ R18 créée — sans site + aucune preuve croissance = DISQUALIFIÉ ; avec preuves = GARDER
- ✅ Nettoyage CRM automatisé (01/03/2026) : 11 disqualifiés supprimés + 5 doublons supprimés
- ✅ Disqualifiés supprimés du CRM : Charroin Toitures, Echo Garage, Goin Nicolas, JE DIS VERT, La Rhodanienne, Lyon Créateurs, Math SARL, Persico, SLDC (×2), Smile Cube
- ✅ Doublons supprimés du CRM : ALLOIN ×2→1, BG-BTP ×2→1, Menuiserie Sornay ×2→1, Simonetti SA ×2→1, Jury et Fils (doublon de Jury & Fils)
- ✅ **État final CRM : 42 PROSPECT IDENTIFIÉ (39 nommés + 3 vides perso Yanis)**
- ✅ **État Supabase : 39 qualifiés / 38 incertains / 101 disqualifiés (178 total, 01/03/2026)**
- ✅ **Concordance Supabase↔CRM : 39/39 parfaite**
- ⚠️ Note technique CRM : clé anon extraite via JWT regex `eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+` — le nom du bundle JS change à chaque redéploiement
- ℹ️ R28v2 (09/03) : tél non bloquant — Electriklim et Roque Plomberie restent qualifiés (canal LinkedIn/email)
- ✅ **Session revue incertains batch 1 — V4.5 (01/03/2026)** — revue prospects #1-20 du fichier 38_Incertains
- ✅ Verdicts Yanis : 9 qualifiés, 8 disqualifiés, 2 liens cassés vérifiés, 1 non mentionné (#18 Orakci)
- ✅ 9 qualifiés batch 1 : ATS Carrosserie, IPEL Fluides, STPML, 2B Construction Bois, Entreprise Bouvard, SLPIB, ECEC, Garage du Sud-Est, MG BAT
- ✅ 8 disqualifiés batch 1 : BGP Plomberie, COIRO TP, KD Rénov, Curtet et Blazy, CTM Bire, PERRIN Paysage, Jean Rivière, Delabre Bento
- ✅ **4 nouvelles règles** : R25 (accroche = 4e bloc CRM), R26 (5 templates accroches A-E), R27 (factuel > design), R28 (pas de tél = pas de qualification)
- ✅ **Format CRM V4.5** : 4 blocs (📞 Contact / 🎯 Angles+Axes / 📣 Accroche / 🔗 Implication) — accroche obligatoire
- ✅ Exception R11 ajoutée : ©2026 MAIS site tellement moche = GARDER (cas 2B Construction Bois)
- ✅ Recherche téléphones : 11/13 trouvés, 2 introuvables (CYM Entreprise, IDFacade)
- ✅ R28 appliquée : CYM Entreprise + IDFacade disqualifiés (tél introuvable après recherche 6+ sources)
- ✅ CRM injecté : 7 nouveaux + 2 mis à jour (ATS, Garage du Sud-Est) + 1 rattrapage (Yakarrosserie) + 2 supprimés (CYM, IDFacade)
- ✅ **État final CRM : 64 total, 54 PROSPECT IDENTIFIÉ**
- ✅ **État Supabase : 51 qualifiés / 25 incertains / 123 disqualifiés (199 total)**
- ✅ **Concordance Supabase↔CRM : 51/51 parfaite (+ ~13 leads perso/historiques Yanis)**

- ✅ **SKILL.md V5 déployé (09/03/2026)** — simplifié de 399→~160 lignes, toutes les règles préservées (R4-R28, 4 Gates, scoring, CRM 4 blocs, 5 accroches, 25 niches AGS, Supabase enums)
- ✅ Process Swarm (Phases 1-6), injection CRM (script JS), protocole anti-fuite → externalisés dans STRATEGY_V1.md (référencé en bas de SKILL.md)
- ✅ Vibe Prospecting MCP testé (09/03/2026) — NON VIABLE pour Lyon PME (city_region US-only, 20% couverture mobile, profils inadaptés)
- ✅ Apollo.io MCP identifié — free-to-search, disponible dans le registry (directoryUuid: `8fd555a4-ea5f-49cf-9335-582dd6760597`), pas encore connecté
- ✅ **SKILL.md V5.1 déployé (09/03/2026)** — 2 changements majeurs :
  - **R28v2** : Téléphone NON BLOQUANT. Seuls 06/07 comptent. Standard (01-05/09) = secrétariat = inutile. Sans 06/07 → canal LinkedIn/email. Injection CRM possible sans tél.
  - **Gate 2** : CA abaissé de 150k€ à **70k€** pour TOUS les prospects (pas juste création site)
  - Scoring contactabilité ajusté : LinkedIn remplace email/form dans la grille (0-3 pts)
  - BLOC 1 CRM : dirigeant obligatoire, tél 06/07 SI dispo, LinkedIn/email = canal par défaut si pas de 06/07
- ✅ Instant Data Scraper recommandé (09/03/2026) — extension Chrome 100% gratuite, export CSV, ~120 résultats/recherche Google Maps. Yanis l'installe.
- ✅ Revue complète des règles (09/03/2026) — audit bottlenecks et fuites. R11 et R5 gardés tels quels (Yanis : "trop complexe à changer").
- 💡 **Idée niche focus** (09/03/2026) — Yanis mentionne vouloir se concentrer sur ~5 niches (conciergeries, paysagistes marchent bien). "Garde-le en tête" = pas d'action immédiate.
- ✅ **Pool candidats pré-sourcés (09/03/2026)** — Yanis a lancé des runs Phase 1 via d'autres chats Claude → **1 598 candidats** injectés en Supabase (status `candidate`, phase `found`), répartis sur **77 villes**
- ✅ **R29 ajoutée dans SKILL.md** — Skip Phase 1 si pool candidats > 0 (requête SQL avant chaque run)
- ✅ **R30 ajoutée dans SKILL.md** — Anti-doublon zones obligatoire : `SELECT DISTINCT city FROM prospects` avant tout sourcing, ne jamais sourcer une ville déjà présente
- ✅ **SKILL.md V5.1b** — section "POOL CANDIDATS — RÈGLES DE RUN" ajoutée avec R29 + R30 + requêtes SQL
- ⚠️ `zones_coverage` table quasi vide (1 entrée Lyon 3e) — les autres chats n'ont pas rempli cette table. Workaround : utiliser `SELECT DISTINCT city FROM prospects` (R30)
- ✅ **SKILL.md V5.2 déployé (09/03/2026)** — 2 nouvelles règles majeures :
  - **R31** : CRM = UNIQUEMENT si `phone_mobile` = 06/07 du dirigeant. Tous les qualifiés → Supabase (colonnes structurées). Sans 06/07 → Supabase only, machine secrétariat récupère.
  - **R32** : PAS de double vérification séparée. La machine qualifie → Supabase/CRM. Yanis vérifie au moment du GK2 (30s/prospect), pas avant.
  - Section "DESTINATION DES QUALIFIÉS" réécrite avec routing clair (tous→Supabase, 06/07→CRM)
- ✅ **Migration Supabase `add_dirigeant_contact_columns` (09/03/2026)** — 3 colonnes ajoutées : `linkedin_url`, `accroche`, `axes_amelioration` + index `idx_prospects_callable` sur (final_status, phone_mobile)
- ✅ **Colonnes contact structurées V5.2** : `contact_name`, `phone_mobile`, `phone_main`, `linkedin_url`, `email`, `accroche`, `axes_amelioration` — remplacent le vrac dans `notes`
- ℹ️ Stats callable (09/03) : 62 qualifiés en base, seulement 3 avec `phone_mobile` rempli, 0 avec `linkedin_url`, 19 avec `email` — données contact historiques encore dans `notes` (à migrer progressivement)
- ✅ **SKILL.md V5.3 déployé (09/03/2026)** — R33 ajoutée :
  - **R33** : `session X` = X prospects CALLABLE (phone_mobile 06/07 du dirigeant). La machine ne s'arrête pas tant que le quota callable n'est pas atteint. Qualifiés sans 06/07 → Supabase only, ne comptent pas dans le quota.
  - Section "RÈGLE DE SESSION — QUOTA CALLABLE" ajoutée avec requête SQL de suivi et format résumé fin de session
- ✅ **STRATEGY_V1.md entièrement réécrit (09/03/2026)** — ancien fichier (23/02/2026) obsolète, ne documentait pas Swarm V4.3
  - Nouveau contenu : architecture Swarm complète (Phases 1-6), injection CRM (script JS), protocole anti-fuite, R33 quota callable, credentials Supabase/CRM, requêtes SQL de suivi
  - Référencé par SKILL.md ligne 238

**Prochaines étapes (dans l'ordre) :**
1. ⏳ **Lancer sessions de qualification depuis le pool** — 1 598 candidats prêts, passer directement Phase 2 (R29)
2. ⏳ Tester Instant Data Scraper sur une zone Lyon (batch pré-filtre via Google Maps CSV) — extension installée par Yanis
3. ⏳ Connecter Apollo.io MCP et tester filtrage Lyon + couverture PME françaises
4. ⏳ Revue incertains batch 2 (#21-42) — 22 prospects restants à revoir avec Yanis + #18 Orakci Façade non mentionné
5. ⏳ Relancer sessions SWARM V4.3 — zones non couvertes restantes (Est Lyon, Sud-Est, Nord-Ouest)
6. ⏳ Réfléchir focus ~5 niches (conciergeries, paysagistes identifiés comme top performers — à valider avec Yanis)
7. ⏳ Nettoyage/compression des documents de mémoire (prochaine maintenance)
8. ⏳ Explorer mesure automatique des temps de chargement (R15 — Yanis intéressé)
9. ⏳ Créer le shortcut Cowork planifié (8h00, lun-ven) — PC doit être allumé

**Contexte AGS :**
- Valentin = coach, structure qui accompagne ~3200 élèves, 5 coachs, 20-30 membres actifs
- Tous utilisent le "filtre en or" (même méthodo que Yanis)
- Potentiel SaaS : ~150€/mois × 30 membres = 4500€/mois
- Mission immédiate : 15 qualifiés validés par le coach

---

## RÈGLES DE QUALIFICATION — RÉSUMÉ CRITIQUE

### Pré-filtre obligatoire V5.3 (AVANT Gate 0)
- 📞 **R28v2 — Téléphone NON BLOQUANT** : Seuls 06/07 (mobile/ligne directe) ont de la valeur. Standard (01-05/09) = secrétariat = inutile (redirige vers mail). Sans 06/07 → canal LinkedIn + email. Prospect qualifiable sans téléphone.
- 📋 **R31 — CRM = 06/07 dirigeant UNIQUEMENT** : Tous les qualifiés → Supabase (colonnes structurées). CRM = seulement si `phone_mobile` 06/07 trouvé. Sans 06/07 → Supabase only, machine secrétariat récupère.
- ⚡ **R32 — Pas de double vérification** : La machine qualifie → Supabase/CRM direct. Yanis vérifie au moment du GK2 (30s/prospect), pas dans un pass séparé.
- 🎯 **R33 — Quota callable** : `session X` = X prospects CALLABLE (06/07 dirigeant). Qualifiés sans 06/07 → Supabase only, ne comptent pas dans le quota. Machine continue tant que quota non atteint.
- **Pas de site** → EXCLU (R5) **SAUF métiers d'appel** (R5b : garages, plombiers, serruriers, artisans BTP…) → GARDER, angle "Création site"
- **Site Error 404** → **Métiers d'appel = GARDER obligatoirement** (prospect en or). Autres : EXCLU uniquement si preuve concrète d'abandon prolongé (R6).
- **Screenshot obligatoire via Claude in Chrome** (R7) — visiter le site + screenshot + analyse visuelle 1-5 avant tout scoring
- **Date copyright** : 2025-2026 = site récent (signal R4). 2022 et avant = bon signal cible.
- **Site visiblement beau et moderne (note 4-5)** → STOP immédiat, R4 (Bon site = NQ)
- **Niches exclues** : boulangeries, coiffeurs, cafés/bars, petits commerces (tabac, kebabs, snacks)
- **Temps de chargement** (R15) : >3 secondes = levier commercial majeur → toujours noter dans les axes
- **Tester les URLs** (R14) : toujours vérifier qu'une URL répond AVANT insertion Supabase

### Les 4 Gates binaires V4 (ordre strict — premier échec = STOP immédiat)
- **Gate 0** : B2C local → OUI direct. B2B industriel → OUI si site existant + effort contenu visible + taille significative (angle image de marque). Sinon STOP.
- **Gate 1** : Exclusions sectorielles → alcool, porc, drogue = ÉLIMINÉ
- **Gate 2** : CA ≥ 70 000 € — BINAIRE UNIQUEMENT, aucun point de scoring
- **Gate 3** : ≥ 3 axes d'amélioration FLAGRANTS sur le site — si < 3, STOP (prospect pas prêt à payer)

### Scoring — GRILLE V4 (26/02/2026) — seulement si pré-filtre + 4 gates passés
- **Écart Site/Standing** (inclut image de marque + esthétique) : 0-**50** pts ← DIMENSION PRINCIPALE
- **Besoins digitaux** (Ads, SEO, réseaux) : 0-**25** pts
- **Croissance** (signaux positifs) : 0-**15** pts
- **Contactabilité** (infos directes trouvables) : 0-10 pts
- **Total ≥ 70 = QUALIFIÉ | 55-69 = INCERTAIN | < 55 = NON QUALIFIÉ**
- ⚠️ CA = gate binaire seulement, JAMAIS de points
- ⚠️ Fonctionnel ≠ Suffisant — l'esthétique compte autant que les fonctionnalités
- ⚠️ Bon site = NON QUALIFIÉ même avec fort standing

### Règle anti-hallucination (ABSOLUE — jamais déroger)
Chaque info doit être étiquetée :
- **Confirmé** : source officielle directe (site, pappers, Google Maps, SIRET)
- **Probable** : cohérent avec plusieurs signaux indirects
- **Déduit** : logique mais non vérifiable — TOUJOURS indiqué explicitement dans la fiche

### Sources autorisées (dans l'ordre de priorité)
Site officiel → Google Maps → pappers.fr/societe.com → réseaux sociaux → Meta Ads Library → Pages Jaunes

---

## COMPORTEMENT EN CAS DE REPRISE DE CONTEXTE

1. Lire CE fichier + `CALIBRATION_LOG.md` + `SKILL.md` (les 3 sont la mémoire du système)
2. Demander à Yanis : "On est à quelle étape ?"
3. Ne refaire aucun fichier déjà listé comme ✅ Livré
4. Si Supabase pas configuré → demander URL + clé anon avant toute autre action
5. Si shortcut pas créé → créer après Supabase

### Hiérarchie de mémoire
| Fichier | Rôle | Fréquence de lecture |
|---|---|---|
| `CLAUDE.md` | Contexte général + statut projet | À chaque session |
| `CALIBRATION_LOG.md` | Historique corrections coach + règles extraites | À chaque session |
| `SKILL.md` | Règles complètes de qualification V5 (~160 lignes) | Avant chaque run |
| `STRATEGY_V1.md` | Architecture technique Swarm V4.3 + CRM + anti-fuite + R33 | Si besoin technique |

---

## RACCOURCI MANUEL — COMMANDE "SESSION N" (R33 — V5.3)

Yanis peut lancer un run de qualification à tout moment en tapant simplement :
- `session 5` → 5 prospects **CALLABLE** (06/07 dirigeant)
- `session 10` → 10 prospects **CALLABLE**
- `session 30` → 30 prospects **CALLABLE**

⚠️ **R33** : Le chiffre = nombre de qualifiés avec `phone_mobile` 06/07 du dirigeant. Les qualifiés sans 06/07 vont en Supabase only (machine secrétariat) et ne comptent PAS dans le quota. La machine continue tant que le quota callable n'est pas atteint.

Le run reprend toujours là où Supabase en est (zone suivante non couverte, zéro doublon).

**Workflow V4.3 (depuis 28/02/2026) — ANTI-FUITE :**
- **Agent CHECKPOINT** en Phase 1 : injecte CHAQUE candidat dans Supabase immédiatement (status `candidate`, phase `found`)
- Colonne `phase` trace la progression : `found → pre_analyzed → chrome_visited → scored → crm_injected`
- **Reprise après saturation** : requêter `SELECT phase, COUNT(*) FROM prospects WHERE session_id='[ID]' GROUP BY phase` et reprendre là où ça s'est arrêté
- Plus de DOCX — le CRM est le livrable unique
- Notes CRM enrichies : dirigeant (prénom+LinkedIn), angle d'attaque, axes d'amélioration, CA, SIRET, résumé
- Concordance permanente Supabase ↔ CRM à chaque fin de run
- Lire SKILL.md pour le workflow complet (Phases 1-6)

---

## RÈGLE — SIGNALEMENT D'INCOHÉRENCES

Dès qu'une contradiction est détectée (entre deux instructions, entre une règle et un cas concret, entre ce que Yanis dit et ce que le coach dit) → STOP et signalement immédiat avant de continuer. Format : ⚠️ INCOHÉRENCE DÉTECTÉE + les deux règles en conflit + une question ciblée pour trancher.

## MAINTENANCE DU CONTEXTE (à faire toutes les ~10 sessions)

Les fichiers de mémoire grossissent avec le temps → coût tokens croissant. Toutes les 10 sessions environ, compresser CALIBRATION_LOG.md (garder les règles extraites, supprimer l'historique narratif détaillé) et purger les sections obsolètes du SKILL.md. Claude fait cette maintenance de sa propre initiative, sans attendre.

---

## CRM PERSONNEL — INTÉGRATION V4.2

**URL CRM :** https://structur-a-lead.vercel.app/leads
**Backend :** Supabase (`eywnzgsvrsxzahoiwnml.supabase.co`) — injection via Chrome JS
**Colonne à utiliser :** "PROSPECT IDENTIFIÉ" (stage = `PROSPECT_IDENTIFIE`)
**Déclencheur :** Automatiquement à la fin de chaque run + concordance Supabase↔CRM

**Protocole V4.2 (actif depuis 27/02/2026) :**
- Injection automatique en batch via API REST (Chrome JS) — plus besoin de demander
- Plus de DOCX — le CRM est le livrable unique
- Notes enrichies : dirigeant (prénom+LinkedIn), angle d'attaque détaillé, axes d'amélioration, CA, SIRET
- Concordance permanente : chaque fin de run compare Supabase qualifiés vs CRM leads
- Suppressions CRM = manuelles par Yanis (sécurité)

**Voir SKILL.md section "CRM — INJECTION DIRECTE" pour le script et le format notes détaillé.**

---

## NOTES LONG-TERME

- Priorité absolue de Yanis : **qualité > volume** (un 90/100 vaut mieux que cinq 60/100)
- Zone de démarrage : Aire métropolitaine Lyon complète (59 communes), puis expansion
- Secteurs cibles : TOUS (critère = force du besoin Gate 3, pas le corps de métier)
- Le shortcut Cowork fonctionne UNIQUEMENT si le PC est allumé et l'app ouverte (pas de run PC éteint)
- À terme : sortie des fiches dans un logiciel externe de Yanis (format à définir avec lui)
- V2 planifiée (app Claude Code + interface web) mais non prioritaire — valider V1 d'abord
- Contexte partagé entre chats : NON automatique. Seul le CLAUDE.md + Supabase + skill = mémoire persistante
