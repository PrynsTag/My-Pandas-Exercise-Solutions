# # Pokemon
# ### Introduction:
# This time you will create the data.
# ### Step 1. Import the necessary libraries
import pandas as pd
# ### Step 2. Create a data dictionary that looks like the DataFrame below
pd.DataFrame({"evolution" : ["Ivysaur", "Charmeleon", "Watortle", "Metapod"], 
            "hp" : [45 ,39, 44, 45], 
            "name" : ["Bulbasaur", "Charmander", "Squirtle", "Caterpie"], 
            "pokedex" : ["yes", "no", "yes", "no"], 
            "type" : ["grass", "fire", "water", "bug"]})              
# ### Step 3. Assign it to a variable called pokemon
pokemon = pd.DataFrame({"evolution" : ["Ivysaur", "Charmeleon", "Watortle", "Metapod"], 
            "hp" : [45 ,39, 44, 45], 
            "name" : ["Bulbasaur", "Charmander", "Squirtle", "Caterpie"], 
            "pokedex" : ["yes", "no", "yes", "no"], 
            "type" : ["grass", "fire", "water", "bug"]})              
# ### Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place  the order of the columns as name, type, hp, evolution, pokedex
pokemon = pokemon.reindex(columns=["name", "type", "hp", "evolution", "pokedex"])
pokemon.head()
# ### Step 5. Add another column called place, and insert what you have in mind.
pokemon["place"] = ["Manila", "Baguio", "Cainta", "Taguig"]
pokemon.head()
# ### Step 6. Present the type of each column
pokemon.dtypes
# ### Display only the pokemons who are in the pokedex.
pokemon[pokemon["pokedex"] == "yes"]
