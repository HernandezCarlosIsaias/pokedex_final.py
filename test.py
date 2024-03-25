from pokedex import *

#test si la listas estan vacias
pokemon = Pokedex()
assert pokemon.contar_entrenador() == 0

pokemon = Pokedex()
assert pokemon.contar_pokemon() == 0

# test agregar contacto
pokemon.agregar_pokemon(1,"Pikachu","electrico","agua","tiernito y pachonchito","Raichu")
assert pokemon.contar_pokemon() == 1

#test agregar entrenador
pokemon.agregar_entrenador("Emiliano", 2 , "Cordoba", "Charizard")
assert pokemon.contar_entrenador() == 1
