import pandas as pd

# Step 2
raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']                        
            }

# Step 3
pokemon = pd.DataFrame(raw_data)
print(pokemon)

# Step 4
pokemon = pokemon[['name', 'type', 'hp', 'evolution', 'pokedex']]
print(pokemon)

# Step 5
pokemon['place'] = ['park', 'street', 'lake', 'forest']
print(pokemon)

# Step 6
print(pokemon.dtypes)
