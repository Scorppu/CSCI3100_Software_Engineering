from abc import ABC, abstractmethod
from typing import List

class Antigen:
    pass

class Enemy:
    def __init__(self, has_been_seen_before: bool, antigens: List[Antigen]):
        self.has_been_seen_before = has_been_seen_before
        self.antigens = antigens

class Antibody:
    def __init__(self, enemy: Enemy):
        self.__enemy = enemy

    def set_enemy(self, enemy: Enemy):
        self.__enemy = enemy

    def can_kill_enemy(self, enemy: Enemy) -> bool:
        pass

    def kill_enemy(self, enemy: Enemy) -> bool:
        pass

class WhiteBloodCell(ABC):
    @abstractmethod
    def is_enemy(self, antigens: List[Antigen]) -> bool:
        pass

    @abstractmethod
    def kill(self, enemy: Enemy) -> bool:
        pass

class Neutrophils(WhiteBloodCell):
    def __init__(self):
        super().__init__()
    def kill(self, enemy: Enemy) -> bool:
        pass

    def is_enemy(self, antigens: List[Antigen]) -> bool:
        pass

class Lymphocytes(ABC):
    def __init__(self):
        super().__init__()
    def is_enemy(self, antigens: List[Antigen]) -> bool:
        pass

    def kill(self, enemy: Enemy) -> bool:
        pass

class NKCell(Lymphocytes):
    def __init__(self):
        super().__init__()
    pass

class BCell(Lymphocytes):
    def __init__(self):
        super().__init__()

    def make_antibodies(self, enemy: Enemy) -> 'Antibody':
        pass

    def ask_helper_t_cell_make_antibodies(self, helper_t_cell: 'HelperTCell'):
        pass  

class TCell(Lymphocytes):
    def __init__(self):
        super().__init__()
        self.is_activated = False

    def is_enemy(self, antigens: List[Antigen]) -> bool:
        pass

    def kill(self, enemy: Enemy) -> bool:
        pass

class HelperTCell(TCell):
    def __init__(self):
        super().__init__()
        self.__enemy_to_characteristics = {}

    def get_enemy_characteristics(self, enemy: Enemy) -> List[float]:
        pass