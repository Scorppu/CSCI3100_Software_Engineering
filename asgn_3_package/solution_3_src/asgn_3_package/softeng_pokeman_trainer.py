import time
from asgn_3_package.training import TrainingStatusObserver

def add_training_methods(softeng):
    """
    Add training-related methods to a SoftEngPokeman instance to make it compatible with PokemanGym.
    This uses duck typing to make the pokeman behave like a Trainable object.
    """
    # Store observers
    softeng._training_observers = []

    def practice(duration: int):
        """
        Practice for a certain amount of time and notify observers when done.
        """
        print(f"  {softeng.get_name()} is practicing for {duration} seconds")
        time.sleep(duration)
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

    # Add the methods to the softeng instance
    softeng.practice = practice
    softeng.add_training_observer = add_training_observer
    softeng.determine_type = determine_type

    return softeng
