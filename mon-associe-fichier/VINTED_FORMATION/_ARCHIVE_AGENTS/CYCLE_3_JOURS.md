# SYSTÈME CYCLE 3 JOURS — Méthode M22

*Documenté le 18 mars 2026*

---

## Principe fondamental

Chaque compte Vinted poste **5 annonces par jour**.
Toutes les 3 jours : review des ventes → ajuster le mix gagnants/nouveaux.
Objectif : converger progressivement vers un compte 100% gagnants + variantes.

---

## Règle de composition des 5 annonces

| Situation | Variantes gagnants | Nouveaux articles |
|-----------|-------------------|-------------------|
| Cycle 1 (démarrage) | 0 | 5 |
| Après 2 ventes | 2 | 3 |
| Après 3 ventes | 3 | 2 |
| Après 5 ventes | 4 | 1 |
| Compte mature | 5 variantes | 0 (si stock suffisant) |

**Règle simple :** 1 vente = 1 slot remplacé par une variante du gagnant.

---

## Exemple concret (expliqué par Yanis)

### Cycle 1 — Jours 1-3
- Poster 5 articles nouveaux (toutes catégories différentes)
- Résultat : **2 articles vendus**

### Cycle 2 — Jours 4-6
- 2 variantes des articles gagnants (même article, couleur différente)
- 3 nouveaux articles
- Résultat : **1 des 3 nouveaux se vend** → 3 gagnants au total

### Cycle 3 — Jours 7-9
- 3 variantes des gagnants
- 2 nouveaux articles
- Et ainsi de suite...

---

## Définition "Produit Gagnant"

Un produit devient **gagnant** dès qu'il réalise **1 vente**.
→ Il va dans `PRODUITS_GAGNANTS/`
→ On source immédiatement 2-3 variantes couleurs
→ On génère les images de chaque variante
→ On prépare les annonces `.docx`

---

## Ce que fait l'agent à chaque cycle

### Review J+3
1. Yanis indique quels articles ont été vendus
2. Agent les archive dans `PRODUITS_GAGNANTS/`
3. Agent source les variantes (même fournisseur, autre couleur)
4. Agent source X nouveaux articles (selon tableau ci-dessus)
5. Agent génère images + annonces `.docx` pour tout

### Stock minimum à maintenir
- 5 annonces/jour × 4 comptes = **20 annonces/jour**
- Toujours avoir **au moins 6 jours d'avance** en stock prêt
- Soit 120 annonces prêtes en permanence

---

## Structure fichiers par cycle

```
VINTED_FORMATION/
├── PRODUITS_GAGNANTS/          ← articles ayant vendu au moins 1 fois
│   └── [produit]/
│       ├── FICHE_PRODUIT.md
│       ├── VARIANTES.md
│       └── annonces/[couleur]/
│           ├── ANNONCE.docx
│           └── images/
├── annonces/                   ← stock prêt à publier (nouveaux + variantes)
│   └── [NN_NOM]/
│       ├── ANNONCE.docx
│       └── images/
└── _archive/                   ← articles testés 3 jours, 0 vente → archivés
```

---

## Comptes actifs

| Compte | Niche / Persona | Statut |
|--------|----------------|--------|
| Compte 1 | Romantique Victorienne | 🟡 En cours |
| Compte 2 | Western Chic | 🟡 En cours |
| Compte 3 | Grande Taille Cottagecore | 🟡 En cours |
| Compte 4 | LARP Médiéval | 🟡 En cours |

---

## Prochaine review

**Date prochaine review :** 21 mars 2026 (J+3)
Yanis indique les ventes → l'agent met à jour les gagnants et prépare le cycle suivant.
