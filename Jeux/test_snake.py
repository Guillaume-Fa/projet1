import pytest

import snake


def test_grille():
    grille = snake.creer_grille([(1, 1), (0, 1)], (2, 0))
    assert len(grille) == snake.CASES
    assert grille[1][1] == "T"
    assert grille[1][0] == "S"
    assert grille[0][2] == "P"
    assert grille[5][5] == "."


def test_pomme_pas_sur_serpent():
    serpent = [(0, 0), (1, 0), (2, 0)]
    for i in range(50):
        assert snake.nouvelle_pomme(serpent) not in serpent


def test_pas_de_demi_tour():
    assert snake.changer_direction("droite", "gauche") == "droite"
    assert snake.changer_direction("droite", "haut") == "haut"


def test_avancer():
    serpent = [(5, 5), (4, 5), (3, 5)]
    assert snake.deplacer(serpent, "droite", (0, 0)) == "ok"
    assert serpent == [(6, 5), (5, 5), (4, 5)]


def test_manger():
    serpent = [(5, 5), (4, 5), (3, 5)]
    assert snake.deplacer(serpent, "droite", (6, 5)) == "mange"
    assert len(serpent) == 4


def test_mur():
    serpent = [(24, 5), (23, 5), (22, 5)]
    assert snake.deplacer(serpent, "droite", (0, 0)) == "perdu"


def test_corps():
    serpent = [(5, 5), (5, 6), (4, 6), (4, 5), (4, 4)]
    assert snake.deplacer(serpent, "gauche", (0, 0)) == "perdu"


def test_niveau_valide():
    assert snake.valider_niveau("2") == 2


def test_niveau_invalide():
    with pytest.raises(ValueError):
        snake.valider_niveau("abc")
    with pytest.raises(ValueError):
        snake.valider_niveau("5")


def test_record(tmp_path):
    fichier = tmp_path / "record.txt"
    assert snake.charger_record(fichier) == 0
    snake.sauvegarder_record(12, fichier)
    assert snake.charger_record(fichier) == 12
