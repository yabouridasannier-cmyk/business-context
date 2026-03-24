
[CALIBRATION_IMAGES.md](https://github.com/user-attachments/files/26213645/CALIBRATION_IMAGES.md)
# CALIBRATION QUALITÉ IMAGE GEMINI — GUIDE COMPLET
*Testé et validé le 25 mars 2026 — 3 itérations de calibration avec Yanis*

---

## POURQUOI CE FICHIER EXISTE

Vinted masque les annonces avec images IA détectables. Ce guide documente la calibration EXACTE pour que tout agent IA (Cowork, ChatGPT, etc.) reproduise le même niveau de qualité d'image sans itérations.

---

## LA RÈGLE D'OR : L'ENTRE-DEUX

**"J'ai pris 30 secondes pour faire cette photo mais mon appart est correct."**

### CE QUI SE FAIT MASQUER (trop pro)
- Images trop lisses, pas assez de contraste
- Éclairage de studio / photoshoot professionnel
- Décors trop parfaits (monde idéal, tout bien rangé)
- Images photoshopées / trop retouchées
- Fond blanc parfait
- Mise en scène "magazine" (scandinave parfait, minimaliste extrême)

### CE QUI NE VEND PAS (trop low-effort)
- Images trop sombres, éclairage jaunâtre
- Décors sales ou très en désordre
- Angles trop tordus, photos floues
- Valeur perçue trop basse

---

## DIRECTIVE DE STYLE — INJECTER DANS CHAQUE PROMPT

Copier-coller ce bloc dans CHAQUE prompt Gemini :

```
STYLE INSTRUCTIONS: This photo should look like a real person's iPhone photo
for a Vinted listing, but still appealing enough to make someone want to buy.
NOT a professional photoshoot (no perfect lighting, no studio setup, no
immaculate staging). NOT super messy or ugly (no dirty floors, no harsh yellow
light, no extreme angles). THE SWEET SPOT: a tidy-ish real apartment with
natural daylight from a window, the item placed with some care but not
perfectly styled, small real-life details visible (remote control, book,
phone charger cable, mug), colors slightly warm and natural, slight angle
imperfection. Think: "I took this in 30 seconds but my apartment is decent."
```

---

## RÈGLE CRITIQUE : LES MAINS

**UNE SEULE MAIN visible maximum.**

Logique : la personne tient son téléphone d'une main pour prendre la photo. On voit son AUTRE main dans le cadre qui touche/montre le produit.

- ✅ Main droite visible touchant le produit, photo prise main gauche
- ✅ Main gauche visible, photo prise main droite
- ❌ JAMAIS deux mains visibles (le téléphone est tenu comment sinon ?)
- ❌ Pas de mains qui "présentent" le produit comme un shooting

Prompt pour photos avec main :
```
The seller holds their phone in one hand. We see their OTHER hand casually
resting on or touching the product. First-person perspective, looking down.
Only ONE hand visible — the other holds the phone. This must make logical sense.
```

---

## STRUCTURE : 3 PHOTOS PAR ANNONCE

| # | Type | Style | Ce qu'on montre |
|---|------|-------|-----------------|
| 1 | Mise en scène | Entre-deux | Produit en contexte (canapé, chaise, sol). Décor réaliste avec détails de vie. Lumière naturelle imparfaite. |
| 2 | Détail/texture | Entre-deux | Close-up qualité produit. Éventuellement UNE main qui touche. |
| 3 | Vue brute | Plus basique | Produit seul sur surface simple (lit, sol). Vue d'ensemble overhead. Moins d'effort. |

---

## CHECKLIST VALIDATION AVANT PUBLICATION

- [ ] L'image fait "vraie" (pas de studio, pas de fond blanc parfait)
- [ ] La valeur perçue reste HAUTE (article désirable)
- [ ] Petits détails de vie réelle visibles (télécommande, tasse, câble, livre)
- [ ] Éclairage naturel mais PAS parfait (légèrement chaud)
- [ ] Angle pas parfaitement droit (léger décalage naturel)
- [ ] Décor rangé mais PAS impeccable (vivant, pas magazine)
- [ ] Si main visible : UNE SEULE (l'autre tient le téléphone)
- [ ] Pas de texte/watermark/logo visible
- [ ] Métadonnées EXIF iPhone 15 injectées

---

## WORKFLOW TECHNIQUE (Pour agent IA / Cowork)

```
1. Récupérer image produit fournisseur (Temu/AliExpress)
2. Récupérer image persona : personas/[NOM_PERSONA]/fichier.avif → convertir en .jpg
3. Appeler API Gemini :
   - Modèle : gemini-2.5-flash-image
   - Clé API : .env (NE JAMAIS mettre en clair dans le repo)
   - Contents : [prompt + STYLE INSTRUCTIONS + image produit]
   - Config : response_modalities=["IMAGE", "TEXT"]
4. Injecter EXIF iPhone 15 :
   Make: Apple | Model: iPhone 15 | Software: 17.4.1
   FocalLength: 6.86mm | FNumber: f/1.78 | ISO: 200
5. Vérifier visuellement vs checklist
6. Livrer : 3 photos + titre + description + hashtags + compte cible
```

---

## PROMPTS CALIBRÉS PAR TYPE

### Chaussures

**Photo 1 (sol casual) :**
```
[STYLE INSTRUCTIONS] These EXACT [description] placed casually on a wooden
floor with a pair of jeans and tote bag nearby. Natural indoor light, slightly
warm. Taken from above while standing.
```

**Photo 2 (portées, POV) :**
```
[STYLE INSTRUCTIONS] Only legs from knee down wearing dark jeans and these
EXACT shoes. First-person looking down at own feet. Regular floor, slightly
off-angle.
```

**Photo 3 (brut) :**
```
[STYLE INSTRUCTIONS] These EXACT shoes on a plain bedsheet. Overhead, no
styling. Quick snap.
```

### Déco / Coussins / Housses

**Photo 1 (en situation) :**
```
[STYLE INSTRUCTIONS] This EXACT [produit] on a [meuble] in a normal living
room. Real details visible (remote, mug, book). Natural daylight, slightly warm.
```

**Photo 2 (détail + une main) :**
```
[STYLE INSTRUCTIONS] First-person view looking down. ONE hand touching this
EXACT [produit] to show texture. The other hand holds the phone. Only ONE hand.
```

**Photo 3 (brut) :**
```
[STYLE INSTRUCTIONS] This EXACT [produit] alone on a plain surface. Overhead,
simple, no styling.
```

### Tapis

**Photo 1 (chambre) :**
```
[STYLE INSTRUCTIONS] This EXACT rug next to a bed. Bedroom not perfectly made,
slippers visible. Normal lighting.
```

**Photo 2 (salon) :**
```
[STYLE INSTRUCTIONS] This EXACT rug on wooden floor in living room. Coffee
table leg, maybe a book. Natural light.
```

**Photo 3 (roulé) :**
```
[STYLE INSTRUCTIONS] This EXACT rug rolled up or folded. Close-up texture.
Ready-to-ship vibe.
```

### Vêtements

**Photo 1 (selfie miroir) :**
```
[STYLE INSTRUCTIONS] Mirror selfie, phone covers the face. Wearing this EXACT
[vêtement]. Normal bedroom or hallway. ONE hand holds phone, face hidden.
```

**Photo 2 (dos) :**
```
[STYLE INSTRUCTIONS] Back view wearing this EXACT [vêtement]. Hair visible,
natural indoor light. Real apartment.
```

**Photo 3 (flatlay) :**
```
[STYLE INSTRUCTIONS] This EXACT [vêtement] laid flat on bed or wooden floor.
Slightly rumpled, not perfectly spread.
```

---

## HISTORIQUE DE CALIBRATION

| Version | Style | Verdict |
|---------|-------|---------|
| V1 | Ultra pro (scandinave magazine) | ❌ Risque masquage Vinted |
| V2 | Ultra messy (sol sale, angle tordu) | ❌ Valeur perçue trop basse |
| V3 | Entre-deux (appart correct, détails vie) | ✅ Validé |
| V3.1 | Correction mains (une seule visible) | ✅ Validé final |

---

*Créé le 25 mars 2026 après 3 itérations de calibration.*
