1.2 Using a data class provides better code readability with named attributes instead of positional parameters, and it enables easier future extensibility as new attributes can be added to the data class without changing existing method signatures.
1.3 Using an approach called forward referencing. Within training.py, we imported PokemonTrainingStats as a string.
1.4 The circular reference could be avoided by moving the shared data class (PokemanTrainingStats) to a separate module that both pokeman.py and training.py can import independently.

2.1.1 update_stats() accepts a dictionary with keyword arguments instead of the parameters themselves.
2.1.2 create a method get_attributes that takes a string argument to check what the user wants to access.
2.1.3 The program goes through a lot of checking for a simple get method

