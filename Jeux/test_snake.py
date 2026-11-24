import os
import tempfile
import unittest

import snake


class TestSnake(unittest.TestCase):

    def test_grille(self):
        grille = snake.creer_grille([(1, 1), (0, 1)], (2, 0))
        self.assertEqual(len(grille), snake.CASES)
        self.assertEqual(grille[1][1], "T")
        self.assertEqual(grille[1][0], "S")
        self.assertEqual(grille[0][2], "P")
        self.assertEqual(grille[5][5], ".")

    def test_pomme_pas_sur_serpent(self):
        serpent = [(0, 0), (1, 0), (2, 0)]
        for i in range(50):
            self.assertNotIn(snake.nouvelle_pomme(serpent), serpent)

    def test_pas_de_demi_tour(self):
        self.assertEqual(snake.changer_direction("droite", "gauche"), "droite")
        self.assertEqual(snake.changer_direction("droite", "haut"), "haut")

    def test_avancer(self):
        serpent = [(5, 5), (4, 5), (3, 5)]
        self.assertEqual(snake.deplacer(serpent, "droite", (0, 0)), "ok")
        self.assertEqual(serpent, [(6, 5), (5, 5), (4, 5)])

    def test_manger(self):
        serpent = [(5, 5), (4, 5), (3, 5)]
        self.assertEqual(snake.deplacer(serpent, "droite", (6, 5)), "mange")
        self.assertEqual(len(serpent), 4)

    def test_mur(self):
        serpent = [(24, 5), (23, 5), (22, 5)]
        self.assertEqual(snake.deplacer(serpent, "droite", (0, 0)), "perdu")

    def test_corps(self):
        serpent = [(5, 5), (5, 6), (4, 6), (4, 5), (4, 4)]
        self.assertEqual(snake.deplacer(serpent, "gauche", (0, 0)), "perdu")

    def test_niveau_valide(self):
        self.assertEqual(snake.valider_niveau("2"), 2)

    def test_niveau_invalide(self):
        with self.assertRaises(ValueError):
            snake.valider_niveau("abc")
        with self.assertRaises(ValueError):
            snake.valider_niveau("5")

    def test_record(self):
        fichier = os.path.join(tempfile.mkdtemp(), "record.txt")
        self.assertEqual(snake.charger_record(fichier), 0)
        snake.sauvegarder_record(12, fichier)
        self.assertEqual(snake.charger_record(fichier), 12)


if __name__ == "__main__":
    unittest.main()
