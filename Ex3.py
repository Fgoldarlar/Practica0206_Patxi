def Linea_multiplicar ():
    """Esta función nos pide 2 números n y m entre 1 y 10, lea el fichero 
    tabla-n.txt con la tabla de multiplicar de ese número, y muestre por 
    pantalla la línea m del fichero.
    Parametros:
    - Dos números n y m entre 1 y 10
    Salida:
    muestra un mensaje por pantalla informando de ello.
    """
    n = int(input("Dime un número entre el 1 y el 10: "))
    m = int(input("Dime otro número del 1 al 10: "))
    fichero = "tabla-" + str(n) + ".txt"
    if 1<= n and m <=10:
            try:
                with open(fichero, "r") as osasuna:
                    Linea = osasuna.readlines
                print(Linea[m-1])
            except FileNotFoundError:
                print("No hay fichero con esta tabla")
    else:
        print("DEL 1 AL 10!!!")


Linea_multiplicar()

        
