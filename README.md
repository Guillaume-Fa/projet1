# projet1

Projet scolaire de programmation en Python.

## 🐍 Snake

Un jeu du serpent classique, codé en Python avec le module `turtle`.
Le fichier se trouve dans [`Jeux/snake.py`](Jeux/snake.py).

### Principe du jeu

- Le serpent avance tout seul dans une grille de 600 × 600 pixels.
- Il faut manger les pommes rouges : chaque pomme rapporte **1 point** et fait grandir le serpent.
- À chaque pomme mangée, le serpent **accélère** (jusqu'à une vitesse maximale).
- La partie est perdue si le serpent touche un **mur** ou **son propre corps**.
- Le **record** de la session s'affiche à côté du score.

### Lancer le jeu

Il faut Python 3. Le module `turtle` est fourni avec Python : il n'y a rien à installer.

```bash
python Jeux/snake.py
```

### Commandes

| Touche                  | Action                          |
|-------------------------|---------------------------------|
| ↑ / `W`                 | Aller vers le haut              |
| ↓ / `S`                 | Aller vers le bas               |
| ← / `A`                 | Aller vers la gauche            |
| → / `D`                 | Aller vers la droite            |
| `Espace`                | Rejouer après avoir perdu       |

> Le serpent ne peut pas faire demi-tour directement (par exemple passer de droite à gauche).

### Fonctionnement du code

| Élément        | Rôle                                                                 |
|----------------|----------------------------------------------------------------------|
| `snake`        | Liste des coordonnées des cases du serpent (la tête en premier).      |
| `jeu`          | Dictionnaire avec la direction, le score, le record, la vitesse et l'état de la partie. |
| `new_pomme()`  | Place une nouvelle pomme au hasard, jamais sur le serpent.            |
| `change_dir()` | Change la direction en empêchant le demi-tour.                        |
| `boucle()`     | Fait avancer le serpent, gère les collisions et les pommes, puis se relance avec `ontimer`. |
| `affiche()`    | Dessine la pomme, le serpent, le score et le message de fin.          |
| `restart()`    | Remet tout à zéro quand on appuie sur Espace après une défaite.       |

### Améliorations possibles

- Sauvegarder le record dans un fichier pour le garder entre deux lancements.
- Ajouter les touches `Z` / `Q` / `S` / `D` pour les claviers AZERTY.
- Ajouter un bouton pause.
