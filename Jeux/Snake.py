import turtle
import random

taille = 20
larg = 600
haut = 600

dirs = {
    "haut": (0, taille),
    "bas": (0, -taille),
    "gauche": (-taille, 0),
    "droite": (taille, 0),
}

opposes = {
    "haut": "bas",
    "bas": "haut",
    "gauche": "droite",
    "droite": "gauche",
}

jeu = {
    "dir": "droite",
    "score": 0,
    "record": 0,
    "vit": 120,
    "fini": False,
}

snake = [(0, 0), (-20, 0), (-40, 0)]
pomme = [100, 100]

ecran = turtle.Screen()
ecran.title("Snake")
ecran.setup(larg, haut)
ecran.bgcolor("black")
ecran.tracer(0)

stylo = turtle.Turtle()
stylo.hideturtle()
stylo.penup()

txt = turtle.Turtle()
txt.hideturtle()
txt.penup()
txt.color("white")


def carre(x, y, coul):
    stylo.goto(x - taille / 2, y - taille / 2)
    stylo.color(coul)
    stylo.begin_fill()
    for i in range(4):
        stylo.forward(taille)
        stylo.left(90)
    stylo.end_fill()


def new_pomme():
    while True:
        x = random.randint(-14, 14) * taille
        y = random.randint(-14, 14) * taille
        if (x, y) not in snake:
            pomme[0] = x
            pomme[1] = y
            return


def change_dir(nouv):
    if nouv != opposes[jeu["dir"]]:
        jeu["dir"] = nouv


def restart():
    if jeu["fini"]:
        snake.clear()
        snake.extend([(0, 0), (-20, 0), (-40, 0)])
        jeu["dir"] = "droite"
        jeu["score"] = 0
        jeu["vit"] = 120
        jeu["fini"] = False
        new_pomme()
        boucle()


def affiche():
    stylo.clear()
    txt.clear()
    carre(pomme[0], pomme[1], "red")
    for i, bout in enumerate(snake):
        if i == 0:
            carre(bout[0], bout[1], "lime")
        else:
            carre(bout[0], bout[1], "green")
    txt.goto(0, haut / 2 - 40)
    txt.write("Score : " + str(jeu["score"]) + "   Record : " + str(jeu["record"]),
              align="center", font=("Arial", 16, "bold"))
    if jeu["fini"]:
        txt.goto(0, 0)
        txt.write("PERDU ! Appuie sur Espace", align="center", font=("Arial", 22, "bold"))
    ecran.update()


def boucle():
    dx, dy = dirs[jeu["dir"]]
    tete = snake[0]
    new_tete = (tete[0] + dx, tete[1] + dy)

    dehors_x = abs(new_tete[0]) > larg / 2 - taille
    dehors_y = abs(new_tete[1]) > haut / 2 - taille
    if dehors_x or dehors_y or new_tete in snake:
        jeu["fini"] = True
        if jeu["score"] > jeu["record"]:
            jeu["record"] = jeu["score"]
        affiche()
        return

    snake.insert(0, new_tete)

    if new_tete == (pomme[0], pomme[1]):
        jeu["score"] += 1
        if jeu["vit"] > 50:
            jeu["vit"] -= 5
        new_pomme()
    else:
        snake.pop()

    affiche()
    ecran.ontimer(boucle, jeu["vit"])


touches = {
    "Up": "haut",
    "Down": "bas",
    "Left": "gauche",
    "Right": "droite",
    "w": "haut",
    "s": "bas",
    "a": "gauche",
    "d": "droite",
}

for touche, d in touches.items():
    ecran.onkey(lambda d=d: change_dir(d), touche)
ecran.onkey(restart, "space")
ecran.listen()

new_pomme()
boucle()
ecran.mainloop()
