# Process DR1 — Audit personnalisé Logipro Web (2 pages)

## Contexte
Un DR1 est un document Canva de 2 pages envoyé à chaque prospect AVANT le premier rendez-vous (R1).
Il est basé sur un template de base, personnalisé par prospect.

---

## Infos agence (à injecter dans chaque DR1)
- **Nom** : Logipro Web
- **Email** : logipro.contact.client@gmail.com
- **Téléphone** : 07 49 25 25 93
- **Site** : logipro-web.fr

---

## Rendez-vous
### Lundi 9 mars 2026
| Heure | Prospect |
|-------|----------|
| 10h30 | Senvenhaven |
| 11h00 | Lionkey |
| 11h30 | Benyahia |
| 16h00 | Leroy T2R Conciergerie |
| 17h30 | Prospect téléphone — 06 06 44 92 06 |

### Mardi 10 mars 2026
| Heure | Prospect |
|-------|----------|
| 11h00 | Alex |
| 11h45 | Alexandre SMA |
| 13h30 | Aleyo |
| 15h30 | M. Bérenger |

---

## Zones à personnaliser dans chaque DR1

### Page 1
| Zone | Contenu | Source |
|------|---------|--------|
| **Titre / Hook** | Accroche personnalisée avec **nom du dirigeant + URL du site**. Ex : "M. Aurélien, 3 raisons pour lesquelles lesjardinsdaurelien.com vous fait perdre des candidats qualifiés." | Audit site + CRM |
| **Image** | Capture d'écran du site web actuel du prospect (zone image en haut à droite) | Screenshot via mshots ou browser |
| **"POUR UN (RÉSULTAT VOULU) OPTIMAL SUR (OBJECTIF)"** | Doit contenir le **nom de l'entreprise** et l'**objectif métier précis**. Ex : "Pour que Les Jardins d'Aurélien recrute ses prochains paysagistes qualifiés, votre futur candidat doit trouver sur votre site :" | CRM + secteur |
| **Conseil 1, 2, 3** (titre + description max 2 phrases) | Chaque description adopte la **perspective du candidat/client** : "Votre futur collaborateur cherche X... il arrive sur votre site... il ne trouve pas X... il part." | Réflexion secteur + audit site |

### Page 2
| Zone | Contenu | Source |
|------|---------|--------|
| **Image PC** | Screenshot du site du prospect inséré dans/sur le PC mockup | mshots URL |
| **Constat 1, 2, 3** ("VOTRE SITE WEB AUJOURD'HUI") | Max 2 phrases, **angle ROI** : ce que le prospect PERD aujourd'hui. Ex : "Votre futur candidat arrive, ne voit rien, appelle votre concurrent." | CRM + audit site |
| **Bloc agence** | Adapter le secteur. Format : "NOUS SOMMES UNE AGENCE WEB SPÉCIALISÉE DANS [SECTEUR]." | Secteur CRM |
| **PLUS DE CONVERSIONS + PANIER MOYEN** | Descriptions courtes (1-2 phrases), orientées **résultat concret pour le prospect** | Secteur CRM |
| **Bonne nouvelle** | Mention du **nom du prospect** : "Bonne nouvelle [Prénom], tout ça se règle." | CRM |

### Fixe (ne pas changer)
- Section "LE SITE DOIT AUSSI" (4 points : Responsive, SEO, Rédigé, Performances)
- Structure et layout général

---

## ⚠️ Règles de rédaction (learnings du test)

### 1. Hyper-personnalisation obligatoire
- Le nom du dirigeant doit apparaître **au moins 2 fois** dans le document (hook + bonne nouvelle)
- Le nom de l'entreprise doit apparaître **au moins 3 fois**
- L'URL du site doit apparaître **au moins 1 fois**
- Le document doit sembler **écrit spécifiquement pour cette personne**, pas pour un secteur

### 2. Textes courts — max 2 phrases par description
- Titre constat/conseil : 4-6 mots max, tout en majuscules
- Description : **2 phrases maximum**, percutantes
- Supprimer tout remplissage générique

### 3. Perspective candidat/client (pas agence)
Raconter le parcours de la personne qui cherche :
> "Votre futur paysagiste tape 'paysagiste emploi Essonne' sur Google. Il clique sur votre site. Il ne trouve pas de page recrutement. Il clique sur 'Retour' et postule chez votre concurrent."

### 4. ROI visible partout
- Chaque constat doit montrer **ce que le prospect perd** (candidats, clients, chiffre d'affaires)
- Chaque conseil doit montrer **ce qu'il gagnera** concrètement
- Utiliser des chiffres quand possible (ex: "70% des visiteurs ne rappellent jamais", "3× plus de candidatures")

### 5. Images obligatoires
- **Page 1** (zone image haut droite) : screenshot du site du prospect
  - URL mshots : `https://s.wordpress.com/mshots/v1/[URL_ENCODÉE]?w=800&h=600`
  - Uploader via Canva MCP `upload-asset-from-url` → récupérer asset_id → `insert_fill`
- **Page 2** (zone PC mockup) : même screenshot ou focus sur défaut visible

---

## Workflow de production (par prospect)

1. **Lire le CRM** → aller dans Leads > colonne R1 > cliquer sur le lead > tout lire
2. **Lister les infos disponibles** :
   - Prénom/nom du dirigeant, nom entreprise, secteur, téléphone
   - URL site web
   - Axes majeurs / notes de l'appel de qualification
   - Objectif principal (recrutement, réservations, leads, ventes...)
3. **Rechercher ce qui manque sur Google** :
   - Site web du prospect → visite complète + screenshot
   - Google Maps / GMB (avis, photos, complétude)
   - LinkedIn si disponible
4. **Préparer le contenu personnalisé** :
   - Hook : "[Prénom], X raisons pour lesquelles [URL] vous fait perdre [résultat]..."
   - Phrase centrale : "Pour que [Nom entreprise] atteigne [objectif], votre futur [client/candidat] doit trouver sur votre site :"
   - 3 conseils : perspective du candidat/client, max 2 phrases chacun
   - 3 constats : angle ROI (ce que le prospect PERD), max 2 phrases chacun
   - "Bonne nouvelle [Prénom]..." + nom entreprise dans la suite
5. **Préparer les images** :
   - Screenshot via `https://s.wordpress.com/mshots/v1/[URL_ENCODÉE]?w=800&h=600`
   - Upload dans Canva → récupérer asset_id
6. **Dupliquer le template Canva** → personnaliser toutes les zones + insérer images
7. **Vérifier** → nommer le design "DR1 - [Nom prospect]" → passer au suivant

---

## Sources d'information
- **CRM** : https://structur-a-lead.vercel.app/leads (colonne R1)
- **Site web** de chaque prospect (recherche Google)
- **Google Maps** / fiche Google My Business
- **LinkedIn** de l'entreprise si disponible

---

## Statut de production
| Prospect | CRM OK | Site trouvé | GMB vérifié | DR1 créé |
|----------|--------|-------------|-------------|----------|
| Les Jardins d'Aurélien (test) | ✅ | ✅ | — | ✅ [DR1 - Les Jardins d'Aurélien](https://www.canva.com/design/DAHDLh9X8rQ/edit) |
| Senvenhaven | ⬜ | ⬜ | ⬜ | ⬜ Design: DAHDM5-KKTU |
| Lionkey (Dennis) | ⬜ | ⬜ | ⬜ | ⚠️ Sous-agent a prétendu terminer — À VÉRIFIER [Canva](https://www.canva.com/design/DAHDM1PdNVQ/edit) |
| Benyahia | ⬜ | ⬜ | ⬜ | ⬜ Design: DAHDM9sUwKc |
| Leroy T2R Conciergerie | ⬜ | ⬜ | ⬜ | ⬜ Design: DAHDM2DKEk8 |
| Prospect 06 06 44 92 06 | ⬜ | ⬜ | ⬜ | ⬜ Design: DAHDM-noVl0 |
| Alex | ⬜ | ⬜ | ⬜ | ⬜ Design: DAHDM-noVl0 |
| Alexandre SMA | ⬜ | ⬜ | ⬜ | ❌ Design DAHDM6ao-cE DÉTRUIT (ctrl+A hors text-edit) — À RECRÉER depuis template |
| Aleyo | ⬜ | ⬜ | ⬜ | ⬜ Design: DAHDMxrkJ3g |
| M. Bérenger | ⬜ | ⬜ | ⬜ | ⬜ Design: DAHDM2OoQtA |

## ⚠️ Notes techniques (learnings sessions précédentes)
- **JAMAIS Ctrl+A hors du mode text-edit** → sélectionne TOUT le canvas → Delete détruit tout
- **Méthode safe** : double-clic → triple-clic pour sélectionner → `type "texte"` directement
- **shift+R avec Caps Lock ON** = produit un "r" minuscule (inversion) → utiliser `type "R"` à la place
- **Ctrl+Z** ne récupère pas après une destruction massive (version history = Pro+ uniquement)
- **Template original** (Les Jardins d'Aurélien) : DAHDLh9X8rQ — NE PAS MODIFIER
- **Canva MCP** fonctionne pour les text edits via start-editing-transaction / perform-editing-operations / commit

## IDs des éléments Canva (identiques sur tous les designs dupliqués)
### Page 1
- Hook: `PB8QdG7R8jS24tsP-LBdv821znXNQkr9W-LBzML5NnwTpGYjM8`
- Phrase centrale: `PB8QdG7R8jS24tsP-LBPDZq4ZTZTbqwdh`
- Conseil 1 titre: `PB8QdG7R8jS24tsP-LBkH69DSY4qcycQL`
- Conseil 1 desc: `PB8QdG7R8jS24tsP-LBzR3cyqRz09Nv3B`
- Conseil 2 titre: `PB8QdG7R8jS24tsP-LBLJf9TlbKpNQ3sz`
- Conseil 2 desc: `PB8QdG7R8jS24tsP-LBK2b8kPkjd4rYy6`
- Conseil 3 titre: `PB8QdG7R8jS24tsP-LBM8WxFjwV7RHXPR`
- Conseil 3 desc: `PB8QdG7R8jS24tsP-LBM5YpBZwy08hxMb`

### Page 2
- Constat 1 titre: `PBPXNh4nFb4F83Ll-LBF3p3cs456flWPq-LBzLW02WhwrmG0Q9`
- Constat 1 desc: `PBPXNh4nFb4F83Ll-LBF3p3cs456flWPq-LB9q0c9DhZBrv8kf`
- Constat 2 titre: `PBPXNh4nFb4F83Ll-LBkhHZLjYByqgQ7V-LBHrLHLZH3ZskXrG`
- Constat 2 desc: `PBPXNh4nFb4F83Ll-LBkhHZLjYByqgQ7V-LBd2NZSMt6f5YSS6`
- Constat 3 titre: `PBPXNh4nFb4F83Ll-LB6QZqBJhTds8ZSJ-LBZfqS74zwPxkSmq`
- Constat 3 desc: `PBPXNh4nFb4F83Ll-LB6QZqBJhTds8ZSJ-LBBMhc0xl50gWV4W`
- Bonne nouvelle: `PBPXNh4nFb4F83Ll-LBHDZFRNCvkRhrc2`
- Bloc agence titre: `PBPXNh4nFb4F83Ll-LBf12DfRFPDGFkw9`
- Bloc agence desc: `PBPXNh4nFb4F83Ll-LBQ1g4jjSckz91w4`
- Visiteurs desc: `PBPXNh4nFb4F83Ll-LB8202ZzvYfqDSm0`
- Conversions desc: `PBPXNh4nFb4F83Ll-LBpswJv1h7KHkDww`
- Panier desc: `PBPXNh4nFb4F83Ll-LBvSHyC1xf8t1xDN`
- CTA bottom: `PBPXNh4nFb4F83Ll-LB4w2M8ZwfBnpQM3`
