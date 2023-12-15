def TablaMultiplicar():
    """Esta función pide un número entre el 1 y el 10
    Parametros.
    Entrada:
    -Recibe un número entero entre el 1 y el 10
    Salida:
    Guarda en un fichero con el nombre tabla-n.txt la tabla de multiplicar
      de ese número, donde n es el número introducido.
    """

Numero = int(input("Dime un número entero del 1 al 10"))

chimy = "Tabla-" + str(Numero) + ".txt"
if  1 <= Numero <= 10:
    with open(chimy, "w") as Osasuna: 
        for i in range(1,11):
            Osasuna.write(str(Numero) + " * " + str(i) + "\n") 
else:
    print("Anda no seas tonto y dime un número entero del 1 al 10")

