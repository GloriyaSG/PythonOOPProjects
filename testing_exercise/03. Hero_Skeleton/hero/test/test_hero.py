from unittest import TestCase, main

from project.hero import Hero

class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Batman", 100, 50.5, 75.5)

    def test_initalize(self):
        self.assertEqual(self.hero.username, "Batman")
        self.assertEqual(self.hero.level, 100)
        self.assertEqual(self.hero.health, 50.5)
        self.assertEqual(self.hero.damage, 75.5)

    def test_battle_for_usernames(self):
        enemy = self.hero
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_for_hero_health(self):
        with self.assertRaises(ValueError) as ex:
            self.hero.health = -1
            enemy = Hero("Spiderman", 100, 50.5, 75.5)
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_for_enemy_health(self):

        with self.assertRaises(ValueError) as ex:
            enemy = Hero("Spiderman", 100, -1, 75.5)
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Spiderman. He needs to rest", str(ex.exception))

    def test_battle_for_draw(self):
        enemy = Hero("Spiderman", 100, 50.5, 75.5)
        self.assertEqual(self.hero.battle(enemy), "Draw")

    def test_battle_for_win(self):
        enemy = Hero("Spiderman", 0, 9.5, 0.5)
        result = self.hero.battle(enemy)
        self.assertEqual(result, "You win")
        self.assertEqual(101, self.hero.level)
        self.assertEqual(55.5, self.hero.health)
        self.assertEqual(80.5, self.hero.damage)
        #"Batman", 100, 50.5, 75.5


    def test_battle_for_lose(self):
        enemy = Hero("Spiderman", 100, 90.6, 90.5)
        self.hero = Hero("Batman", 0, 0.5, 0.5)
        result = self.hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(101, enemy.level)
        self.assertEqual(95.6, enemy.health)
        self.assertEqual(95.5, enemy.damage)

    def test_if_str_method_return_correct(self):
        result = f"Hero Batman: 100 lvl\n" \
               f"Health: 50.5\n" \
               f"Damage: 75.5\n"
        self.assertEqual(result, str(self.hero))

if __name__ == "__main__":
    main()