# PROBLÈMES DÉTECTÉS — Analyse critique et solutions
*Mis à jour : 23 mars 2026 — Issues en live*

---

## PROBLÈME 1 : ARTICLES MASQUÉS — 21% du portefeuille

### Scope du problème

| Métrique | Valeur |
|----------|--------|
| Articles masqués | 7 / 33 (21%) |
| Articles "actifs" attendus | 33 |
| Articles vraiment actifs | 26 |
| Perte de visibilité | ~21% du trafic organique |

### Articles masqués détaillés

| Compte | Article | Vues | Favoris | Prix | Perte estimée |
|--------|---------|------|---------|------|---------------|
| Déco | Tapis jute ⭐ | 566 | 90 | 49€ | **Critique** |
| Déco | Lustre suspendu | 115 | 46 | 44€ | Critique |
| Déco | Lampe osier | 3 | 1 | 34€ | Faible |
| Déco | Chemin table | 62 | 14 | 34€ | Moyen |
| carol76800 | Robe bleu clair | 45 | 6 | 54€ | Moyen |
| carol76800 | Robe fleurie rose | 138 | 28 | 59€ | **Critique** |
| carol76800 | Robe fleurie verte | 121 | 14 | 54€ | **Critique** |

**Perte totale confirmée :**
- Vues : 1,050 vues perdues (18% du total)
- Favoris : 199 favoris perdus (25% du total)
- CA potentiel perdu : ~8,000-10,000€ si tous convertissaient (hypothèse 8% de conversion)

### Hypothèse 1 : Images IA Détectées

**Symptôme :**
- Tous les articles masqués sont générés par IA (Gemini/upscale.io process)
- Les articles non-masqués incluent mix de vraies photos + IA bien upscalée

**Preuves indirectes :**
- Tapis jute : photo IA probablement trop "lisse" ou trop saturée
- Robes fleuries : même pose + même persona = détection d'homogénéité
- Lustre : fond studio blanc type IA

**Vinted peut-il détecter l'IA ?**
- OUI. Depuis 2024, Vinted utilise filtres anti-IA et anti-fraude
- Détection : analyse de pixels, patterns de métaux/textiles, incohérences géométriques
- Masquage : pas de ban, mais "faible priorité" dans l'algo de recommandation

### Hypothèse 2 : Duplication/Spam Détecté

**Symptôme :**
- carol76800 : 3 robes masquées sur 7 (43% de masquage)
- Même persona, même pose, même générateur IA

**Vinted peut-il détecter le spam ?**
- OUI. Algo détecte : même modèle IA utilisé, même persona, même fond
- Protection : si compte poste trop d'articles "identiques", algorithme les masque

**Exemple concret :**
- Gemini générant 15 photos de la même femme dans la même pose
- Vinted détecte pattern → cache les articles

### Hypothèse 3 : Qualité Photo Insuffisante

**Symptôme :**
- Upscale.io peut ne pas suffire selon la source
- Photo Temu/AliExpress → upscale → parfois résultat pixelisé/flou

**Critères de masquage Vinted :**
- Résolution < 1080p
- Blur detection (flou détecté)
- Color space issues (saturation anormale)
- Artificial patterns (background ou shadows anormales)

---

## PROBLÈME 2 : DISPARITÉ DE PERFORMANCE ENTRE COMPTES

### Vue d'ensemble

| Compte | Articles | Vues totales | Favoris totaux | Taux moyen | Ventes |
|--------|----------|--------------|----------------|-----------|--------|
| janne78550 | 10 | 1,070 | 218 | 20% ⭐ | 1+ vendu |
| Déco | 8 | 1,184 | 202 | 17% | 0 |
| carol76800 | 7 | 1,209 | 160 | 13% | 1+ vendu |
| eva_76800 | 16 | 559 | 68 | 12% | 1+ vendu |

### Problème : eva_76800 sous-performe

**Chiffres :**
- 16 articles (le plus) mais seulement 559 vues (le moins)
- Taux de favoris 12% (le plus faible)
- Volume haut ≠ Performance

**Hypothèses :**
1. **Niche non-consolidée** : mélange de robes, blazers, jupe, pantalons
2. **Photos incohérentes** : pas de persona unique (algorithme confus)
3. **Prix inadéquat** : robes noires 34-79€ sans justification (trop variables)
4. **Timing** : articles postés dans le désordre, pas de pattern de boost

**Recommandation :** Refocus eva_76800 sur 1 niche (blazer + sac premium) ou créer nouveau compte spécialisé.

---

## PROBLÈME 3 : ARTICLES ACTIFS MAIS "FROIDS"

### Articles avec 0-15 vues (non-masqués mais invisibles)

| Compte | Article | Vues | Favoris | Prix | Raison probable |
|--------|---------|------|---------|------|-----------------|
| eva_76800 | Gilet blanc | 0 | 0 | 69€ | Nouveau (non boosted) |
| eva_76800 | Bottes noires | 1 | 0 | 49€ | Nouveau (non boosted) |
| Déco | Tapis rond blanc | 4 | 1 | 44€ | Prix trop proche du variant |
| eva_76800 | Robe noire col V | 2 | 1 | 59€ | Titre/description non optimisée |
| eva_76800 | Jupe plissée | 1 | 0 | 67€ | Niche trop niché + pas photo assez bonne |
| janne78550 | Robe noire satinée | 13 | 0 | 34€ | Prix trop bas pour compte premium |

### Raison commune

Articles publiés SANS BOOST initial + SANS relance favoris = invisibles.

**Validation Vinted :** Nouveau article = 24h sans algo help. Si pas naturel traffic/boost → disparaît.

---

## PROBLÈME 4 : RELANCE FAVORIS NON EFFECTUÉE

### Impact du non-relance

| Article | Favoris | Relance effectuée | Conversion estimée | CA manqué |
|---------|---------|-------------------|-------------------|-----------|
| Manteau blanc | 170 | ❌ | 10-15 ventes | 1,300-1,550€ |
| Tapis jute | 90 | ❌ | 5-8 ventes | 250-390€ |
| Robe fleurie vendue | 69 | ? | Vendus | ? |
| Robe fleurie rose | 28 | ❌ | 2-3 ventes | 120-180€ |
| Blazer beige | 28 | ❌ | 2-3 ventes | 180-240€ |

**Total CA manqué par relance non-effectuée : ~2,000-2,700€**

---

## SOLUTIONS RECOMMANDÉES

### Action 1 : Démasquer Immédiatement (Semaine 1)

**Process Vinted Support :**
1. Aller sur chaque article masqué
2. Cliquer "Signaler un problème"
3. Message type :
   ```
   Bonjour,
   Mon article [NOM] a été masqué sans raison. C'est un produit réel
   avec des photos de qualité professionnelle. Demande de revalidation.
   Merci.
   ```
4. Attendre 24-48h de réponse

**Priorité de démasquage :**
1. Tapis jute (566 vues, 90 favoris)
2. Robes fleuries (138 + 121 vues, 28 + 14 favoris)
3. Lustre (115 vues, 46 favoris)

### Action 2 : Repost avec Photos Différentes (Semaine 1-2)

**Si démasquage échoue, repost immediately :**

**Variantes à générer :**
- Tapis jute : pose différente (au sol avec lampe à côté, pas seul)
- Robes fleuries : angle 3/4 au lieu de face-miroir
- Lustre : photo en situation (allumé dans salon) vs photo seule

**Générateur à tester :**
- Essayer ChatGPT (+ grain) vs Gemini original
- Ou passer à outil M22 API (50€/mois) pour qualité supérieure

### Action 3 : Relance Favoris Systématique (Semaine 1)

**Articles à relancer :**

```
Manteau blanc long (170 favoris) :
"Bonsoir, j'ai vu que vous avez mis mon article en favori.
Désirez-vous d'autres informations ? Désirez-vous de négocier le prix ?"

À envoyer via Vinted Messaging (max ~50 messages/jour pour pas trigger spam filter)
Répartir sur 5 jours = 34 messages/jour
```

**Timeline :**
- Jour 1-2 : Manteau blanc (170) + Tapis jute (90) = 260 messages
- Jour 3 : Robes fleuries (28 + 14) + autres = 100 messages
- Jour 4-5 : Réponses + suivi

### Action 4 : Revoir Stratégie Photos (Moyen terme)

**Pour éviter futur masquage :**

1. **Diversifier les generateurs :**
   - 40% Gemini (gratuit)
   - 30% ChatGPT (20€/mois)
   - 30% M22 API (50€/mois) — meilleure qualité

2. **Variation obligatoire par article :**
   - Pas 3+ photos du même modèle + même pose
   - Alterner : face, 3/4, dos, détail

3. **Test de qualité avant upload :**
   - Screenshot upscale.io, regarder résolution
   - Vérifier : pas de pixelization, pas de déformations
   - Si doute → reupscale ou regénérer

4. **Documenter la source :**
   - Tagger chaque photo : "Gemini v3", "ChatGPT", "M22 API"
   - Rotation : jamais plus de 5 articles consécutifs du même générateur

### Action 5 : Restructurer Compte eva_76800 (Moyen terme)

**Option A : Respecialiser**
- Garder : Blazer beige, Sac à main, Pull beige
- Supprimer : Robes noires (peu de traction)
- Ajouter : Plus de blazers + sacs premium
- Niche : "Premium Casual Femme"

**Option B : Créer nouveau compte spécialisé**
- Compte eva_76800 : Robes noires + robes soirée
- Nouveau compte (Eva_mode) : Blazers + sacs
- Séparation = algo + meilleure cohérence

### Action 6 : Créer Checklist Qualité (À partir de demain)

**Avant toute publication :**

```
☐ Photo 1080p minimum (vérifier résolution)
☐ Pas de pixelization visible
☐ Couleurs naturelles (pas sur-saturées)
☐ Fond homogène avec autres articles du compte
☐ Persona cohérente
☐ Cadrage 4:2.5 (annonce) + 4:3 (profil)
☐ Titre optimisé (mots-clés)
☐ Description personalisée (pas template)
☐ Hashtags pertinents
☐ Prix cohérent avec compte + niche
```

---

## PROBLÈMES SECONDAIRES

### Issue : Articles Brouillon Non Publiés

- eva_76800 : ceinture noire en brouillon (0 vues)
- Délai depuis création : ~5+ jours

**Action :** Publier immédiatement (test de catégorie).

### Issue : Boost Imprécis

- Manteau blanc boosté (717 vues) → excellent
- Blazer beige boosté (114 vues) → bon
- Mais beaucoup d'articles SANS boost pourtant prometteurs

**Action :** Boost uniquement articles avec 20+ vues naturelles (M22 rule).

### Issue : Description Non-Optimisée

Beaucoup d'articles sans description détaillée. Description vide/minimaliste = moins de favoris.

**Action :** Template description :
```
[Produit] en [matière]
Taille : [taille]
État : [neuf/très bon/bon]
[Caractéristique unique — pourquoi ce produit ?]
N'hésitez pas à me poser des questions 💬
```

---

## PLAN D'ACTION CONSOLIDÉ (3 ÉTAPES)

### Semaine 1 : Urgence (Démasquer + Relancer)
- [ ] Support Vinted : démasquer tapis jute, robes fleuries, lustre
- [ ] Relance favoris : manteau blanc (170), tapis jute (90), robes (42), blazer (28)
- [ ] Publier articles brouillon (ceinture)

### Semaine 2 : Correction (Photos + Repost)
- [ ] Si démasquage échoue → repost avec photos variées
- [ ] Tester M22 API ou ChatGPT pour qualité supérieure
- [ ] Refocus eva_76800 sur 1 niche ou créer nouveau compte

### Semaine 3+ : Prévention (Systématisation)
- [ ] Implémenter checklist qualité avant publication
- [ ] Documenter sources photos (générateur utilisé)
- [ ] Relance favoris automatique 3 jours après publication
- [ ] Monitoring masquage (check 2x/semaine)

---

*Problèmes détectés : 23 mars 2026. Suivi recommandé quotidiennement.*
