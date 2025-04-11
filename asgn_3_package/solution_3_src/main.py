from asgn_3_package.pokeman_gym import PokemanGym
from asgn_3_package.pokeman import Pokeman, SoftEngPokeman
from asgn_3_package.softeng_pokeman_trainer import create_proxy


pokeman_gym = PokemanGym()

# Train until the pokeman reaches the max level
pikachu = Pokeman("Pikachu")
while pikachu.get_level() < Pokeman.MAX_LEVEL:
    pokeman_gym.train_pokeman(pikachu)
    print(pikachu)

# Create a SoftEngPokeman
softeng = SoftEngPokeman("SoftEng")

# Get a proxy that can be trained but updates the SoftEngPokeman
proxy = create_proxy(softeng)

# Train until max level
while softeng.get_cur_level() < Pokeman.MAX_LEVEL:
    pokeman_gym.train_pokeman(proxy)

