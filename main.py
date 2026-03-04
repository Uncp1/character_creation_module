from random import randint

from graphic_arts.start_game_banner import run_screensaver

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    BRIEF_DESC_CHAR_CLASS = "отважный любитель приключений"

    ATTACK_RANGE_VALUE = (1, 3)
    DEFENCE_RANGE_VALUE = (1, 5)

    SPECIAL_BUFF = 15
    SPECIAL_SKILL = "Удача"

    def __init__(self, name):
        self.name = name

    def attack(self):
        attack_value = DEFAULT_ATTACK + randint(*self.ATTACK_RANGE_VALUE)
        return f"{self.name} нанёс противнику урон, равный {attack_value}"

    def defence(self):
        defence_value = DEFAULT_DEFENCE + randint(*self.DEFENCE_RANGE_VALUE)
        return f"{self.name} блокировал {defence_value} ед. урона."

    def special(self):
        return (
            f"{self.name} применил специальное умение "
            f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".'
        )

    def __str__(self):
        return f"{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}."


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = " дерзкий воин ближнего боя. Сильный, выносливый и отважный"
    GREETING = "ты Воитель — великий мастер ближнего боя."
    ATTACK_RANGE_VALUE = (3, 5)
    DEFENCE_RANGE_VALUE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = "Выносливость"


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (
        " находчивый воин дальнего боя. Обладает высоким интеллектом"
    )
    GREETING = "ты Маг — превосходный укротитель стихий."
    ATTACK_RANGE_VALUE = (5, 10)
    DEFENCE_RANGE_VALUE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = "Атака"


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (
        " могущественный заклинатель. Черпает силы из природы, веры и духов"
    )
    GREETING = "ты Лекарь — чародей, способный исцелять раны."
    ATTACK_RANGE_VALUE = (-3, -1)
    DEFENCE_RANGE_VALUE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = "Защита"


def start_training(character):
    print(f"{character.name}, {character.GREETING}")
    print("Потренируйся управлять своими навыками.")
    print(
        "Введи одну из команд: attack — чтобы атаковать противника, "
        "defence — чтобы блокировать атаку противника или "
        "special — чтобы использовать свою суперсилу."
    )
    print("Если не хочешь тренироваться, введи команду skip.")
    cmd = None
    while cmd != "skip":
        cmd = input("Введи команду: ")
        if cmd == "attack":
            print(character.attack())
        if cmd == "defence":
            print(character.defence())
        if cmd == "special":
            print(character.special())
    return "Тренировка окончена."


def choice_char_class(char_name: str) -> Character:
    game_classes = {"warrior": Warrior, "mage": Mage, "healer": Healer}

    approve_choice = None

    while approve_choice != "y":
        selected_class = input(
            "Введи название персонажа, "
            "за которого хочешь играть: Воитель — warrior, "
            "Маг — mage, Лекарь — healer: "
        )
        char_class: Character = game_classes[selected_class](char_name)

        print(char_class)

        approve_choice = input(
            "Нажми (Y), чтобы подтвердить выбор, "
            "или любую другую кнопку, "
            "чтобы выбрать другого персонажа "
        ).lower()
    return char_class


def main():
    run_screensaver()
    print("Приветствую тебя, искатель приключений!")
    print("Прежде чем начать игру...")
    char_name = input("...назови себя: ")
    print(
        f"Здравствуй, {char_name}! "
        "Сейчас твоя выносливость — 80, атака — 5 и защита — 10."
    )
    print("Ты можешь выбрать один из трёх путей силы:")
    print("Воитель, Маг, Лекарь")
    character = choice_char_class(char_name)
    start_training(character)


if __name__ == "__main__":
    main()
