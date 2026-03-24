# PROMPT — Génération d'images Vinted (méthode M22)
*Usage : envoyer ce prompt à Claude ou Gemini avec la photo du produit fournisseur*

---

## RÈGLE ABSOLUE
L'image générée doit correspondre EXACTEMENT au produit réel du fournisseur.
- Même couleur
- Même forme
- Même nombre de boutons, fermetures, poches
- Même ceinture (ou absence de ceinture)
- Même longueur
- AUCUN ajout, AUCUNE modification du produit

---

## PROCESS EN 3 ÉTAPES

### Étape 1 — Tu reçois l'image du produit fournisseur
Analyse le produit en détail :
- Type de vêtement (robe, veste, manteau, etc.)
- Couleur exacte
- Matière apparente
- Détails (boutons, ceinture, col, poches, coutures, motifs)
- Longueur (court, mi-long, long)

### Étape 2 — Tu génères le prompt Gemini
Format du prompt à envoyer à Gemini :

```
Génère une photo réaliste d'une [PERSONA] portant ce vêtement exactement tel qu'il est.

Le vêtement :
- [TYPE] [COULEUR] [MATIÈRE]
- [DÉTAIL 1]
- [DÉTAIL 2]
- [DÉTAIL 3]
- Longueur : [LONGUEUR]

La personne :
- [DESCRIPTION DU PERSONA selon le compte Vinted]
- Pose naturelle, comme un selfie miroir ou une photo prise par un ami
- PAS de pose de mannequin catalogue
- PAS de fond studio blanc

Cadrage : de la mâchoire jusqu'à mi-genou.

Style : photo iPhone, lumière naturelle, intérieur cosy ou extérieur urbain.
Ambiance Vinted — authentique, pas professionnel.

IMPORTANT : ne modifie RIEN au vêtement. Pas d'ajout de ceinture, pas de changement de couleur, pas de modification de longueur. Le produit doit être identique à la photo de référence.
```

### Étape 3 — Tu fournis aussi

**Titre Vinted :**
[Titre optimisé avec mots-clés que les acheteuses tapent vraiment]
Max 5 mots. Pas de majuscules excessives.

**Description Vinted :**
[3-4 lignes max. Ton personnel, pas catalogue.]
- Taille
- Matière
- État
- Ce qui rend l'article unique
- "N'hésitez pas à me poser des questions 💬"

**Hashtags :**
#[niche] #[type] #[couleur] #[style] #[saison]
(5 hashtags max, pertinents)

---

## PERSONAS PAR COMPTE

| Compte | Persona | Description pour le prompt |
|--------|---------|---------------------------|
| Eva | À définir | [à compléter quand le persona est fixé] |
| Compte 3 | À définir | [à compléter] |
| Compte 4 | À définir | [à compléter] |

---

## EXEMPLES DE CE QU'IL NE FAUT PAS FAIRE

❌ Produit fournisseur = veste sans ceinture → Image IA = veste AVEC ceinture → INTERDIT
❌ Produit fournisseur = robe courte → Image IA = robe longue → INTERDIT
❌ Produit fournisseur = bleu marine → Image IA = bleu ciel → INTERDIT

## CE QU'IL FAUT FAIRE

✅ Produit fournisseur = veste bordeaux sans ceinture → Image IA = même veste bordeaux sans ceinture, portée par le persona dans un cadre naturel
✅ Sublimer l'éclairage, le cadrage, l'ambiance — PAS le produit

---

*Source : méthode M22 — persona Pinterest + article fournisseur = image fidèle portée*
