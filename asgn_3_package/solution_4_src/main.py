from asgn_3_package.pokeman_gym import PokemanGym
from asgn_3_package.pokeman import Pokeman, SoftEngPokeman
from asgn_3_package.battle_system import BattleSystem, BattleConfig
from asgn_3_package.softeng_pokeman_trainer import create_proxy

pokeman_gym = PokemanGym()

pikachu = Pokeman("Pikachu")

# Train until the pokeman reaches the max level
while pikachu.get_level() < Pokeman.MAX_LEVEL:
    pokeman_gym.train_pokeman(pikachu)
    print(pikachu)

ChuKaPi = Pokeman("ChuKaPi")

while ChuKaPi.get_level() < Pokeman.MAX_LEVEL:
    pokeman_gym.train_pokeman(ChuKaPi)
    print(ChuKaPi)

# Create a SoftEngPokeman
Kei = SoftEngPokeman("Kei")
# Create a proxy for training the SoftEngPokeman
proxy = create_proxy(Kei)

# Train until max level
while Kei.get_cur_level() < Pokeman.MAX_LEVEL:
    pokeman_gym.train_pokeman(proxy)

battle_system = BattleSystem(BattleConfig(num_rounds=3))
print(battle_system.battle(ChuKaPi, proxy))

