from pokedex import Pokemon , Entrenador , Pokedex

def menu():
    opcion = 0
    while opcion < 1 or opcion > 13:
        print("--")
        print ("BIENVENIDO A SU POKEDEX! ")
        print("--")
        print("(1) Agregar pokemon")
        print("(2) Buscar pokemon")
        print("(3) Editar pokemon")
        print("(4) Eliminar pokemon")
        print("(5) Agregar entrenador")
        print("(6) Buscar entrenador")
        print("(7) Editar entrenador")
        print("(8) Eliminar entrenador")
        print("(9) Imprimir informacion de los pokemon")
        print("(10) Imprimir informacion basica de los entrenadores")
        print("(11) Guardar en archivo")
        print("(12) Cargar desde archivo")
        print("(13) Salir")
        print("--")
        opcion = int(input("Elija una opcion: "))
        print("--")
    return opcion

def ejecutar(pokedex): # controlador
    opcion = 0
    while opcion != 13:
        opcion = menu()
        if opcion == 1:
            numero = input("Numero: ")
            nombre = input("Nombre: ")
            tipo = input("Tipo: ")
            debilidad = input("Debilidad: ")
            descripcion = input("Descripcion: ")
            evolucion = input("Evolucion: ")
            pokedex.agregar_pokemon(numero,nombre,tipo,debilidad,descripcion,evolucion)
            print("--")
            print("Pokemon agregado")
        if opcion == 2:
            nombre = input("Nombre: ")
            respuesta = pokedex.buscar_pokemon(nombre)
            if respuesta != -1:
                print("--")
                print(f"El pokemon {nombre} tiene: \nNumero :", numero ,"\nTipo :", tipo,"\nDebilidad :" , debilidad ,"\nDescripcion :" , descripcion, "\nEvolucion :", evolucion)
            else:
                print("--")
                print(f"{nombre} no se encuentra en la pokedex.")
        if opcion == 3:
            nombre= input("Ingrese el nombre del pokemon que desea editar: ")
            respuesta = pokedex.buscar_pokemon(nombre)
            if respuesta != -1:
                nuevo_nombre = input("Ingrese los nuevos datos del pokemon \n Nombre: ")
                nuevo_numero=input ("Numero: ")
                nuevo_tipo= input("Tipo: ")
                nuevo_debilidad= input("Debilidad: ")
                nuevo_descripcion= input("Descripcion: ")
                nuevo_evolucion= input("Evolucion: ")
                pokedex.modificar_pokemon(nombre,nuevo_nombre, nuevo_numero,nuevo_tipo,nuevo_debilidad,nuevo_descripcion,nuevo_evolucion)
                print("--")
                print("Se modifico correctamente")
            else:
                print("--")
                print(f"{nombre} no se encuentra en la pokedex.")
        if opcion == 4:
            nombre = input("Nombre: ")
            respuesta = pokedex.eliminar_pokemon(nombre)
            if respuesta != -1:
                print("--")
                print(f"{nombre} ha sido eliminado de la pokedex.")
            else:
                print("--")
                print(f"{nombre} no se encuentra en la pokedex.")
        if opcion == 5:
            nombre = input("Nombre: ")
            medallas = input("Medallas: ")
            region = input("Region: ")
            pokemonUsado = input("Pokemon mas Usado: ")
            pokedex.agregar_entrenador(nombre , medallas , region , pokemonUsado)
            print("--")
            print("Entrenador agregado")
        if opcion == 6:
            nombre = input("Nombre: ")
            respuesta = pokedex.buscar_entrenador(nombre)
            if respuesta != -1:
                print("--")
                print(f"El Entrenador {nombre} tiene: \nMedallas",medallas ,"\nRegion :", region,"\nPokemon mas usado :" , pokemonUsado,)
            else:
                print("--")
                print(f"{nombre} no se encuentra en la pokedex.")
        
        if opcion == 7:
            nombre = input("Ingrese el nombre del entrenador que desea editar: ")
            respuesta = pokedex.buscar_entrenador(nombre)
            if respuesta != -1:
                nuevo_nombre= input("Ingrese los nuevos datos del entrenador \n Nombre: ")
                nuevo_medalla= input("Medalla: ")
                nuevo_region= input("Region: ")
                nuevo_pokemonUsado= input("Pokemon mas usado: ")
                pokedex.modificar_entrenador(nombre,nuevo_nombre ,nuevo_medalla ,nuevo_region,nuevo_pokemonUsado)
                print("--")
                print("Se modifico {nombre} con exito")
            else:
                print("--")
                print(f"{nombre} no se encuentra en la pokedex.")
        if opcion == 8:
            nombre = input("Nombre: ")
            respuesta = pokedex.eliminar_entrenador(nombre)
            if respuesta != -1:
                print("--")
                print(f"{nombre} ha sido eliminado de la pokedex.")
            else:
                print("--")
                print(f"{nombre} no se encuentra en la pokedex.")        
        if opcion == 9:
            print("INFORMACION DE LOS POKEMONES \n ")
            pokedex.imprimir_informacion_pokemon()    
        if opcion == 10:
            print("INFORMACION BASICA DE LOS ENTRENADORES\n")
            pokedex.imprimir_nombre_medallas_pokemonUsado()
        if opcion == 11:
            pokedex.guardar_pokedex()
            print("--")
            print("Se guardo Correctamente")
        if opcion == 12:
            pokedex.cargar_pokedex()
            print("--")
            print("Se cargo Correctamente")

if __name__ == "__main__":
    pokedex = Pokedex()
    ejecutar(pokedex)