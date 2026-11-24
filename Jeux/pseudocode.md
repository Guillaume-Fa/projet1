debut
demander niveau tant que pas 1 2 ou 3
record = lire fichier sinon 0

serpent = 3 cases
pomme = random

tant que pas perdu
    avancer tete
    si mur ou corps -> perdu
    si pomme -> score + 1 et nouvelle pomme
    sinon -> enlever queue
    dessiner grille
fin

si score > record -> sauver record
espace = rejouer
fin