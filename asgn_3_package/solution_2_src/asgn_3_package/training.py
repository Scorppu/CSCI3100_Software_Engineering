from abc import ABC, abstractmethod


class TrainingStatusObserver(ABC):
    """
    An interface of expected functions for observing the training status of an object
    """

    @abstractmethod
    def finished_training(self, obj: "Trainable"):
        """
        When the obj is trained, this method is called
        """


class Trainable(ABC):
    """
    An interface of expected functions that an object that can be trained should provide
    """

    @abstractmethod
    def add_training_observer(self, observer: TrainingStatusObserver):
        """
        Adds an observer to the object
        """

    def practice(self, duration: int):
        """
        Practise for a certain amount of time

        When the practice is complete, the observers are notified

        time: int: The amount of time to practice in seconds
        """

    @abstractmethod
    def update_stats(self, stats: dict[str, any]):
        """
        Update the stats after training
        
        Args:
            stats: A dictionary containing the attributes to update
                  Each key is the attribute name, value is the new value
        """

    @abstractmethod
    def get_attribute(self, attribute_name: str) -> any:
        """
        Get any attribute of the object
        
        Args:
            attribute_name: The name of the attribute to get
            
        Returns:
            The value of the requested attribute
        """

    @abstractmethod
    def get_cur_level(self) -> int:
        """
        Get the current level of the object
        """

    @abstractmethod
    def get_name(self) -> str:
        """
        Get the object's name
        """
