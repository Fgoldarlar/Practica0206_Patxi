def MostrarMultiplicar ():
    """Esta función nos pide un número entero entre 1 y 10, lea el fichero
    tabla-n.txt
    Parametros:
    - Numero: n es el número introducido
    salida:
    Debe mostrarlo por pantalla. Si el fichero no existe debe mostrar un 
    mensaje por pantalla informando de ello.
    """
n = int(input("Dime un numero entero del 1 al 10"))
if 1 <= n <= 10:
    try:
        fichero = "Tabla-" + str(n) + ".txt"
        with open(fichero, "r") as archivo: 
            print("El archivo se ha leido!")
    except FileNotFoundError:
        print("No está el fichero")
else:
    print("Venga gracioso, que te he dicho del 1 al 10")