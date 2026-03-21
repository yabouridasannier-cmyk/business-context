# CALIBRATION LOG — Qualification Prospects Lyon
> Fichier de mémoire d'apprentissage — mis à jour à chaque feedback Yanis ou coach
> À lire en complément de CLAUDE.md et SKILL.md lors des reprises de contexte

---

## COMMENT UTILISER CE FICHIER

Ce fichier trace **chaque correction apportée au système de qualification** :
- Quand notre verdict ne correspondait pas au verdict du coach
- Quand une règle a été ajoutée, modifiée ou supprimée
- Les cas de référence positifs et négatifs

Il sert à :
1. Ne pas répéter les mêmes erreurs
2. Comprendre l'évolution du système et pourquoi chaque règle existe
3. Fournir des exemples concrets lors des nouvelles sessions

---

## SESSION 3 — Test Blind 6 Prospects (24/02/2026)
### Correction majeure — Verdicts du coach reçus le 25/02/2026

| Prospect | Notre verdict (V2) | Verdict coach | Écart |
|---|---|---|---|
| Valente SAS | ❌ NON QUALIFIÉ (Gate 0 — B2B) | ✅ QUALIFIÉ | Faux négatif |
| Ducret Bois | ❌ NON QUALIFIÉ (Gate 0 — B2B) | ✅ QUALIFIÉ | Faux négatif |
| Le Clocher | ❌ NON QUALIFIÉ (45/100) | ✅ QUALIFIÉ | Faux négatif |
| Château des Avenières | ❌ NON QUALIFIÉ (47/100) | ❌ NON QUALIFIÉ | ✅ Correct |
| Mont SPA Les Trésoms | ❌ NON QUALIFIÉ (50/100) | ❌ NON QUALIFIÉ | ✅ Correct |
| ART Paysage Élagage | ✅ QUALIFIÉ (76/100) | ❌ NON QUALIFIÉ | Faux positif |

**Score de précision : 2/6 corrects → calibration majeure déclenchée**

### Analyse des erreurs

**Faux négatif — Valente SAS**
Cause de l'erreur : Gate 0 trop restrictive, B2B industriel éliminé automatiquement
Argument du coach : "grosse boîte, site dégueulasse, mais il y a un effort visible (beaucoup de sections, il montre ses machines). L'angle c'est l'image de marque, pas le SEO."
Règle créée → R2 (Exception B2B Image de Marque) + révision Gate 0

**Faux négatif — Ducret Bois**
Cause de l'erreur : même que Valente SAS — Gate 0 B2B trop stricte
Argument du coach : "site très vieux, très moche, fait il y a longtemps. Site pas même une page complète."
Règle renforcée → R2

**Faux négatif — Le Clocher**
Cause de l'erreur : on avait évalué "site fonctionnel" comme passable. Score 45/100 trop bas.
Argument du coach : "Grand restaurant, grand établissement. Le site c'est juste du texte, des horaires et une adresse. Fonctionnel ≠ apparence. Site fait vieux, ne convertit pas."
Règle créée → R1 (Fonctionnel ≠ Suffisant) + révision Écart Site/Standing pour intégrer l'esthétique pleinement

**Faux positif — ART Paysage Élagage**
Cause de l'erreur : on avait scoré 76/100, surestimé l'Écart Site/Standing
Argument du coach : "Le site est relativement propre, passé du temps dessus, fait il n'y a pas si longtemps. Pas assez d'axes d'amélioration flagrants. Psychologiquement, il ne serait pas prêt à payer."
Règle créée → R3 (Gate 3 — 3 axes flagrants minimum) + R4 (Bon site = non qualifié)

---

## SESSION 6 — Revue des 15 qualifiés + Overhaul V4 (26/02/2026)

### Contexte
Après avoir atteint 15 prospects qualifiés en base, Yanis a consulté les sites internet directement et renvoyé des screenshots. Résultat : **4 faux positifs majeurs détectés**.

### Erreurs identifiées

**Faux positif — JEB Agencement (référence historique 90/100)**
Notre verdict : QUALIFIÉ 90/100 ❌ → reclassifié DISQUALIFIÉ
Argument Yanis : "JEB Agencement, leur site, il est déjà magnifique visuellement, très récent, 2025, et sans réelle amélioration flagrante."
Screenshot confirmé : design moderne, navigation structurée, photo cuisine qualitative, mise en page professionnelle.
Cause de l'erreur : **site jamais visité via WebFetch**. Évalué uniquement sur des signaux indirects.
Impact : JEB n'est plus une référence 90/100. C'est un faux positif historique.

**Faux positif — EMH Plomberie (73/100)**
Notre verdict : QUALIFIÉ 73/100 ❌ → reclassifié DISQUALIFIÉ
Argument Yanis : "EMH Plomberie, le site, il est déjà magnifique visuellement, très récent, 2025, et sans réelle amélioration flagrante."
Cause de l'erreur : site non visité. Décrit comme "site daté" sur des signaux textuels — c'était faux.

**Faux positif — Garage Valette**
Notre verdict : QUALIFIÉ (inclus en session précédente) ❌ → reclassifié DISQUALIFIÉ
Argument Yanis : "Garage Valette, 0 photo qualitative, 0 modernité du site." ← C'était notre description. Yanis a montré le screenshot : agent Renault/Dacia, hero photo professionnelle, design propre Vistalid 2026, navigation structurée.
Cause de l'erreur : **site jamais visité via WebFetch**. Notre description était l'inverse de la réalité.

**Faux positif — Atouts Peinture (74/100)**
Notre verdict : QUALIFIÉ 74/100 ❌ → reclassifié DISQUALIFIÉ
Raison : site en Error 404 depuis longtemps, non restauré.
Règle de Yanis : "Quand un site ne fonctionne pas depuis pas mal de temps et qu'il n'a pas été restauré, c'est que finalement il n'y a pas eu le besoin derrière à l'entreprise. Donc il ne faut pas les prospecter."
Règle créée → R6 (Site mort = exclu)

### Décision structurelle de Yanis — Overhaul V4

**Citation exacte de Yanis :**
> "Le plus important (je dis bien le plus important), qui vaut peut-être à 60% de la qualification, c'est vraiment : aller sur le site, voir si il est beau ou moche, s'il y a des améliorations flagrantes, s'il est fonctionnel, etc. C'est tout ça qui compte, quasiment le plus, étant donné que notre service porte d'entrée, c'est ça. Donc, si en mode éco tu vas pas sur les sites, là, ça va pas du tout."

**Décisions prises :**
1. **Mode écho SUPPRIMÉ définitivement** — cause racine de tous les faux positifs (sites non visités)
2. **Visite WebFetch obligatoire** pour tout prospect ayant un site (avant tout scoring)
3. **Sans site = exclusion automatique** — les prospects sans site ne sont pas les meilleures cibles
4. **Site en Error 404 = à vérifier** — exclusion uniquement si preuve concrète d'abandon prolongé
5. **Poids Écart Site/Standing relevé** : 40 pts → 50 pts
6. **Poids autres dimensions ajustés** : need 30→25, croissance 20→15, contact 10→10

---

## DÉCISION NICHES — 27/02/2026

### Niches exclues (décision Yanis)
- **Boulangeries** — CA insuffisant, pas de besoin site
- **Coiffeurs** — CA rarement > 150k€ pour les indépendants
- **Petits commerces de proximité** (tabac-presse, kebabs, snacks…)
Raison : "Ça sert à rien de passer du temps dessus, ils n'ont pas le capital requis. Même pas besoin d'un site pour des boulangeries."
→ Ajoutées dans SKILL.md, à appliquer dès la Phase 1 (ne pas chercher ces niches).

### 25 niches à fort potentiel (source : Valentin Heinly / AGS)
Liste complète ajoutée dans SKILL.md (Gate 0). Les 25 niches : paysagistes, rénovation générale, architectes, expertise-comptable, cabinets recrutement, cliniques dentaires, cliniques privées/esthétiques, centres de formation, bureaux d'études, cabinets conseil B2B, couvreurs, gestion patrimoine, kinésithérapie, salles de sport premium, dératisation, transport B2B, climatisation/chauffage, hôtels 4★+, services animaux, coachs, escape games, SaaS/startups matures, agences branding/print, menuiserie haut de gamme, isolation/rénovation énergétique.
→ À explorer systématiquement dans chaque zone, mais PAS exclusivement.

---

## SESSION 7 — Feedback Yanis post-run Lyon 7e (27/02/2026)

### Contexte
Run Lyon 7e : 2 qualifiés trouvés (Franck Brévi 74/100, Le Framboisier 84/100) sur ~20 analysés.
Yanis a revu les résultats et donné plusieurs feedbacks correctifs.

### Corrections appliquées

**Reclassification — Franck Brévi Coiffure (74/100) → DISQUALIFIÉ**
Raison Yanis : "Les coiffeurs, c'est pas des bons clients." Niche exclue.
→ Coiffeurs déjà dans niches exclues depuis 27/02/2026.

**Reclassification — Le Framboisier (84/100) → DISQUALIFIÉ**
Raison Yanis : "Les boulangeries, pas d'axe énormément sur la vente. Pas des bons clients."
→ Boulangeries déjà dans niches exclues.

**Nouvelle niche exclue — Cafés / bars**
Citation Yanis : "Les cafés, ils n'ont pas besoin de site Internet. Ne recherche même pas café."
→ Ajouté aux niches exclues dans SKILL.md.

**Nouvelle règle R5b — Exception métiers d'appel (sans site = GARDER)**
Citation Yanis : "Garage, carrosserie, etc. qui n'ont pas de site, c'est une grosse partie d'argent pour eux. Potentiellement, on peut les convaincre."
Logique : les artisans/métiers d'appel (plombiers, serruriers, garagistes, etc.) génèrent leur CA via appels entrants. Un site = levier de ventes direct et massif. Même sans site existant, ils restent prospectables.
→ R5 modifiée dans SKILL.md : exception pour métiers d'appel. Angle = "Création site".

**Mise à jour R6 — Site 404 pour métiers d'appel = prospect en or**
Citation Yanis : "Tous les sites cassés, avec des erreurs 404, si c'est des domaines qui ont besoin d'appels comme les plombiers, serruriers, je veux que ce soit qualifié."
→ R6 modifiée : métier d'appel + site 404 = GARDER obligatoirement (pas besoin de preuve d'abandon).

### Impact sur les prospects en base
- Garage B.P.C. (CA 1M€, pas de site) → potentiellement requalifiable (R5b)
- Carrosserie Corzani (CA 354k€, pas de site) → potentiellement requalifiable (R5b)
- Carrosserie Saint-Louis (CA confidentiel, pas de site) → potentiellement requalifiable si CA vérifié (R5b)
- ABADOM (plomberie, site cassé) → potentiellement requalifiable (R6 métier d'appel)

---

## SESSION 8 — Double-check Yanis 15 qualifiés (27/02/2026)

### Contexte
Run session 8 : 15 nouveaux qualifiés insérés (pré-score ≥ 70). Yanis a visité chaque site manuellement et donné son verdict. Chrome était déconnecté donc pas de R7 screenshots — tous les pré-scores étaient basés sur WebFetch Phase 2 sans validation visuelle.

### Résultat : 7 gardés / 5 éliminés / 3 éliminés après investigation preuves
**Score de précision : 7/15 bons → 47% (chute due à absence de R7 Chrome)**

### Corrections détaillées

**✅ GARDÉS (7)**
| Prospect | Score | Raison |
|---|---|---|
| Smile Cube | 79 | Site ancien, grosse friction prise RDV |
| Lyon Créateurs Ext. | 78 | Site beau 4.5/5 MAIS aucun CTA — sauvé par R10 |
| Carrosserie Perrière | 73 | Sans site, CA 610k€ confirmé (R5b) |
| Le Pelet | 73 | CTA formulaire daté, design pas ouf |
| RZ Électricité | 73 | Site depuis 2018, ancienneté confirmée |
| Garage Sardellitti | 72 | Site ~2017, assez nul, CTA nul |
| SECC Thermique | 71 | 3/5 mais CTA formulaire + bouton contact cassé (R10) |

**❌ ÉLIMINÉS PAR YANIS (5)**
| Prospect | Score | Raison élimination |
|---|---|---|
| Clin. Vét. Passerelle | 78 | Site très bien, beau CTA, rien à redire (R4) |
| Maison Butaud | 77 | Erreur activité (chauffage pas menuiserie) + site pas ancien, bon CTA (R12) |
| TP2R Terrassement | 74 | Site correct, pas d'axe réel (R9) |
| YMAIN Maçonnerie | 72 | Site 2025, aucun problème (R11) |
| YC Électricité | 70 | Site très bien, aucun axe réel. Design/réalisations/certifications pas des vrais axes (R13) |

**❌ ÉLIMINÉS APRÈS INVESTIGATION PREUVES (3)**
| Prospect | Score | Investigation | Résultat |
|---|---|---|---|
| Piégay Paysage | 88 | Site moderne 4/5, actif (articles nov-déc 2025), bon CTA, Alliance Paysage | ÉLIMINÉ — aucune preuve technique (R9) |
| HL Concept | 80 | Site 20+ ans, design daté, dirigeant Guillaume PRENAT trouvé | ÉLIMINÉ — Yanis avait noté 3.5/5, pas d'axe clair (R9) |
| Rhône Renov ISO | 79 | Site moderne, bon CTA orange, RGE + Pro ITE. Dirigeante: Christèle RIZZOTTI | ÉLIMINÉ — site ≥ 4/5, aucune preuve (R9) |

### Règles créées à partir de cette session

**R8 — "Design" seul n'est PAS un axe d'amélioration valide**
Le design subjectif (cohérence couleurs, esthétique) ne compte pas comme axe. Confirmé par Valentin/coach.
Vrais axes = pages cassées, non responsive, erreurs 404, site visuellement très vieillot (1-2/5 max).
"Tout ce qui est design, c'est pas ça le principal." — Yanis session 8.

**R9 — Site ≥ 3/5 = preuves techniques obligatoires pour qualifier**
Si note visuelle ≥ 3/5, on ne qualifie PAS sauf preuves concrètes :
- Pages 404 dans le site
- CTA défaillant ou absent
- Boutons cassés
- Non responsive sur mobile
- Friction forte à la prise de contact/RDV
Sans preuve technique → STOP immédiat, même avec gros CA.

**R10 — CTA absent ou défaillant = axe majeur (peut sauver un prospect)**
Pas de CTA, CTA en formulaire daté, bouton qui ne marche pas = vrai axe d'amélioration.
Peut sauver un prospect avec un site 4+/5 si le CTA est vraiment problématique.
Cas de référence : Lyon Créateurs Ext. (site 4.5/5, aucun CTA → GARDÉ).

**R11 — Copyright 2025 = site récent = ÉLIMINER automatiquement**
Extension de R4 : copyright 2025 ou 2026 = refait récemment = STOP direct.
Pas besoin de vérifier d'autres axes.

**R12 — Toujours vérifier activité réelle vs fiche**
Ne jamais se fier uniquement à Google/Pappers pour l'activité.
Vérifier sur le site que l'activité annoncée correspond.
Cas de référence : Maison Butaud (annoncé menuiserie/charpente, en réalité chauffage/plomberie).

**R13 — "Réalisations", "certifications", "SEO" ne sont pas des axes stand-alone**
Ces éléments ne comptent que s'ils accompagnent un vrai axe technique (404, CTA cassé, responsive).
Manque de page réalisations ≠ problème que le prospect paiera pour résoudre.
"Design, réalisation, certification — tout ça c'est pas bon comme axes." — Yanis session 8.

### Conclusion majeure — Enseignement session 8
Le pré-filtre WebFetch sans visite visuelle Chrome ne suffit pas pour les sites ≥ 3/5.
Il faut systématiquement chercher des preuves techniques (404, CTA cassé, responsive, date copyright) avant de qualifier.
47% de précision sans R7 Chrome vs objectif > 80%.

---

## SESSION 8b — Double-check Yanis 13 incertains (27/02/2026)

### Contexte
Review par Yanis des 13 prospects en statut "incertain" (scores 57-69). 8/13 avaient des URLs cassées dans Supabase → Yanis ne pouvait pas vérifier les sites. URLs corrigées après investigation.

### Résultat : 4 qualifiés / 3 disqualifiés (R4) / 5 restent incertains / 1 "on verra"

**✅ PROMUS QUALIFIÉS (4)**
| Prospect | Score | Raison |
|---|---|---|
| KPN Renovation | 67 | CTA quasi-invisible, site 2/5, pas responsive. "Exemple type" — Yanis |
| Serrurerie Fidésienne | 66 | Sans site, serrurerie métier d'appel, CA 314k€ confirmé |
| Easy Clim | 63 | E-commerce clim, présentation produits horrible. "Obligé d'accepter refonte" — Yanis |
| CDA Auto | 62 | Garage Vénissieux, validé par Yanis |

**❌ DISQUALIFIÉS APRÈS VÉRIFICATION SITE (3)**
| Prospect | Score | Raison |
|---|---|---|
| Verneil Formation | 69 | URL corrigée → verneil-formation.com. Site moderne 3.5-4/5 (R4) |
| SVH & Associés | 68 | URL corrigée → cabinet-svh.com. Site moderne, CTA visible (R4) |
| Phébus | 57 | URL corrigée → groupe-climater.com. Filiale groupe, site pro 4/5 (R4) |

**⏸️ EN ATTENTE**
- La Nuelloise (61) : "On verra plus tard" — Yanis doute, CTA pas top mais site OK
- 5 incertains avec URLs corrigées : Jury & Fils, Palisse Sopalver, AD Auto Pros, IDFacade, DGN Maçonnerie

### Pattern clé — R14 : Vérifier systématiquement les URLs
8/13 incertains avaient des URLs cassées (mauvais domaine). Cause : l'URL devinée lors du scraping initial ne correspondait pas au vrai domaine.
**Règle : toujours tester l'URL via Chrome/WebFetch AVANT d'insérer dans Supabase. Si 404 → rechercher le vrai domaine via Google.**

### Pattern secondaire — E-commerce avec mauvaise présentation = signal fort
Easy Clim = nouveau type de prospect : site fonctionnel mais catalogue produits horrible. Le client "est obligé d'accepter une refonte" (Yanis). À intégrer comme cas de référence pour Gate 3.

---

## SESSION 8c — Double-check Yanis 12 incertains restants (28/02/2026)

### Contexte
Suite de la review des incertains. 12 prospects restants après session 8b. Yanis a visité chaque site et donné ses verdicts.

### Résultat : 3 qualifiés / 6 disqualifiés / 3 non reviewés
**Précision du scoring : les 3 qualifiés avaient des axes réels détectés par le système → cohérent.**
**2 ratés R11 : Muré Paysage et Bourdin Peinture avaient copyright 2026 non détecté → à renforcer.**

**✅ QUALIFIÉS (3)**
| Prospect | Score | Raison Yanis |
|---|---|---|
| André Vaganay SAS | 66 | CTA redirige vers accueil, layout cassé, espaces blancs, 2.5/5 |
| IDFacade | 64 | Aucun CTA, zéro copywriting, on comprend pas l'activité. Site 2025 mais axes réels |
| DGN Maçonnerie | 62 | Pages 404, design 3/10, HTML, Gmail, logo énorme |

**❌ DISQUALIFIÉS (6)**
| Prospect | Score | Raison |
|---|---|---|
| Cabinet Desbois | 68 | Pas d'axe d'attaque. Site 3.5/5, date 2021, aucune faille exploitable |
| Muré Paysage | 68 | ⚠️ R11 RATÉ — Copyright 2026 non détecté. Éliminé directement |
| AD Auto Pros | 64 | Pas de site + pas d'ads. Réseau AD franchise, pas de levier |
| La Nuelloise | 61 | Site correct, pas assez d'axes. Non sélectionné |
| L'Atelier du Print | 61 | Site excellent. Non sélectionné |
| Bourdin Peinture | 58 | ⚠️ R11 RATÉ — Copyright 2026 non détecté |

### Règles créées/mises à jour

**R14 — Toujours tester URLs avant insertion Supabase**
Ne jamais deviner un domaine. Toujours vérifier l'existence via Chrome/WebSearch.

**R15 — Temps de chargement = levier commercial majeur (NOUVEAU)**
Mesurer systématiquement. > 3 secondes = argument énorme ("70% des utilisateurs partent").
À intégrer dans les axes CRM.

**R11 renforcé — DOUBLE CHECK copyright obligatoire**
2 prospects avec copyright 2026 sont passés au travers : Muré Paysage et Bourdin Peinture.
Action corrective : vérifier le footer de CHAQUE site pour la date copyright. C'est un critère éliminatoire automatique.

**Liste axes prioritaires formalisée** (ajoutée dans SKILL.md) :
Temps de chargement > CTA absent/défaillant > Pages 404 > Design très nul > Pages internes cassées > Non responsive > Copyright ancien > Gmail pro > Zéro copywriting.

### Enseignement clé — Session 8c
"Les infos clés pour le CRM = dirigeant + LinkedIn + axes d'amélioration. Le reste j'en ai pas besoin." — Yanis.
→ Format CRM recentré sur ces 3 éléments.

---

## QUESTIONS OUVERTES (à clarifier lors de futures sessions)

1. **Prospects sans site parmi les 11 qualifiés actuels** : Osio Paysagiste, Valente SAS, Ducret Bois, CYM, ARTI-MENUISERIE, Entreprise Romulus, Garage Chêne, Garage du Chater → ces 8 prospects ont été qualifiés sous les anciennes règles (avant R5). À revalider avec Yanis avant de les prospecter.
2. **Seuil exact "3 axes flagrants"** : à confirmer sur les prochains cas. Est-ce que 2 axes très graves (ex: aucun mobile + aucune photo) valent 3 axes moyens ?
3. **Poids exact de l'image de marque** : intégré dans Écart Site/Standing (0-50 pts V4), à affiner selon les prochains feedbacks.
4. **Migration Supabase** : colonnes `visual_note` et `site_date` déjà ajoutées ✅.

---

## RÈGLES STABLES — NE PAS REMETTRE EN QUESTION SANS FEEDBACK EXPLICITE

| Règle | Description | Date de validation |
|---|---|---|
| R1 — Fonctionnel ≠ Suffisant | Un site fonctionnel peut être moche et ne pas convertir. L'esthétique compte autant que les fonctionnalités. | 25/02/2026 |
| R2 — Exception B2B Image de Marque | B2B industriel autorisé si site existant + effort contenu visible + taille significative. Angle = image de marque. | 25/02/2026 |
| R3 — Gate 3 : 3 axes flagrants minimum | Si < 3 axes d'amélioration flagrants sur le site, le prospect n'est psychologiquement pas prêt à payer. STOP. | 25/02/2026 |
| R4 — Bon site = NON QUALIFIÉ | Un site moderne, propre, professionnel = non qualifiable même avec fort standing et fort CA. | 25/02/2026 |
| R5 — Sans site = Exclu (sauf métiers d'appel) | Aucun site = exclusion automatique SAUF métiers d'appel (R5b). | 26/02/2026, révisé 27/02/2026 |
| R5b — Exception métiers d'appel | Garages, plombiers, serruriers, artisans BTP sans site = GARDER. Un site augmenterait drastiquement leurs ventes. Angle = "Création site". | 27/02/2026 |
| R6 — Site 404 = à vérifier | Métiers d'appel + 404 = GARDER obligatoirement (prospect en or). Autres métiers : exclusion uniquement si preuve concrète d'abandon prolongé. | 26/02/2026, révisé 27/02/2026 |
| R7 — WebFetch obligatoire | Tout prospect avec un site doit être visité via WebFetch avant tout scoring. Évaluation visuelle = 50% de la décision. | 26/02/2026 |
| Gate 2 = 150k€ | Seuil CA binaire, zéro points de scoring | 25/02/2026 |
| Écart Site/Standing = 50 pts (V4) | Dimension principale, inclut esthétique + image de marque. Anciennement 40 pts. | 26/02/2026 |
| Mode écho = SUPPRIMÉ | Cause racine de tous les faux positifs. Ne jamais réactiver sans revoir la visite WebFetch. | 26/02/2026 |
| R8 — Design ≠ axe valide | Le design subjectif (couleurs, esthétique) n'est PAS un axe. Vrais axes = 404, responsive, CTA cassé, site 1-2/5. | 27/02/2026 |
| R9 — Site ≥ 3/5 = preuves obligatoires | Si note ≥ 3/5, qualifier SEULEMENT avec preuves techniques (404, CTA cassé, responsive, friction). | 27/02/2026 |
| R10 — CTA défaillant = axe majeur | CTA absent/cassé/formulaire daté = vrai axe. Peut sauver un site 4+/5. | 27/02/2026 |
| R11 — Copyright 2025+ = STOP | Site avec copyright 2025-2026 = refait récemment = ÉLIMINER direct. | 27/02/2026 |
| R12 — Vérifier activité réelle | Toujours confirmer l'activité sur le site vs description Google/Pappers. | 27/02/2026 |
| R13 — Réalisations/certifications/SEO ≠ axes | Ces éléments seuls ne sont pas des axes. Valides seulement en complément d'un vrai axe technique. | 27/02/2026 |

---

## SESSION DOUBLE-CHECK — Batch 1-2 (01/03/2026)

### Corrections Yanis — Batch 1 (#1-15)
| Prospect | Notre verdict | Verdict Yanis | Cause |
|---|---|---|---|
| Charroin Toitures | QUALIFIÉ (85) | DISQUALIFIÉ | Site fonctionne (pas de 404), notre Chrome avait un bug |
| Echo Garage | QUALIFIÉ (82) | DISQUALIFIÉ | Aucune envie de croissance — pas de site ≠ pas envie de digital |
| La Rhodanienne | QUALIFIÉ (80) | DISQUALIFIÉ | Trop gros, ne vont pas se laisser convaincre |
| Smile Cube | QUALIFIÉ | DISQUALIFIÉ | Niche dentiste exclue + site correct |
| Lyon Créateurs Ext. | QUALIFIÉ (78) | DISQUALIFIÉ | Site magnifique (notre évaluation visuelle était fausse) |
| Jury et Fils (76) | QUALIFIÉ (76) | DISQUALIFIÉ | Pas d'axes MAJEURS — design ≠ axe suffisant |
| SLDC | QUALIFIÉ (75) | DISQUALIFIÉ | One-page suffit pour les démolisseurs |
| SABEKO | QUALIFIÉ (77) | ✅ CONFIRMÉ | Site daté très moche = énorme écart |
| ARTI-MENUISERIE | QUALIFIÉ (77) | ✅ CONFIRMÉ | Signal de croissance fort |
| Electriklim | QUALIFIÉ (75) | ✅ CONFIRMÉ | 404, métier d'appel = prospect en or |

### Règles extraites — Batch 1
| Règle | Description | Date |
|---|---|---|
| R16 — Axes MAJEURS obligatoires | Le service porte d'entrée = vendre un site pour des axes d'amélioration MAJEURES. Design seul ≠ suffisant. | 01/03/2026 |
| R17 — One-page peut suffire | Certaines niches (démolition, TP, etc.) n'ont pas besoin de plus qu'un one-page. Ne pas qualifier juste parce que "site basique". | 01/03/2026 |
| R18 — Trop gros sans site = pas intéressé | Entreprise >2M€ CA sans site = signe qu'ils n'ont pas envie de digital, pas qu'ils ont besoin d'aide. | 01/03/2026 |
| R19 — Dentiste = niche exclue | Ajout aux niches exclues (boulangeries, coiffeurs, cafés/bars, petits commerces, dentistes). | 01/03/2026 |
| R20 — Classement Google 2e page = axe majeur | Pour les métiers concurrentiels (plombiers, électriciens, artisans d'appel), être en 2e page Google = axe majeur. | 01/03/2026 |

### Règles CRM extraites — Session 01/03/2026
| Règle | Description | Date |
|---|---|---|
| R21 — CRM actionnable obligatoire | Le CRM DOIT être directement actionnable : cliquer → appeler → savoir quoi dire. 3 blocs : Contact (tél+dirigeant), Angles+Axes majeurs, Implication (concurrent ou fait personnalisant). | 01/03/2026 |
| R22 — Jamais injecter sans téléphone | Ne JAMAIS injecter un prospect dans le CRM sans au minimum un numéro de téléphone + nom du dirigeant. | 01/03/2026 |
| R23 — Synchronisation permanente | Vérifier concordance Supabase ↔ CRM à CHAQUE fin de session. Signaler immédiatement tout écart, doublon, ou accumulation. | 01/03/2026 |
| R24 — Double-check systématique | TOUT prospect doit passer le double-check avant d'être considéré comme définitivement validé. Tag ✅ DOUBLE-CHECK obligatoire. | 01/03/2026 |

---

## REVUE INCERTAINS — Batch moitié 1 (#1-20) (01/03/2026)

### Contexte
Yanis a reviewé les 20 premiers prospects incertains (sur 43 total). Verdicts donnés un par un avec justifications détaillées.

### Résultat : 9 qualifiés / 8 disqualifiés / 2 liens cassés / 1 non mentionné (#18 Orakci)

**✅ QUALIFIÉS (9)**
| Prospect | Raison Yanis |
|---|---|
| ATS Carrosserie | Sans site, carrossier établi, prospect valide (R5b) |
| IPEL Fluides | SSL cassé = erreur technique flagrante |
| STPML | Sans site, terrassement VRD, prospect valide (R5b) |
| 2B Construction Bois | Site ©2026 MAIS tellement moche → exception R11. Accroche concurrents+structuration+CTA |
| Entreprise Bouvard | Même approche que 2B — récent mais mal structuré |
| SLPIB | 8.6M€ CA avec site nul = écart maximal. "C'est vraiment n'importe quoi" |
| ECEC | Yanis "l'aurait pas qualifié" mais l'accroche proposée l'a convaincu |
| Garage du Sud-Est | Déjà validé sur autre PC (vérifier doublon CRM) |
| MG BAT | Qualifié directement |

**❌ DISQUALIFIÉS (8)**
| Prospect | Raison Yanis |
|---|---|
| BGP Plomberie | "Site très beau, pas d'axe" (R4) |
| COIRO TP | "2026 en bas, c'est mort" (R11) — erreur d'analyse initiale |
| KD Rénov | CTA bourré, cohésion couleurs, "ils n'ont pas besoin" |
| Curtet et Blazy | "Depuis 2004, il aurait déjà eu un site" (R18 confirmé) |
| CTM Bire et Fils | CTA présent, air récent, "on ne qualifie pas" |
| PERRIN Paysage | Pas d'axe majeur |
| Jean Rivière | "Pas d'axe majeur, inaccessible" |
| Delabre Bento | Non qualifié par Yanis |

**⏸️ À VÉRIFIER (liens cassés)**
| Prospect | Résultat vérification |
|---|---|
| Chauffage 2000 | URL corrigée : chauffage-2000.com (pas chauffage2000.fr) |
| BFE Rénovations | URL corrigée : bferenovation.com (pas bfe-renovations.fr) |

### Règles créées/mises à jour

| Règle | Description | Date |
|---|---|---|
| R25 — Accroche = 4e bloc CRM | Phrase concrète et factuelle que Yanis dit au téléphone. Obligatoire dans chaque injection CRM. | 01/03/2026 |
| R26 — Templates d'accroches | 5 types selon le prospect : A (récent+moche), B (sans site), C (ancien+gros CA), D (erreur technique), E (template générique). | 01/03/2026 |
| R27 — Arguments factuels uniquement | "On ne peut pas critiquer trop sur le design" — Valentin/coach. Toujours des problèmes concrets, pas des avis subjectifs. | 01/03/2026 |
| R11 exception | ©2026 MAIS site tellement moche que l'écart est flagrant → GARDER. Cas : 2B Construction Bois. | 01/03/2026 |
| R18 confirmé | Curtet et Blazy (serrurier depuis 2004 sans site) = "il aurait déjà eu un site" → pas intéressé. | 01/03/2026 |

### Enseignements clés — Revue incertains Batch 1

1. **L'accroche fait la différence** : ECEC (#12) aurait été disqualifié sans l'accroche proposée → Yanis a changé d'avis grâce à l'angle d'attaque bien formulé
2. **Les arguments factuels > design** : Yanis insiste que "design" seul ne convainc pas, il faut des problèmes concrets (CTA, structure, temps de chargement)
3. **Exception R11 possible** : un site ©2026 peut être qualifié s'il est tellement moche que l'écart est flagrant (pas de CTA, mal structuré, trop de texte)
4. **Les templates d'accroches permettent l'automatisation** : Yanis veut que les accroches deviennent semi-automatiques selon le type de prospect
5. **Le CRM doit toujours avoir l'accroche** : c'est ce que Yanis lit AVANT d'appeler

---

## REVUE INCERTAINS — Batch 2 (#21-42) (02/03/2026)

### Contexte
Yanis a revu les prospects 21 à 42 du fichier 38_Incertains. En plus des verdicts, il a apporté 2 changements majeurs de stratégie sur les cibles.

### Verdicts
**QUALIFIÉS (4 + 2 déjà qualifiés) :**
- #21 Brocard Durand → QUALIFIÉ (CTI faibles, potentiel SEO, images lentes, pas de portfolio)
- #25 Entreprise Mancini → QUALIFIÉ (pas responsive = 70% perte clientèle mobile, faute d'orthographe)
- #26 Sallamand Paysagiste → QUALIFIÉ (pas responsive = axe majeur, structure mauvaise, manque images)
- #29 BCCA2 → QUALIFIÉ (déjà qualifié — photos personnes au lieu de réalisations bâtiment)
- #24 R.E.V.E. Paysagistes → déjà qualifié dans Supabase (confirmé)
- #31 Yakarrosserie → déjà qualifié dans Supabase (mais garage = à reclasser per R29?)

**DISQUALIFIÉS (15) :**
- #23 Matthieu Bertrand Plomberie → artisan plombier = client trop dur à éduquer (feedback coach Valentin)
- #28 EGEI Électricité → disqualifié par Yanis
- #30 Lyonnaise Renovation → disqualifié
- #32 CEDDIA TP → site déjà très clean (R4)
- #33 Idelec Plus → site très bien avec blogs, pas besoin (R4)
- #34 Garage Des Monts D'Or → garage + site OK (R29 + R4)
- #35 SAONE DECOR → disqualifié
- #36 Decibois → très belles images, pas besoin (R4)
- #37 Les Règles de l'Art → pas besoin
- #38 AMB Propreté → bon site
- #39 Corpet Couvreur → disqualifié
- #40 Dupuis Serrurerie 3D Serrure → disqualifié
- #41 ECM PERFORMANCE 69 → disqualifié
- #42 MB MAÇONNERIE → disqualifié
- #43-45 : 3 à purger (coiffeur, resto, SECP non visité)

**NON MENTIONNÉS :**
- #18 Orakci Façade — jamais mentionné dans batch 1 ni batch 2
- #22 Decock Audric — qualifié par Yanis PUIS artisans serruriers déclarés cible à éviter → incohérence à clarifier
- #27 Soly Renov Batiment — non mentionné dans le flux de verdicts

### Nouvelles règles / changements stratégiques majeurs
**R29 — Artisans métiers d'appel = cible à éviter (02/03/2026)**
- Source : Feedback coach Valentin, confirmé par expérience Yanis
- Raison : « Tous les métiers artisanaux (serrurier, plombier...) ils sont énormément sur les chantiers, ils sont ranchons, ils savent pas ce qu'ils ratent. Des clients à éduquer énormément. Pas la meilleure cible. »
- ⚠️ CONTRADICTION AVEC R5b (sans site artisan = GARDER) → à clarifier avec Yanis

**R30 — Garages = cible à éviter (02/03/2026)**
- Source : Feedback coach Valentin
- Raison : « Les garages travaillent déjà avec des assurances, ils ont aucun besoin de site internet. »
- Impact : tous les garages qualifiés à reclasser (Yakarrosserie, Garage du Sud-Est, Garage Chêne, Garage du Chater, Garage Reynard, Garage Sardellitti, CDA Auto, Charly Automobiles, etc.)

**Liste cibles préférentielles / à éviter → à formaliser avec Yanis**

### Incident session autre ordinateur (02/03/2026)
- Session `dfb7c715` lancée sur un autre PC avec le même dossier
- R28 (téléphone obligatoire) n'était pas dans les règles de cette instance
- Résultat : 69 prospects injectés dont 25 qualifiés, **TOUS sans téléphone**
- Contient aussi des garages/carrosseries/plombiers (niches maintenant à éviter)
- → R28 renforcée en BLOQUANT ABSOLU dans SKILL.md et CLAUDE.md

### Apprentissages clés
1. **La responsivité est un axe majeur** : "pas responsive = 70% perte clientèle" — argument factuel très puissant pour l'accroche
2. **Les photos de personnes au lieu de réalisations** : pour le BTP, c'est un argument tueur (cas BCCA2)
3. **Le coach est la source de vérité sur les niches** : ses retours terrain (artisans ranchons, garages assurances) changent la stratégie entière
4. **R28 doit être impossible à oublier** : renforcée ⛔ BLOQUANT ABSOLU après l'incident

---

## FORMAT D'ENTRÉE POUR FUTURES CORRECTIONS

Quand Yanis ou le coach donnent un feedback, l'enregistrer ainsi :

```
## Date — [Nom du prospect]
Notre verdict : [QUALIFIÉ/INCERTAIN/NQ] ([score]/100)
Verdict coach : [QUALIFIÉ/NQ]
Argument coach : "[texte exact si possible]"
Cause de l'erreur : [description]
Règle créée/modifiée : [référence dans SKILL.md]
```
