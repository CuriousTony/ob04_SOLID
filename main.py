from abc import ABC, abstractmethod
from random import randint


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        score = randint(25, 50)
        print(f"Удар мечом наносит страшную рану, нанося противнику {score} очков урона!")
        return score


class Bow(Weapon):
    def attack(self):
        score = randint(15, 30)
        print(f"Выстрел из лука причиняет противнику мучения, нанося {score} урона!")
        return score


class Bazooka(Weapon):
    def attack(self):
        score = randint(60,100)
        print(f"Выстрел из базуки оглушает всех присутствующих, нанося цели {score} урона.")
        return score


class Fighter:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self, target):
        print(f"{self.name.title()} атакует!")
        target.get_damage(self.weapon.attack())

    def change_weapon(self, new_weapon):
        print(f"{self.name.title()} сменил оружие!")
        self.weapon = new_weapon


class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def get_damage(self, damage):
        if self.hp > 0:
            self.hp -= damage
            print(f"Остаток очков здоровья {self.name.title()} {self.hp}hp.")
        if self.hp <= 0:
            print(f"Монстр по имени {self.name.title()} не выдержал такого "
                  f"напора и отъехал в мир иной.")


sword = Sword()
bow = Bow()
bazooka = Bazooka()


monster = Monster('sqeegl', 100)
swordsman = Fighter('titus', sword)
swordsman.attack(monster)
swordsman.change_weapon(bow)
swordsman.attack(monster)
swordsman.change_weapon(bazooka)
swordsman.attack(monster)
