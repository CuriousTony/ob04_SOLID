from abc import ABC, abstractmethod
from random import randint


class Creature(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def get_damage(self, damage_in):
        self.damage_in = damage_in
        pass

    @abstractmethod
    def attack(self):
        pass


class Monster(Creature):
    def __init__(self, name, health):
        super().__init__(name, health)

    def get_damage(self, damage_in):
        if self.health > 1:
            self.health -= damage_in
            print(f"Чудище {self.name.title()} получило {damage_in} урона.\n"
                  f"Оставшиеся очки здоровья - {self.health}.\n")
        elif self.health <= 0:
            print(f"{self.name.title()} падает замертво."
                  f"Смертельный удар нанес ему {self.damage_in} урона.")

    def attack(self, target):
        damage_out = randint(10, 40)
        print(f"Чудище {self.name.title()} наносит размашистый удар!")
        target.get_damage(damage_out)


class Knight(Creature):
    def __init__(self, name, health):
        super().__init__(name, health)

    def get_damage(self, damage_in):
        if self.health >= 1:
            self.health -= damage_in
            print(f"Рыцарь {self.name.title()} получил {damage_in} урона.\n"
                  f"Оставшиеся очки здоровья - {self.health}.\n")
        elif self.health <= 0:
            print(f"Рыцарь {self.name.title()} падает замертво."
                  f"Смертельный удар нанес ему {self.damage_in} урона.")

    def attack(self, target):
        damage_out = randint(10, 30)
        print(f"Рыцарь {self.name.title()} кровожадно громит врага.")
        target.get_damage(damage_out)


knight = Knight('Титус', 100)
monster = Monster('Мргл-мргл', 120)

knight.attack(monster)
monster.attack(knight)

# class Weapon(ABC):
#     @abstractmethod
#     def hit_target(self):
#         pass
