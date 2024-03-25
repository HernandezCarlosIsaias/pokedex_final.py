import pickle

class Pokemon:
    def __init__ (self, numero:int , nombre:str , tipo:str , debilidad:str , descripcion:str , evolucion:str):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.debilidad = debilidad
        self.descripcion = descripcion
        self.evolucion = evolucion
        
class Entrenador:
    def __init__(self, nombre:str , medallas:str , region:str , pokemonUsado:str ):
        #self.pokemones_capturados = [] #mejora en un futuro
        self.nombre = nombre
        self.medallas = medallas
        self.region = region
        self.pokemonUsado = pokemonUsado
        
    #def capturar_pokemon(self, pokemon):#mejora en un futuro
    #    self.pokemones_capturados.append(pokemon)#mejora en un futuro
        
                
class Pokedex:
    def __init__(self):
        self.pokemones = []
        self.entrenadores = []
        
      
#define si el pokemon a agregar esta o no        
    def contiene_pokemon(self,numero:int)->bool:
        esta = False
        for pokemon in self.pokemones:
            if pokemon.numero == numero:
                esta = True
        return esta

#define si el entrenedar a agregar esta o no
    def contiene_entrenador(self,nombre:str)->bool:
        esta = False
        for entrenador in self.entrenadores:
            if entrenador.nombre == nombre:#mejora en un futuro poner ID
                esta = True
        return esta


#contamos todos los entrenadores(Pruebas)
    def contar_entrenador(self):
        return len(self.entrenadores)

#contamos todos los pokemones (Pruebas)       
    def contar_pokemon(self):
        return len(self.pokemones)
                
#agregamos pokemones a la lista de la Pokedex  
    def agregar_pokemon(self, numero:int , nombre:str, tipo:str , debilidad:str , descripcion:str , evolucion:str ):
        pokemon = Pokemon(numero , nombre , tipo , debilidad , descripcion , evolucion )
        self.pokemones.append(pokemon)
        
#agregamos entrenadores en la lista de la Pokedex        
    def agregar_entrenador(self, nombre:str , medallas:str , region:str , pokemonUsado:str ):
        entrenador = Entrenador(nombre , medallas , region , pokemonUsado )
        self.entrenadores.append(entrenador)

#buscamos el nombre del pokemon en la lista de la pokedex
    def buscar_pokemon(self, nombre:str):
        for pokemon in self.pokemones:
            if pokemon.nombre == nombre:
                return pokemon.numero,pokemon.tipo,pokemon.debilidad,pokemon.descripcion,pokemon.evolucion
        return -1
    
#buscamos el nombre del entrenedar en la lista de la pokedex    
    def buscar_entrenador(self, nombre:str):
        for entrenador in self.entrenadores:
            if entrenador.nombre == nombre:
                return entrenador.medallas , entrenador.region, entrenador.pokemonUsado
        return -1
    
#Permite modificar todos los datos de los pokemones
    def modificar_pokemon(self, nombre,nuevo_nombre, nuevo_numero,nuevo_tipo,nuevo_debilidad,nuevo_descripcion,nuevo_evolucion):
        for pokemon in self.pokemones:
            if pokemon.nombre == nombre:
                pokemon.nombre = nuevo_nombre
                pokemon.numero = nuevo_numero
                pokemon.tipo = nuevo_tipo
                pokemon.debilidad = nuevo_debilidad
                pokemon.descripcion = nuevo_descripcion
                pokemon.evolucion = nuevo_evolucion
            
  
#Permite modificar todos los datos de los entrenadores
    def modificar_entrenador(self, nombre,nuevo_nombre ,nuevo_medalla ,nuevo_region,nuevo_pokemonUsado):
        for entrenador in self.entrenadores:
            if entrenador.nombre == nombre:
                entrenador.nombre = nuevo_nombre
                entrenador.medallas = nuevo_medalla
                entrenador.region = nuevo_region
                entrenador.pokemonUsado = nuevo_pokemonUsado

#permite eliminar un pokemon
    def eliminar_pokemon(self, nombre:str):
        for pokemon in self.pokemones:
            if pokemon.nombre == nombre:
                self.pokemones.remove(pokemon)
                return 1
        return -1

#permite eliminar un entrenador
    def eliminar_entrenador(self, nombre:str):
        for entrenador in self.entrenadores:
            if entrenador.nombre == nombre:
                self.entrenadores.remove(entrenador)
                return 1
        return -1
    

#imprime informacion de los pokemones
    def imprimir_informacion_pokemon(self):
        for pokemon in self.pokemones:
            print(f"Numero: {pokemon.numero}. \nNombre: {pokemon.nombre}.  \nTipo: {pokemon.tipo}. \nDescripcion: {pokemon.descripcion}. \nEvolucion: {pokemon.evolucion}.\n")
            
#imprime lo mas importante de los entrenadores nombre , medallas , region , pokemonUsado 
    def imprimir_nombre_medallas_pokemonUsado(self):
        for entrenador in self.entrenadores:
            print(f"Nombre: {entrenador.nombre}. \nRegion: {entrenador.region}. \nPokemon mas Usado: {entrenador.pokemonUsado}.\n")
            
#Guarda los datos guardados en el archivo
    def guardar_pokedex(self, archivo="pokedex.pickle"):
        archivo_pickle = open(archivo, 'wb')
        pickle.dump(self.pokemones, archivo_pickle)
        pickle.dump(self.entrenadores, archivo_pickle)
        archivo_pickle.close()
#Carga los datos guardados en el archivo
    def cargar_pokedex(self, archivo="pokedex.pickle"):
        archivo_pickle = open(archivo, 'rb')
        self.pokemones = pickle.load(archivo_pickle)
        self.entrenadores = pickle.load(archivo_pickle)
        archivo_pickle.close()