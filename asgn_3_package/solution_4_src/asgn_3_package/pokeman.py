import time

from enum import Enum

from random import Random

from asgn_3_package.battle_system import CanBattle, BattleObjectData

from asgn_3_package.training import (
    Trainable,
    TrainingStatusObserver,
)


class PokemanType(Enum):
    FIRE = 1
    WATER = 2
    GRASS = 3
    ELECTRIC = 4
    UNKNOWN = 999


class Pokeman(Trainable, CanBattle):
    MAX_LEVEL = 4

    def __init__(self, name: str):
        """
        name: The name of the pokeman
        """

        # All attributes are private, please do not access them directly
        self._name = name
        self._level = 0
        self._hp = 10
        self._attack = 0
        self._defense = 0
        self._speed = 0
        self._type = PokemanType.UNKNOWN
        self._training_observers: list[TrainingStatusObserver] = []
        self._myself = self

    def determine_type(self):
        """
        Determine the type of this Pokeman

        The type of Pokeman is unknown when it was born. After being trained to a certain level,
        the type will become determinable. The exact determination procedure is magic.
        """
        match self._level:
            case 0 | 1 | 2:
                self._type = PokemanType.UNKNOWN
            case 3 | 4:
                rand = Random()
                rand_index = rand.randint(0, rand.randint(3, 4))
                types = [
                    PokemanType.FIRE,
                    PokemanType.GRASS,
                    PokemanType.GRASS,
                    PokemanType.ELECTRIC,
                    PokemanType.UNKNOWN,
                ]
                self._type = types[rand_index]

    def get_name(self) -> str:
        return self._name

    def get_level(self) -> int:
        return self._level

    def get_hp(self):
        return self._hp

    def get_attack(self):
        return self._attack

    def get_defense(self):
        return self._defense

    def get_speed(self):
        return self._speed

    def get_type(self):
        return self._type

    def set_myself(self, myself):
        """
        A function to set myself back, just in case I have got lost...
        """
        self._myself = myself

    def __str__(self) -> str:
        return f"{self._name}: Level {self._level}, HP {self._hp}, Attack {self._attack}, Defense {self._defense}, Speed {self._speed}, Type {self._type}"

    def practice(self, duration: int):
        """
        Practice the pokeman for a certain amount of time

        When the practice is complete, the observers are notified

        time: int: The amount of time to practice in seconds
        """

        if self != self._myself:
            raise Exception("I am not myself!")

        print(f"  {self._name} is practicing for {duration} seconds")

        # Simulate the practice
        time.sleep(duration)

        for observer in self._training_observers:
            observer.finished_training(self._myself)

    def update_stats(self, level: int, hp: int, attack: int, defence: int, speed: int):
        self._level = level
        self._hp = hp
        self._attack = attack
        self._defense = defence
        self._speed = speed

    def get_cur_level(self) -> int:
        return self.get_level()

    def add_training_observer(self, observer: TrainingStatusObserver):
        if observer in self._training_observers:
            return
        self._training_observers.append(observer)

    def attack(self, other: "CanBattle") -> int:
        """
        Attack the other contestant and return the damage dealt
        """
        damage = self.get_attack()
        other.take_damage(damage)
        return damage
    
    def take_damage(self, damage: int):
        """
        Take damage from an attack
        """
        self._hp -= damage

    def get_data_for_battle(self) -> BattleObjectData:
        """
        Return the data of the object for battle
        """
        return BattleObjectData(self._hp, self._attack, self._defense, self._speed, self._type)


class SoftEngPokeman:
    """
    A new type that is not related to Pokeman in any way
    But the author of this class wants to treat it as a Pokeman,
    and let it participate in the Pokeman Battle...
    """

    def __init__(self, name: str):
        self._name = name
        self._level = 0
        self._hp = 10
        self._attack = 0
        self._defense = 0
        self._speed = 0

    def get_hp(self):
        return self._hp

    def set_hp(self, hp: int):
        self._hp = hp

    def get_attack(self):
        return self._attack

    def get_defense(self):
        return self._defense

    def get_name(self) -> str:
        return self._name

    def get_cur_level(self):
        return self._level

    def __str__(self) -> str:
        return f"{self._name}: Level {self._level}, HP {self._hp}, Attack {self._attack}, Defense {self._defense}, Speed {self._speed}"

    def update_stats(self, level: int, hp: int, attack: int, defence: int, speed: int):
        self._level = level
        self._hp = hp
        self._attack = attack
        self._defense = defence
        self._speed = speed

        print(f"{self._name} has been upgraded without any practice!")
        print(self)


# ---------------------------------------------------------------------------------------
