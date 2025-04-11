import time
from asgn_3_package.training import TrainingStatusObserver
from asgn_3_package.pokeman import Pokeman, PokemanType

class PokemanProxy(Pokeman):
    def __init__(self, softeng_pokeman):

        super().__init__(softeng_pokeman.get_name())
        self.softeng_pokeman = softeng_pokeman
        
    def practice(self, duration: int):

        print(f"  {self._name} is practicing for {duration} seconds")
        time.sleep(duration)
        
        # Important: temporarily set myself to the SoftEngPokeman before notification
        for observer in self._training_observers:
            # This is the key trick: we're passing the SoftEngPokeman instead of self
            observer.finished_training(self.softeng_pokeman)

def create_proxy(softeng):

    # Create a proxy that will handle all Pokeman-specific requirements
    proxy = PokemanProxy(softeng)
    return proxy
