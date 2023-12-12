def TablaMultiplicar():
    """Esta función pide un número entre el 1 y el 10
    Parametros.
    -Recibe un número entero entre el 1 y el 10
    Salida:
    Guarda en un fichero con el nombre tabla-n.txt la tabla de multiplicar
      de ese número, donde n es el número introducido.
    """
Numero = int(input("Dime un número entero del 1 al 10"))
if  1 <= Numero <= 10:
    Osasuna = open("tabla-n.txt", "w")
    for i in range(1,11):
        Osasuna.write(str(Numero) + " * " + str(i) + "\n") 
    Osasuna.close
else:
    print("Anda no seas tonto y dime un número entero del 1 al 10")
                  
