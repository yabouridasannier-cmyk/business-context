# MODÈLE RÉFÉRENT — Config Compte Vinted Niche 3
Dernière MAJ : 16 mars 2026

---

## IDENTITÉ DU MODÈLE

**Fichier référence :** `images/model/MODEL_REFERENCE.jpg`
**Description :** Jeune femme, cheveux bruns tressés, silhouette mince, teint méditerranéen, visage non visible (tenu par téléphone). Style naturel, miroir selfie.

**À utiliser sur :** Compte billyprofil1@gmail.com (Vinted Niche 3 — Coquette Aesthetic)

---

## DESCRIPTION PROMPT (pour Leonardo.ai)

Utiliser cette description systématiquement pour garder la cohérence :

```
Young slim woman, brown braided hair, Mediterranean complexion, face hidden by phone mirror selfie,
full body visible, natural indoor lighting, casual aesthetic.
```

---

## 4 POSES À GÉNÉRER PAR PRODUIT

| Pose | Usage | Prompt à ajouter |
|------|-------|-----------------|
| **Face miroir** | Photo principale annonce | `taking a mirror selfie, phone hiding face, front view` |
| **De dos** | Photo secondaire | `back view, hair braid visible, no face` |
| **Profil** | Photo secondaire | `side profile, 3/4 view, natural light` |
| **Flatlay** | Photo produit seul | *(pas de modèle — juste le vêtement à plat)* |

---

## WORKFLOW GÉNÉRATION (Leonardo.ai)

Pour chaque nouveau produit :

1. **Input :** `images/model/MODEL_REFERENCE.jpg` + photo produit AliExpress
2. **Prompt :** `[description modèle], wearing [description produit], [couleur], [pose]`
3. **Mode Leonardo :** Image Guidance (référence de pose) ou img2img
4. **Output :** 3 photos portées + 1 flatlay
5. **Post-traitement :** Injection EXIF iPhone 15 automatique (`inject_exif_iphone()`)

---

## RÈGLES DE COHÉRENCE

- Toujours la même description modèle dans tous les prompts du compte
- Même fond : intérieur naturel, mur neutre ou miroir
- Même style photo : selfie naturel, pas studio
- JAMAIS montrer le visage (CGU Vinted + cohérence comptes multiples)
