from asgn_3_package.pokeman_gym import PokemanGym
from asgn_3_package.pokeman import Pokeman, SoftEngPokeman
from asgn_3_package.softeng_pokeman_trainer import add_training_methods

pokeman_gym = PokemanGym()

# Create and train a regular Pokeman
pikachu = Pokeman("Pikachu")
while pikachu.get_level() < Pokeman.MAX_LEVEL:
    pokeman_gym.train_pokeman(pikachu)
    print(pikachu)

# Create and train a SoftEngPokeman
softeng = SoftEngPokeman("SoftEng")
# Add training methods using duck typing
softeng = add_training_methods(softeng)
# Train until max level
while softeng.get_cur_level() < Pokeman.MAX_LEVEL:
    pokeman_gym.train_pokeman(softeng)
