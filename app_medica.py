import os
import numpy as np
import funciones_medicas as fm
# -------------- variables ------------------
opcion = ""  # Selección del usuario
tamaño = 2  # cantidad máxima de registros
rut = ""    # rut del paciente
arr_ruts = np.empty(tamaño, dtype=object)
nombre = ""  # nombre del paciente
arr_nombres = np.empty(tamaño, dtype=object)
edad = 0    # edad del paciente
arr_edades = np.empty(tamaño, dtype=int)
# ----------- Código Principal --------------
while True:
    os.system("cls")
    opcion = str(input('''
    --------- MENÚ -------
    1.- Cargar datos
    2.- Buscar a un paciente por su rut
    3.- Imprimir ficha médica menores de edad
    4.- Salir
    \n Elija opcion: '''))

    if opcion == "1":
        os.system("cls")
        print("\n ------- Cargar datos ------")
        for k in range(tamaño):
            rut = str(input("Ingrese rut: ")).strip().upper()
            while not (fm.validar_rut(rut)):
                print("Error, no vacio!!")
                rut = str(input("Ingrese rut: ")).strip().upper()
            arr_ruts[k] = rut

            nombre = str(input("Ingrese nombre: ")).strip()
            while not (fm.validar_nombre(nombre)):
                print("Error, minimo 3 caracteres")
                nombre = str(input("Ingrese nombre: ")).strip()
            arr_nombres[k] = nombre

            edad = int(input("Ingrese edad:"))
            while not (fm.validar_edad(edad)):
                print("Error, debe ser postivo")
                edad = int(input("Ingrese edad:"))
            arr_edades[k] = edad
        
            fm.imprimir_ficha(rut,nombre,edad)
        os.system("pause")

    if opcion == "2":
        os.system("cls")
        rut = ("Ingrese rut: ")
        if rut not in arr_ruts:
            print("Error, rut no encontrado")
        else:
            print(arr_ruts)

        os.system("pause")
    if opcion == "3":
        os.system("cls")

        fm.imprimir_ficha()

        os.system("pause")
    if opcion == "4":
        break
