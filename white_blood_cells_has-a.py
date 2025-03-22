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
        return self.__enemy == enemy

    def kill_enemy(self, enemy: Enemy) -> bool:
        if self.can_kill_enemy(enemy):
            print(f"Antibody killing {enemy}")
            return True
        return False

class WhiteBloodCell:
    def is_enemy(self, antigens: List[Antigen]) -> bool:
        print(f"WhiteBloodCell checking if antigens {antigens} are an enemy")
        return True

    def kill(self, enemy: Enemy) -> bool:
        print(f"WhiteBloodCell trying to kill {enemy}")
        return True

class Neutrophils:
    def __init__(self):
        self.white_blood_cell = WhiteBloodCell()

    def is_enemy(self, antigens: List[Antigen]) -> bool:
        return self.white_blood_cell.is_enemy(antigens)

    def kill(self, enemy: Enemy) -> bool:
        return self.white_blood_cell.kill(enemy)

class Lymphocytes:
    def __init__(self):
        self.white_blood_cell = WhiteBloodCell()

    def is_enemy(self, antigens: List[Antigen]) -> bool:
        return self.white_blood_cell.is_enemy(antigens)

    def kill(self, enemy: Enemy) -> bool:
        return self.white_blood_cell.kill(enemy)

class NKCell:
    def __init__(self):
        self.lymphocyte = Lymphocytes()

    def is_enemy(self, antigens: List[Antigen]) -> bool:
        return self.lymphocyte.is_enemy(antigens)

    def kill(self, enemy: Enemy) -> bool:
        return self.lymphocyte.kill(enemy)

class BCell:
    def __init__(self):
        self.lymphocyte = Lymphocytes()

    def is_enemy(self, antigens: List[Antigen]) -> bool:
        return self.lymphocyte.is_enemy(antigens)

    def kill(self, enemy: Enemy) -> bool:
        return self.lymphocyte.kill(enemy)

    def make_antibodies(self, enemy: Enemy) -> Antibody:
        return Antibody(enemy)

    def ask_helper_t_cell_make_antibodies(self, helper_t_cell: 'HelperTCell'):
        print("BCell asking HelperTCell to make antibodies")

class TCell:
    def __init__(self):
        self.lymphocyte = Lymphocytes()
        self.is_activated = False

    def is_enemy(self, antigens: List[Antigen]) -> bool:
        return self.lymphocyte.is_enemy(antigens)

    def kill(self, enemy: Enemy) -> bool:
        return self.lymphocyte.kill(enemy)

class HelperTCell:
    def __init__(self):
        self.t_cell = TCell()
        self.__enemy_to_characteristics = {}

    def is_enemy(self, antigens: List[Antigen]) -> bool:
        return self.t_cell.is_enemy(antigens)

    def kill(self, enemy: Enemy) -> bool:
        return self.t_cell.kill(enemy)

    def get_enemy_characteristics(self, enemy: Enemy) -> List[float]:
        return self.__enemy_to_characteristics.get(enemy, [])
