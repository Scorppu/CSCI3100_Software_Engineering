1.2 Using a data class provides better readability through named fields (stats.level vs tuple[0]), making code more self-documenting and reducing potential errors from parameter ordering confusion. It also enhances extensibility, allowing new stats to be added to the class without breaking existing method signatures, making the code more maintainable as requirements evolve.
1.3 Using an approach called forward referencing. Within training.py, we imported PokemonTrainingStats as a string.
1.4 idfk

2.1.1 update_stats() accepts a dictionary with keyword arguments instead of the parameters themselves.
2.1.2 create a method get_attributes that takes a string argument to check what the user wants to access.
2.1.3 The program goes through a lot of checking for a simple get method

