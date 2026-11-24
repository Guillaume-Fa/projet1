import random
import turtle

TAILLE = 20
CASES = 25

#les directions du joeur

directions = {
    "haut": (0, -1),
    "bas": (0, 1),
    "gauche": (-1, 0),
    "droite": (1, 0),
}

opposes = {
    "haut": "bas",
    "bas": "haut",
    "gauche": "droite",
    "droite": "gauche",
}

#input du joueur

touches = {
    "w": "haut",
    "s": "bas",
    "a": "gauche",
    "d": "droite",
}

#niveaux que le joeur chosii

niveaux = {
    1: 150,
    2: 100,
    3: 60,
}

#couleurs du serpent et de la pomme

couleurs = {
    "T": "lime",
    "S": "green",
    "P": "red",
}

#céation du jeux et du serpent

def creer_grille(serpent, pomme):
    grille = []
    for y in range(CASES):
        ligne = []
        for x in range(CASES):
            ligne.append(".")
        grille.append(ligne)
    grille[pomme[1]][pomme[0]] = "P"
    for x, y in serpent:
        grille[y][x] = "S"
    tete = serpent[0]
    grille[tete[1]][tete[0]] = "T"
    return grille

#Incorporer une pomme à un endroit random

def nouvelle_pomme(serpent):
    while True:
        pomme = (random.randint(0, CASES - 1), random.randint(0, CASES - 1))
        if pomme not in serpent:
            return pomme

#changer la direction selon les input du joueur

def changer_direction(actuelle, nouvelle):
    if nouvelle == opposes[actuelle]:
        return actuelle
    return nouvelle

#vérifie si le joeur entre en contact avec le corps ou mange une pomme

def deplacer(serpent, direction, pomme):
    dx, dy = directions[direction]
    tete = (serpent[0][0] + dx, serpent[0][1] + dy)
    if tete[0] < 0 or tete[0] >= CASES or tete[1] < 0 or tete[1] >= CASES:
        return "perdu"
    if tete in serpent[:-1]:
        return "perdu"
    serpent.insert(0, tete)
    if tete == pomme:
        return "mange"
    serpent.pop()
    return "ok"

#+1 au corps quand le joeur mange une pomme

def nouvelle_partie(vitesse, record):
    serpent = [(12, 12), (11, 12), (10, 12)]
    return {
        "serpent": serpent,
        "pomme": nouvelle_pomme(serpent),
        "direction": "droite",
        "prochaine": "droite",
        "score": 0,
        "record": record,
        "vitesse": vitesse,
        "fini": False,
    }

#vérifier que le joueur choisi les niveaux de 1 à 3

def valider_niveau(texte):
    niveau = int(texte)
    if niveau not in niveaux:
        raise ValueError("niveau invalide")
    return niveau

#demander au joueur le niveau 1 à 3

def demander_niveau():
    while True:
        try:
            return valider_niveau(input("Choisis un niveau (1, 2 ou 3) : "))
        except ValueError:
            print("Erreur : écris 1, 2 ou 3.")

#record quand le joueur meurt

def charger_record(fichier="record.txt"):
    try:
        with open(fichier) as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0

def sauvegarder_record(record, fichier="record.txt"):
    with open(fichier, "w") as f:
        f.write(str(record))

#Affichage

def dessiner_carre(x, y, couleur):
    stylo.goto(x * TAILLE - 250, 230 - y * TAILLE)
    stylo.color(couleur)
    stylo.begin_fill()
    for i in range(4):
        stylo.forward(TAILLE)
        stylo.left(90)
    stylo.end_fill()


def afficher():
    stylo.clear()
    grille = creer_grille(jeu["serpent"], jeu["pomme"])
    for y in range(CASES):
        for x in range(CASES):
            case = grille[y][x]
            if case in couleurs:
                dessiner_carre(x, y, couleurs[case])
    stylo.color("white")
    stylo.goto(0, 260)
    stylo.write("Score : " + str(jeu["score"]) + "   Record : " + str(jeu["record"]),
                align="center", font=("Arial", 14, "bold"))
    if jeu["fini"]:
        stylo.goto(0, 0)
        stylo.write("PERDU ! Appuie sur Espace", align="center", font=("Arial", 20, "bold"))
    ecran.update()

#augmenter le score quand le joueur mange une pomme

def boucle():
    jeu["direction"] = jeu["prochaine"]
    resultat = deplacer(jeu["serpent"], jeu["direction"], jeu["pomme"])
    if resultat == "mange":
        jeu["score"] += 1
        jeu["pomme"] = nouvelle_pomme(jeu["serpent"])
    if resultat == "perdu":
        jeu["fini"] = True
        if jeu["score"] > jeu["record"]:
            jeu["record"] = jeu["score"]
            sauvegarder_record(jeu["record"])
    afficher()
    if not jeu["fini"]:
        ecran.ontimer(boucle, jeu["vitesse"])


def appuyer(sens):
    jeu["prochaine"] = changer_direction(jeu["direction"], sens)


def recommencer():
    if jeu["fini"]:
        jeu.update(nouvelle_partie(jeu["vitesse"], jeu["record"]))
        boucle()


if __name__ == "__main__":
    niveau = demander_niveau()
    jeu = nouvelle_partie(niveaux[niveau], charger_record())

    ecran = turtle.Screen()
    ecran.title("Snake")
    ecran.setup(560, 600)
    ecran.bgcolor("black")
    ecran.tracer(0)

    bord = turtle.Turtle()
    bord.hideturtle()
    bord.color("white")
    bord.penup()
    bord.goto(-250, 250)
    bord.pendown()
    for i in range(4):
        bord.forward(CASES * TAILLE)
        bord.right(90)

    stylo = turtle.Turtle()
    stylo.hideturtle()
    stylo.penup()

    for touche, sens in touches.items():
        ecran.onkey(lambda s=sens: appuyer(s), touche)
    ecran.onkey(recommencer, "space")
    ecran.listen()

    boucle()
    ecran.mainloop()
