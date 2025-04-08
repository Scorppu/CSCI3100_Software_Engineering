import time
from asgn_3_package.training import TrainingStatusObserver
from asgn_3_package.battle_system import BattleObjectData, CanBattle

def add_training_methods(softeng):
    """
    Add training-related methods to a SoftEngPokeman instance to make it compatible with PokemanGym.
    This uses duck typing to make the pokeman behave like a Trainable object.
    """
    # Store observers
    softeng._training_observers = []
    # Add a flag to track training completion
    softeng._training_complete = False

    def practice(duration: int):
        """
        Practice for a certain amount of time and notify observers when done.
        """
        print(f"  {softeng.get_name()} is practicing for {duration} seconds")
        # Set training as not complete
        softeng._training_complete = False
        time.sleep(duration)
        # Set training as complete
        softeng._training_complete = True
        # Notify observers
        for observer in softeng._training_observers:
            observer.finished_training(softeng)

    def add_training_observer(observer: TrainingStatusObserver):
        """
        Add an observer to be notified when training is complete.
        """
        if observer not in softeng._training_observers:
            softeng._training_observers.append(observer)

    def determine_type():
        """
        No-op since SoftEngPokeman doesn't have types.
        """
        pass

    def attack(other: CanBattle) -> int:
        """
        Attack the other contestant and return the damage dealt
        """
        # Access the attack attribute directly
        attack_value = softeng._attack
        other.take_damage(attack_value)
        return attack_value

    def take_damage(damage: int):
        """
        Take damage from an attack by reducing HP.
        """
        # Access HP attribute directly
        softeng._hp = max(0, softeng._hp - damage)

    def get_hp() -> int:
        """
        Get the current HP.
        """
        # Access HP attribute directly
        return softeng._hp

    def get_cur_level() -> int:
        """
        Get the current level.
        """
        return softeng._level

    def is_training_complete() -> bool:
        """
        Check if training is complete.
        """
        return softeng._training_complete

    def get_data_for_battle() -> BattleObjectData:
        """
        Return the data of the object for battle.
        """
        # Access attributes directly
        return BattleObjectData(softeng._hp, softeng._attack, softeng._defense, softeng._speed, None)

    # Add the methods to the softeng instance
    softeng.practice = practice
    softeng.add_training_observer = add_training_observer
    softeng.determine_type = determine_type
    softeng.attack = attack
    softeng.take_damage = take_damage
    softeng.get_hp = get_hp
    softeng.get_cur_level = get_cur_level
    softeng.is_training_complete = is_training_complete
    softeng.get_data_for_battle = get_data_for_battle

    return softeng
