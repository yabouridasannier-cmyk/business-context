# COURS COMPLET — CLAUDE COWORK
*23 mars 2026 — par Claude, pour Yanis*

---

## 1. C'EST QUOI COWORK, CONCRÈTEMENT ?

Cowork c'est un **agent autonome** qui tourne dans une machine virtuelle Linux isolée, directement sur ton ordinateur. C'est pas juste un chatbot — c'est un programme qui peut lire tes fichiers, exécuter des commandes, naviguer sur le web, envoyer des mails, et enchaîner des actions complexes tout seul.

La différence fondamentale avec le chat Claude normal : dans le chat, Claude répond à tes messages. Dans Cowork, Claude **agit**. Il peut ouvrir 10 fichiers, les analyser, créer un document Word, chercher des infos sur le web, et mettre à jour ton calendrier — tout ça en une seule demande.

**Cowork est construit sur Claude Code**, l'outil que les développeurs utilisent en ligne de commande. Anthropic a pris cette base technique et l'a rendu accessible via l'app desktop pour les non-développeurs. C'est pour ça que parfois tu vois des termes techniques dans les erreurs — c'est le moteur Claude Code en dessous.

**Statut actuel** : Cowork est en "Research Preview" depuis janvier 2026. Ça veut dire qu'Anthropic le considère encore en phase de test. Ils l'ont sorti tôt volontairement pour apprendre comment les gens l'utilisent et l'améliorer rapidement. D'où les bugs, les limitations, et les mises à jour fréquentes.

---

## 2. L'ARCHITECTURE — COMMENT ÇA FONCTIONNE EN COULISSES

### La sandbox (bac à sable sécurisé)

Quand tu ouvres Cowork, voilà ce qui se passe :

1. **Une machine virtuelle Linux** se lance sur ton Mac/PC (via VZVirtualMachine sur Mac)
2. À l'intérieur, un système de sécurité appelé **Bubblewrap** restreint ce que Claude peut voir et faire
3. Un filtre **Seccomp** bloque les commandes système dangereuses au niveau du noyau
4. Le réseau passe par un **proxy avec liste blanche** — Claude ne peut accéder qu'aux domaines autorisés

Résultat : Claude travaille dans une bulle. Il voit ton dossier sélectionné et les outils connectés, mais il ne peut pas toucher au reste de ton système.

### L'orchestrateur et les sous-agents

C'est LA partie importante pour comprendre pourquoi Cowork est puissant (et pourquoi ça consomme).

Quand tu donnes une tâche complexe à Cowork, voilà ce qui se passe :

```
TOI : "Fais-moi un audit des 3 entreprises de Kaya"
         │
         ▼
   ORCHESTRATEUR (Claude principal)
   → Analyse la demande
   → Découpe en sous-tâches
   → Lance des sous-agents
         │
    ┌────┼────────────┐
    ▼    ▼            ▼
 Agent 1  Agent 2   Agent 3
 Recherche Recherche Recherche
 RAV EXP   P3F      Combles
    │       │         │
    ▼       ▼         ▼
   ORCHESTRATEUR
   → Récupère les résultats
   → Synthétise
   → Te présente le tout
```

**Points clés :**
- Chaque sous-agent a sa propre fenêtre de contexte indépendante — il ne voit PAS tout l'historique de ta conversation
- Il reçoit uniquement les infos nécessaires pour sa sous-tâche
- Il renvoie un résumé à l'orchestrateur, pas son contexte complet
- L'orchestrateur coordonne, synthétise, et te donne le résultat final

C'est pour ça que Cowork peut gérer des tâches qu'un simple chat ne pourrait jamais faire — mais c'est aussi pour ça que **chaque sous-agent consomme des tokens en plus**.

### Les outils disponibles (MCP = Model Context Protocol)

MCP c'est le protocole qui permet à Claude de se brancher sur des services externes. Chaque "connecteur" (Gmail, Calendar, etc.) est un serveur MCP qui expose des outils.

Ce que Cowork a accès dans notre configuration :

| Connecteur | Ce qu'il peut faire |
|-----------|-------------------|
| **Système de fichiers** | Lire, écrire, éditer tous les fichiers du dossier sélectionné |
| **Bash/Terminal** | Exécuter n'importe quelle commande Linux |
| **Gmail** | Chercher mails, lire mails, créer brouillons (PAS envoyer) |
| **Google Calendar** | Lire, créer, modifier, supprimer des événements |
| **Chrome** | Naviguer sur le web, remplir des formulaires, cliquer (beta) |
| **Recherche web** | Chercher sur internet |
| **Explorium** | Enrichissement de données B2B (infos entreprises, prospects) |
| **Vercel** | Déploiement de sites web |
| **Supabase** | Base de données |

**Chaque connecteur activé ajoute du poids au contexte** — même si tu ne l'utilises pas dans ta session. C'est les définitions des outils qui prennent de la place. C'est un des facteurs de consommation.

---

## 3. LA MÉMOIRE — LE SUJET CRITIQUE

### Ce que Claude retient PENDANT une session

Tout. Chaque message que tu envoies, chaque réponse de Claude, chaque résultat d'outil — tout s'accumule dans la **fenêtre de contexte**.

La fenêtre de contexte c'est comme une feuille de papier : elle a une taille fixe. Plus tu écris dessus, moins il reste de place. Quand elle est pleine, deux choses peuvent se passer :

1. **Compaction automatique** : Claude résume l'historique pour libérer de la place (tu perds des détails)
2. **Erreur "Prompt is too long"** : la session est morte, plus rien ne passe

**Taille de la fenêtre** : environ 200 000 tokens en standard (mais il y a eu un bug signalé le 23 mars 2026 où la fenêtre 1M tokens pour Opus 4.6 n'est plus disponible dans Cowork alors qu'elle l'était 2 jours avant).

### La "spirale de mort" de la compaction

Bug connu et documenté : si ton CLAUDE.md est gros + beaucoup de connecteurs MCP activés, le contexte système seul peut prendre **86% de la fenêtre de 200K tokens**. Il reste 27K tokens pour travailler. Résultat : compaction toutes les 30 secondes, la session devient inutilisable.

### Ce que Claude retient ENTRE les sessions

**RIEN.** Zéro. Chaque nouvelle conversation, Claude repart d'une page blanche.

La seule "mémoire" entre sessions, c'est les fichiers sur ton disque. C'est pour ça que notre système de repository existe :

```
CLAUDE.md    → Ce que Claude lit EN PREMIER à chaque session
TASKS.md     → Les tâches en cours
memory/      → Le contexte détaillé (glossaire, fiches personnes, projets)
```

Quand Claude ouvre une nouvelle session, il remonte l'arborescence de dossiers et charge tous les CLAUDE.md qu'il trouve. C'est sa seule façon de "se souvenir".

### La fonctionnalité "Projets"

Anthropic a ajouté les **Projets** dans Cowork récemment. Un projet = un espace de travail persistant avec ses propres fichiers, instructions, et mémoire. La mémoire du projet est **stockée localement sur ton ordi** (pas dans le cloud). C'est mieux que rien, mais c'est encore limité.

---

## 4. LA CONSOMMATION — POURQUOI ÇA COÛTE AUTANT

### Comment c'est facturé

Tu es sur un plan avec une **fenêtre glissante de 5 heures**. Ce n'est pas un quota journalier — c'est un quota qui se renouvelle en continu.

| Plan | Prix | Messages environ / 5h |
|------|------|-----------------------|
| Pro | 20€/mois | ~45 messages |
| Max 5x | 100€/mois | ~225 messages |
| Max 20x | 200€/mois | ~900 messages |

**Mais attention** : un "message" Cowork ≠ un message chat normal. Un seul message Cowork peut déclencher 5-10 appels d'outils, chacun coûtant des tokens.

### Pourquoi Cowork consomme 5 à 15x plus que le chat

Décomposition d'un message Cowork typique :

```
TON MESSAGE : "Cherche des infos sur RAV EXP et mets-les dans TASKS.md"

Tokens consommés :
├── Instructions système Cowork           ~15 000 tokens
├── Définitions de TOUS les outils MCP    ~10 000 tokens
├── Historique de la conversation          ~5 000 à 200 000 tokens
├── Ton message                           ~50 tokens
├── Réflexion de Claude (thinking)        ~2 000 tokens (facturés x5!)
├── Appel outil : recherche web           ~3 000 tokens (résultat)
├── Appel outil : Explorium               ~2 000 tokens (résultat)
├── Appel outil : lecture TASKS.md        ~1 500 tokens (résultat)
├── Appel outil : édition TASKS.md        ~500 tokens
└── Réponse finale de Claude              ~500 tokens
                                    TOTAL : ~40 000+ tokens
```

En chat normal, le même échange coûterait ~3 000 tokens. **Soit 13x plus cher en Cowork.**

### Le multiplicateur x5 des tokens de sortie

Point technique crucial : les tokens en **sortie** (ce que Claude écrit/pense) coûtent **5 fois plus** que les tokens en entrée (ce qu'il lit).

Ça veut dire :
- 500 tokens de réponse inutile = 2 500 tokens gaspillés
- Les tokens de "réflexion" (extended thinking) sont facturés comme des tokens de sortie → x5
- Un Claude bavard qui fait de longues réponses te coûte exponentiellement plus cher

### La règle de l'accumulation

Message 1 : Claude lit 25K tokens (système + outils) → coût : 25K
Message 2 : Claude relit tout + message 1 + réponse 1 = 30K → coût : 30K
Message 3 : Tout + messages 1-2 + réponses = 38K → coût : 38K
Message 10 : 80K+ → coût : 80K
Message 30 : 150K+ → compaction ou erreur

**Chaque message coûte plus cher que le précédent.** C'est mathématique et inévitable. C'est POUR ÇA qu'il faut des sessions courtes.

---

## 5. DISPATCH — LE CONTRÔLE À DISTANCE (NOUVEAU)

C'est la feature dont tu parlais. **Claude Dispatch** permet de contrôler Cowork **depuis ton téléphone**, pendant que les tâches s'exécutent sur ton ordinateur.

### Comment ça marche

```
📱 TON TÉLÉPHONE
   │
   │ Tu donnes des instructions
   ▼
🧠 ORCHESTRATEUR (sur ton ordi)
   │
   ├──→ Session 1 : Audit site web ravexp.fr
   ├──→ Session 2 : Recherche prospects Global Industrie
   └──→ Session 3 : Mise à jour TASKS.md
   │
   │ Résultats remontent
   ▼
📱 TON TÉLÉPHONE
   Tu consultes les résultats
```

### Ce que ça change concrètement

- Tu es en déplacement terrain → tu lances "prépare-moi l'audit de tel prospect" depuis ton tel
- Cowork bosse sur ton ordi pendant que toi tu prospectes
- Tu reviens, tout est prêt
- Chaque session de tâche a son propre contexte isolé (pas de pollution entre tâches)

### Conditions

- Ton ordinateur doit rester **allumé et éveillé** (pas de mise en veille)
- L'app Claude Desktop doit rester **ouverte**
- Si ton ordi se met en veille ou l'app se ferme → les tâches s'arrêtent

---

## 6. SÉCURITÉ — CE QUE TU DOIS SAVOIR

### Les protections

Cowork a 4 couches de sécurité : VM isolée → Bubblewrap → Seccomp → Proxy réseau. C'est solide sur le papier.

### Les incidents réels

**Suppression de fichiers** : Un utilisateur (Nick Davidov) a demandé à Cowork d'organiser le bureau de sa femme. Il a autorisé la suppression de fichiers temporaires. Cowork a accidentellement supprimé **15 ans de photos** (11 Go). Les fichiers supprimés via terminal ne vont pas à la corbeille. Il a pu les récupérer via iCloud (sauvegarde 30 jours), mais sans ça c'était perdu.

**Fatigue d'approbation** : Cowork demande ta permission avant les actions sensibles. Mais les études montrent que les utilisateurs développent rapidement une "fatigue d'approbation" — ils cliquent OK sans vérifier ce que Claude fait réellement. C'est un vrai risque.

**Faille d'injection** : Des chercheurs en sécurité ont démontré qu'un attaquant peut piéger un fichier pour que Cowork exfiltre tes données confidentielles. La faille a été signalée 3 mois avant le lancement et n'a pas été corrigée à temps.

### Règles de prudence

- **Toujours lire** ce que Cowork propose avant de valider, surtout les suppressions
- **Ne jamais** donner accès à des dossiers contenant des données ultra-sensibles (mots de passe, documents bancaires)
- **Sauvegardes régulières** de tes fichiers importants

---

## 7. BUGS CONNUS (MARS 2026)

| Bug | Impact | Statut |
|-----|--------|--------|
| Fenêtre 1M tokens disparue dans Cowork | Sessions plus courtes, compaction plus fréquente | Signalé 23/03 |
| Spirale de compaction | Session inutilisable quand système > 86% du contexte | Connu |
| Boucle de reprise de session | "I'll pick up where I left off" en boucle, brûle tout le contexte | Connu |
| Rate limit avec fenêtre 1M | Erreurs "Rate limit reached" même avec quota dispo | Connu |
| Allowlist réseau cassée | Domaines autorisés quand même bloqués par le proxy | Connu |
| DNS statique | Si un service change d'IP, la connexion échoue jusqu'au redémarrage | Connu |

---

## 8. ASTUCES AVANCÉES — CE QUE LES POWER USERS FONT

### 8.1 Sessions courtes et thématiques

La règle n°1 que TOUS les utilisateurs avancés appliquent. Pas de session marathon.

| Au lieu de... | Fais plutôt... |
|--------------|----------------|
| 1 session de 3h (tout mélangé) | 4 sessions de 30-45 min (1 sujet chacune) |
| Continuer quand ça rame | Archiver + relancer une session fraîche |
| Garder la même session "au cas où" | Fermer dès que la tâche est finie |

### 8.2 Réduire le poids du contexte système

Chaque connecteur MCP activé ajoute ses définitions d'outils au contexte, même si tu ne l'utilises pas. Avec Gmail + Calendar + Chrome + Explorium + Vercel + Supabase, c'est potentiellement **10 000+ tokens** de définitions d'outils chargés à chaque message.

**Astuce** : si ta session ne concerne que Vinted (fichiers locaux uniquement), tu n'as pas besoin de Gmail ou Calendar. Mais actuellement, tu ne peux pas désactiver les connecteurs par session (limitation Cowork).

### 8.3 Garder CLAUDE.md concis

Recommandation officielle : **moins de 500 lignes**. Chaque ligne de CLAUDE.md est rechargée à chaque message. Un CLAUDE.md de 2000 lignes = 2000 lignes x nombre de messages = explosion de tokens.

Notre CLAUDE.md actuel est correct en taille, mais il faut le surveiller.

### 8.4 Être chirurgical dans les demandes

```
❌ COÛTEUX : "Fais un point complet sur tout"
   → Claude va lire 10 fichiers, réfléchir longuement, produire un pavé

✅ ÉCONOMIQUE : "Ajoute 'Relancer Marshall 97€' dans TASKS.md section relances"
   → Claude ouvre 1 fichier, fait 1 edit, terminé
```

### 8.5 Regrouper les demandes liées

```
❌ COÛTEUX (3 messages = 3x le contexte relu) :
   Message 1 : "Cherche le CA de RAV EXP"
   Message 2 : "Cherche aussi le CA de P3F"
   Message 3 : "Et Combles & Couverture"

✅ ÉCONOMIQUE (1 message = 1x le contexte relu) :
   "Cherche le CA, l'effectif et le site web de ces 3 entreprises :
    RAV EXP, P3F Combles, Combles & Couverture"
```

### 8.6 Utiliser le bon outil pour le bon besoin

| Besoin | Outil |
|--------|-------|
| Question simple, pas besoin de fichiers | Chat Claude normal (claude.ai) |
| Recherche web rapide | Google toi-même |
| Travail sur tes fichiers + Gmail + Calendar | Cowork |
| Tâche longue pendant que tu es en déplacement | Dispatch (depuis le téléphone) |
| Calcul rapide, conversion | Chat Claude ou calculatrice |

### 8.7 Fin de session = mise à jour fichiers

**Toujours** avant de fermer :
1. Demander à Claude de mettre à jour CLAUDE.md avec les nouvelles infos
2. Vérifier que TASKS.md reflète les tâches en cours
3. S'assurer que toute info importante est dans un fichier (pas juste "dite" dans le chat)

---

## 9. COWORK vs CLAUDE CHAT vs CLAUDE CODE

| | Chat Claude | Cowork | Claude Code |
|--|-------------|--------|-------------|
| **Interface** | Navigateur web | App desktop | Terminal |
| **Pour qui** | Tout le monde | Non-développeurs | Développeurs |
| **Accès fichiers** | Non | Oui (dossier sélectionné) | Oui (tout le système) |
| **Exécuter des commandes** | Non | Oui (dans la VM) | Oui (directement) |
| **Connecteurs (Gmail, etc.)** | Non | Oui (MCP) | Oui (MCP) |
| **Autonomie** | Répond aux questions | Exécute des workflows complets | Exécute des workflows complets |
| **Sécurité** | Aucun risque | Sandbox VM | Risque moyen (accès direct) |
| **Consommation** | Faible | Élevée | Élevée |
| **Plugins/Skills** | Non | Oui | Oui |

---

## 10. CONCURRENTS

| Outil | Philosophie | Prix |
|-------|-----------|------|
| **Claude Cowork** | "Files First" — vit sur ton bureau, travaille avec tes fichiers | 20-200€/mois |
| **OpenAI Operator** | "Web First" — vit dans le navigateur, navigue sur internet | ~200€/mois |
| **ChatGPT Desktop** | Chat + Code Interpreter, moins autonome | 20-200€/mois |
| **Cursor / Windsurf** | IDE avec IA intégrée, pour développeurs uniquement | 20-40€/mois |

Cowork est le meilleur pour ce qu'on fait : travailler avec des fichiers locaux, gérer un pipeline, organiser un business. Operator serait mieux pour automatiser des tâches web (réserver des hôtels, remplir des formulaires en ligne).

---

## CHECKLIST RAPIDE — À RELIRE AVANT CHAQUE SESSION

```
AVANT DE COMMENCER
☐ Quel est le sujet UNIQUE de cette session ?
☐ Est-ce que j'ai vraiment besoin de Cowork pour ça ? (sinon → chat normal)
☐ Est-ce que je peux regrouper mes demandes en 1-2 messages clairs ?

PENDANT LA SESSION
☐ Si ça rame → archiver et relancer
☐ Si c'est complexe → donner toutes les infos en 1 message
☐ Ne pas demander de relire ce qui vient d'être fait

AVANT DE FERMER
☐ CLAUDE.md à jour ?
☐ TASKS.md à jour ?
☐ Toute info importante stockée dans le bon fichier ?
```

---

*Dernière mise à jour : 23 mars 2026*
*Sources : documentation Anthropic, GitHub Issues, Reddit r/ClaudeAI, retours utilisateurs Twitter/X*
