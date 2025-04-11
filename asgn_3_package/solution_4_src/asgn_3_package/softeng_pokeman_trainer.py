import time
from asgn_3_package.training import TrainingStatusObserver
from asgn_3_package.pokeman import Pokeman, PokemanType
from asgn_3_package.battle_system import BattleObjectData, CanBattle

class PokemanProxy(Pokeman):
    """
    A proxy class that forwards training updates to a SoftEngPokeman instance
    and also implements the CanBattle interface to allow SoftEngPokeman to battle.
    This allows a SoftEngPokeman to be trained by PokemanGym without inheritance.
    """
    def __init__(self, softeng_pokeman):
        super().__init__(softeng_pokeman.get_name())
        self.softeng_pokeman = softeng_pokeman
        
    def practice(self, duration: int):
        print(f"  {self._name} is practicing for {duration} seconds")
        time.sleep(duration)
        
        # Important: we're passing the SoftEngPokeman instead of self to the observer
        for observer in self._training_observers:
            observer.finished_training(self.softeng_pokeman)
            
    def attack(self, other: CanBattle) -> int:
        # Use SoftEngPokeman's attack value but handle the attack logic here
        damage = self.softeng_pokeman.get_attack()
        other.take_damage(damage)
        return damage
    
    def take_damage(self, damage: int):
        # Update SoftEngPokeman's HP
        self.softeng_pokeman.set_hp(max(0, self.softeng_pokeman.get_hp() - damage))
        
    def get_hp(self) -> int:
        return self.softeng_pokeman.get_hp()
        
    def get_data_for_battle(self) -> BattleObjectData:
        return BattleObjectData(
            self.softeng_pokeman.get_hp(),
            self.softeng_pokeman.get_attack(),
            self.softeng_pokeman.get_defense(),
            self.softeng_pokeman._speed,  # Accessing protected attribute
            None  # No type for SoftEngPokeman
        )

def create_proxy(softeng):
    # Create a proxy that will handle all Pokeman-specific requirements
    proxy = PokemanProxy(softeng)
    return proxy
