class GameCharacter:
    def __init__(self, name, health, attack_power, defense):
        self.__name = None
        self.__health = None
        self.__max_health = health
        self.__attack_power = None
        self.__defense = None
        self.level = 1

        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Ім'я не може бути порожнім.")
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            value = 0
        if value > self.__max_health:
            value = self.__max_health
        self.__health = value

    @property
    def max_health(self):
        return self.__max_health

    @property
    def attack_power(self):
        return self.__attack_power

    @attack_power.setter
    def attack_power(self, value):
        if value <= 0:
            raise ValueError("Сила атаки має бути > 0.")
        self.__attack_power = value

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, value):
        if value < 0:
            raise ValueError("Захист не може бути від'ємним.")
        self.__defense = value

    def attack(self, target):
        print(f"{self.name} атакує {target.name} з силою {self.attack_power}!")
        target.take_damage(self.attack_power)

    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.health -= actual_damage

        print(f"{self.name} отримав {actual_damage} пошкоджень. "
              f"Здоров'я: {self.health}/{self.max_health}")

        if self.health == 0:
            print(f"{self.name} помер!")

    def is_alive(self):
        return self.health > 0

    def level_up(self):
        self.level += 1
        self.__max_health += 10
        self.health = self.__max_health
        self.attack_power += 5
        self.defense += 2
        print(f"{self.name} піднявся до {self.level} рівня!")

    def get_info(self):
        status = "живий" if self.is_alive() else "мертвий"
        print(f"Персонаж: {self.name} ({status})")
        print(f"Рівень: {self.level}")
        print(f"Здоров'я: {self.health}/{self.max_health}")
        print(f"Сила атаки: {self.attack_power}")
        print(f"Захист: {self.defense}")


hero = GameCharacter("Белегар", 100, 20, 10)
enemy = GameCharacter("Горбак", 120, 15, 3)

hero.get_info()
enemy.get_info()

print("\nПочаток бою")

while hero.is_alive() and enemy.is_alive():
    hero.attack(enemy)
    if enemy.is_alive():
        enemy.attack(hero)

print("\nБій закінчено")

hero.level_up()

print("\nПісля підвищення рівня")
hero.get_info()
