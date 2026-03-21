# STRATEGY_V1.md — Plan technique complet de l'automatisation
> Dernière mise à jour : 9 mars 2026 — V5.3
> Complément de SKILL.md — détails techniques, Swarm V4.3, injection CRM, anti-fuite

---

## SUPABASE — CREDENTIALS (CONFIGURÉ ✅)

| Paramètre | Valeur |
|---|---|
| Project ID | `ngewdelqytymolemrkcc` |
| URL | `https://ngewdelqytymolemrkcc.supabase.co` |
| Anon Key | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5nZXdkZWxxeXR5bW9sZW1ya2NjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE4NTQxMzcsImV4cCI6MjA4NzQzMDEzN30.EKrGc75ZvpfAP9_s0HwFdWEZyIq-lLvNDqeAiNFKVhs` |
| Schéma SQL | ✅ Déployé (migrations : schema_qualification_v1, add_candidate_status_and_phase, add_dirigeant_contact_columns) |
| Tables | `sessions`, `prospects`, `scanned_urls`, `zones_coverage` |
| Organisation | `oejekjxxcpodnbnlqiuj` |

---

## ARCHITECTURE V5.3 — VUE D'ENSEMBLE

```
[Déclenchement]
  ├── Manuel : Yanis tape "session X" (X = quota callable 06/07)
  └── Planifié : shortcut Cowork 8h00 lun-ven (à créer)
        ↓
[Miggy (Claude) — moteur de qualification]
  │
  ├── 1. Vérifie pool candidats Supabase (R29)
  │     └── Pool > 0 ? → Skip Phase 1, piocher directement
  │     └── Pool = 0 ? → Phase 1 sourcing
  │
  ├── 2. SWARM V4.3 — agents parallèles (voir détail ci-dessous)
  │     ├── Agent CHECKPOINT : injecte chaque candidat Supabase immédiatement
  │     ├── Agents QUALIFICATION : pré-filtre → 4 Gates → scoring
  │     └── Agent CRM : injection si phone_mobile 06/07
  │
  ├── 3. Boucle R33 : continue tant que quota callable < X
  │     └── Callable = qualifié + phone_mobile 06/07
  │     └── Qualifiés sans 06/07 → Supabase only (ne comptent pas)
  │
  └── 4. Fin de session
        ├── Résumé : X/X callable → CRM, Y sans 06/07 → Supabase only
        ├── Concordance Supabase ↔ CRM
        └── Email notification → yabouridasannier@gmail.com (si planifié)
```

---

## SWARM V4.3 — WORKFLOW MULTI-AGENTS (6 PHASES)

### Principes
- **Sous-agents (sub-agents)** = agents lancés en parallèle via l'outil Agent pour traiter plusieurs prospects simultanément
- **Gain estimé** : ~65% de temps vs séquentiel
- **Anti-fuite** : chaque candidat est injecté Supabase AVANT traitement (status `candidate`, phase `found`)
- **Colonne `phase`** : trace la progression → `found → pre_analyzed → chrome_visited → scored → crm_injected`

### Phase 1 — Sourcing (skip si pool > 0 — R29)

**Vérification pool :**
```sql
SELECT COUNT(*) FROM prospects WHERE final_status = 'candidate' AND phase = 'found';
```
- Pool > 0 → passer directement Phase 2
- Pool = 0 → sourcer via Google Maps / Pages Jaunes / scraper

**Anti-doublon zones (R30) :**
```sql
SELECT DISTINCT city FROM prospects ORDER BY city;
```
Ne JAMAIS sourcer une ville déjà présente.

**Agent CHECKPOINT** : chaque entreprise trouvée → INSERT Supabase immédiat :
```sql
INSERT INTO prospects (session_id, company_name, city, website_url, final_status, phase)
VALUES ($session_id, $name, $city, $url, 'candidate', 'found');
```

### Phase 2 — Pré-analyse (parallélisable)

Lancer N sous-agents en parallèle (typiquement 3-5 selon contexte).
Chaque agent prend un lot de candidats et effectue :
1. Vérification anti-doublon (URL, SIRET, fuzzy name+city)
2. Pré-filtre : site existe ? Niche exclue ? Copyright récent ?
3. Recherche téléphone 06/07 (Google Maps, Pages Jaunes, pappers, societe.com, LinkedIn)
4. UPDATE phase → `pre_analyzed`

```sql
UPDATE prospects SET phase = 'pre_analyzed', phone_mobile = $phone, phone_main = $main
WHERE id = $id;
```

### Phase 3 — Visite site (WebFetch obligatoire — R7)

Pour chaque candidat pré-analysé :
1. WebFetch du site → évaluation visuelle 1-5
2. Check copyright pied de page
3. Identification CTA, responsive, erreurs 404, temps chargement
4. UPDATE phase → `chrome_visited`

```sql
UPDATE prospects SET phase = 'chrome_visited' WHERE id = $id;
```

### Phase 4 — Gates + Scoring

Passage séquentiel des 4 Gates binaires (Gate 0 → 1 → 2 → 3).
Premier échec = STOP → `final_status = 'disqualified'`.

Si 4 Gates passées → scoring V4 (100 pts) :
- Écart Site/Standing : 0-50
- Besoins digitaux : 0-25
- Croissance : 0-15
- Contactabilité : 0-10

UPDATE Supabase :
```sql
UPDATE prospects SET
  gate_0 = $g0, gate_1 = $g1, gate_2 = $g2, gate_3 = $g3,
  score_pe = $pe, score_need = $need, score_growth = $growth, score_contact = $contact,
  final_status = CASE
    WHEN $total >= 70 THEN 'qualified'
    WHEN $total >= 55 THEN 'uncertain'
    ELSE 'disqualified'
  END,
  phase = 'scored',
  elimination_gate = $elim_gate,
  elimination_reason = $elim_reason,
  ca_estimate = $ca, ca_proof_level = $ca_level
WHERE id = $id;
```

### Phase 5 — Enrichissement contact + CRM (R31)

Pour chaque qualifié (≥ 70/100) :
1. Recherche dirigeant : pappers, societe.com, LinkedIn
2. Remplir colonnes structurées : `contact_name`, `phone_mobile`, `phone_main`, `linkedin_url`, `email`
3. Choix accroche (template A-E — voir SKILL.md)
4. Rédaction `axes_amelioration` (numérotés, factuels)

**Routing R31 :**
- `phone_mobile` = 06/07 → **Supabase + CRM** (phase → `crm_injected`)
- Pas de 06/07 → **Supabase only** (phase reste `scored`)

### Phase 6 — Vérification R33 + Concordance

**Check quota callable :**
```sql
SELECT COUNT(*) FROM prospects
WHERE session_id = $session_id
  AND final_status = 'qualified'
  AND phone_mobile IS NOT NULL
  AND phone_mobile ~ '^0[67]';
```

- Quota atteint → FIN de session
- Quota non atteint + pool restant → retour Phase 2 avec nouveaux candidats
- Quota non atteint + pool vide → signaler à Yanis : "X/Y callable trouvés, pool vide"

**Concordance Supabase ↔ CRM :**
Vérifier que chaque qualifié avec `phone_mobile` 06/07 est bien présent dans le CRM.

**Résumé fin de session :**
```
Session [ID] terminée :
- X/X callable → CRM (objectif atteint / partiel)
- Y qualifiés sans 06/07 → Supabase only (machine secrétariat)
- Z disqualifiés / W incertains → Supabase
- Zones couvertes : [liste]
```

---

## REPRISE APRÈS SATURATION (context window)

Si la session est interrompue (saturation contexte, crash, timeout) :
```sql
SELECT phase, COUNT(*) FROM prospects
WHERE session_id = '[SESSION_ID]'
GROUP BY phase ORDER BY phase;
```

Reprendre là où ça s'est arrêté :
- `found` → reprendre Phase 2
- `pre_analyzed` → reprendre Phase 3
- `chrome_visited` → reprendre Phase 4
- `scored` → reprendre Phase 5
- `crm_injected` → déjà terminé

Zéro perte de données grâce à l'agent CHECKPOINT (Phase 1).

---

## CRM — INJECTION DIRECTE

**URL CRM :** https://structur-a-lead.vercel.app/leads
**Backend :** Supabase (`eywnzgsvrsxzahoiwnml.supabase.co`)
**Stage :** `PROSPECT_IDENTIFIE`

### Format notes CRM — 4 BLOCS

```
📞 CONTACT
Dirigeant : [Prénom Nom]
Tél : [06/07...]
LinkedIn : [URL]
Email : [email]

🎯 ANGLES + AXES
Angle : [Refonte / Création site / Multi / Image de Marque / SEO]
Axes :
1. [Axe factuel 1]
2. [Axe factuel 2]
3. [Axe factuel 3]

📣 ACCROCHE
[Template A/B/C/D/E personnalisée]

🔗 IMPLICATION
- Concurrent mieux positionné : [nom]
- Fait marquant : [détail]
- CA : [montant] ([Confirmé/Probable/Déduit])
- SIRET : [numéro]
```

### Injection via Chrome JS (API REST)

Le CRM tourne sur Supabase. L'injection se fait via script JS exécuté dans le navigateur Chrome (outil computer) sur la page du CRM. La clé anon est extraite dynamiquement du bundle JS via regex :
```
eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+
```

⚠️ Le nom du bundle JS change à chaque redéploiement Vercel — toujours extraire dynamiquement.

**Règle R31 absolue** : JAMAIS d'injection CRM sans `phone_mobile` 06/07 du dirigeant identifié.

---

## ANTI-DOUBLONS — 3 NIVEAUX

Avant d'analyser un prospect, vérifier dans cet ordre :

1. **URL exacte** → `SELECT 1 FROM scanned_urls WHERE url = $url`
2. **SIRET** → `SELECT 1 FROM prospects WHERE siret = $siret`
3. **Fuzzy name+city** → `SELECT 1 FROM prospects WHERE similarity(company_name, $name) > 0.9 AND city = $city`

Si trouvé à n'importe quel niveau : SKIP. Couvre aussi les prospects éliminés — on ne les repasse JAMAIS.

---

## GESTION DES ERREURS (run autonome)

| Situation | Comportement |
|---|---|
| Site web inaccessible (403/timeout) | Passer au suivant, noter `final_status='error'` |
| 3 échecs consécutifs de recherche | Générer rapport partiel et notifier |
| Prospect éliminé Gate 0 ou 1 | Inscrire en base avec `elimination_gate` + continuer |
| Score < 70 (incertain ou non qualifié) | Inscrire en base, pas de CRM |
| Pool épuisé avant quota callable | Signaler : "X/Y callable, pool vide" |
| Saturation contexte | Reprendre via requête phase (voir section ci-dessus) |

**Principe clé : le run ne doit JAMAIS bloquer et ne doit JAMAIS nécessiter l'intervention de Yanis.**

---

## SUPABASE — SCHÉMA SQL (RÉFÉRENCE)

```sql
-- Extension pour matching flou
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Sessions de qualification
CREATE TABLE sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  started_at TIMESTAMPTZ DEFAULT NOW(),
  ended_at TIMESTAMPTZ,
  zone TEXT,
  prospects_scanned INTEGER DEFAULT 0,
  prospects_qualified INTEGER DEFAULT 0,
  status TEXT DEFAULT 'running'
);

-- Tous les prospects analysés
CREATE TABLE prospects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id UUID REFERENCES sessions(id),
  company_name TEXT NOT NULL,
  city TEXT,
  postal_code TEXT,
  siret VARCHAR(14),
  website_url TEXT,
  -- Coordonnées structurées V5.2
  phone_main TEXT,
  phone_mobile TEXT,
  email TEXT,
  contact_name TEXT,
  linkedin_url TEXT,
  accroche TEXT,
  axes_amelioration TEXT,
  -- Qualification
  gate_0 BOOLEAN,
  gate_1 BOOLEAN,
  gate_2 BOOLEAN,
  gate_3 BOOLEAN,
  elimination_gate INTEGER,
  elimination_reason TEXT,
  -- Scoring
  score_pe INTEGER,
  score_need INTEGER,
  score_growth INTEGER,
  score_contact INTEGER,
  total_score INTEGER GENERATED ALWAYS AS (
    COALESCE(score_pe,0) + COALESCE(score_need,0) +
    COALESCE(score_growth,0) + COALESCE(score_contact,0)
  ) STORED,
  -- Statut
  final_status TEXT CHECK (final_status IN ('candidate','qualified','uncertain','disqualified','error')),
  phase TEXT DEFAULT 'found',
  crm_status TEXT DEFAULT 'new',
  -- Données économiques
  ca_estimate TEXT,
  ca_proof_level TEXT,
  -- Angle
  angle TEXT,
  -- Meta
  created_at TIMESTAMPTZ DEFAULT NOW(),
  docx_generated BOOLEAN DEFAULT FALSE,
  notes TEXT
);

-- URLs déjà scannées
CREATE TABLE scanned_urls (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  url TEXT NOT NULL,
  domain TEXT,
  prospect_id UUID REFERENCES prospects(id),
  scanned_at TIMESTAMPTZ DEFAULT NOW(),
  CONSTRAINT unique_url UNIQUE (url)
);

-- Zones géographiques
CREATE TABLE zones_coverage (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  zone_name TEXT NOT NULL UNIQUE,
  commune_code TEXT,
  first_scanned_at TIMESTAMPTZ,
  last_scanned_at TIMESTAMPTZ,
  total_scanned INTEGER DEFAULT 0,
  total_qualified INTEGER DEFAULT 0,
  fully_covered BOOLEAN DEFAULT FALSE
);

-- Index
CREATE INDEX idx_prospects_siret ON prospects(siret) WHERE siret IS NOT NULL;
CREATE INDEX idx_prospects_status ON prospects(final_status);
CREATE INDEX idx_prospects_company ON prospects USING gin(company_name gin_trgm_ops);
CREATE INDEX idx_scanned_urls_domain ON scanned_urls(domain);
CREATE INDEX idx_prospects_callable ON prospects(final_status, phone_mobile);
```

---

## ORDRE DES ZONES — SÉQUENCE DE COUVERTURE

1. Lyon 3e (Part-Dieu) · 2. Lyon 7e (Gerland) · 3. Villeurbanne · 4. Lyon 6e · 5. Lyon 2e (Confluence)
6. Bron · 7. Vénissieux · 8. Caluire-et-Cuire · 9. Saint-Priest · 10. Décines-Charpieu
11. Lyon 1er · 12. Lyon 4e/5e · 13. Tassin-la-Demi-Lune · 14. Francheville · 15. Écully
16. Oullins/Pierre-Bénite · 17. Meyzieu · 18. Mions · 19. Corbas · 20. Saint-Fons
... (continuer avec les 39 communes restantes)

⚠️ Toujours vérifier R30 (`SELECT DISTINCT city FROM prospects`) avant de sourcer une zone.

---

## PROMPT SYSTÈME DU SHORTCUT (pour création planifiée)

```
Tu es Miggy, expert en qualification de prospects B2B pour Yanis (Lyon).
Objectif : qualifier X prospects CALLABLE (06/07 dirigeant) — R33.

CONTEXTE :
- Playbook : SKILL.md (V5.3) + STRATEGY_V1.md
- Supabase connecté pour anti-doublons et stockage
- Zone : Aire métropolitaine Lyon (59 communes)

PROCESSUS :
1. Lire SKILL.md + STRATEGY_V1.md
2. Vérifier pool candidats (R29) — skip Phase 1 si pool > 0
3. Vérifier zones couvertes (R30)
4. Lancer Swarm V4.3 (sous-agents parallèles)
5. Pour chaque candidat : pré-filtre → 4 Gates → scoring → enrichissement contact
6. Routing : 06/07 → Supabase + CRM / sans 06/07 → Supabase only
7. Boucle R33 : continuer tant que quota callable non atteint
8. Résumé fin de session + concordance Supabase↔CRM

RÈGLES ABSOLUES :
- Jamais inventer de données (anti-hallucination)
- Tout étiqueter Confirmé / Probable / Déduit
- WebFetch obligatoire pour chaque site (R7)
- En cas d'erreur : continuer, ne pas s'arrêter
- CRM = UNIQUEMENT si 06/07 dirigeant (R31)
- Session X = X callable, pas X qualifiés total (R33)
```

---

## ESTIMATION COÛT ET PLAN

| Fréquence | Runs/mois | Tokens estimés/mois | Plan recommandé |
|---|---|---|---|
| 1x/semaine (test) | 4 | ~2M tokens | Pro (20€) suffisant |
| 3x/semaine | 12 | ~6M tokens | Pro limite, Max conseillé |
| 5x/semaine (cible) | 20 | ~10M tokens | Max (~100€) nécessaire |
