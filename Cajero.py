saldo = 1000
print ("1. Consultar saldo")
print ("2. Retirar Dinero")
print ("3. Depositar dinero")
opcion = input("Escoge una opcion: ")
if opcion == "1":
    print (saldo)
    print("Gracias Por Usar el cajero") 
elif opcion == "2":
    while True:
        retirar = int(input("Cuanto dinero deseas retirar?: "))
        if retirar <= 0:
            print("El monto debe ser positivo.")

        elif retirar > saldo:
            print("saldo insuficiente")
        else:
            saldo-= retirar
            print("Retiro exitoso este es tu nuevo saldo:", saldo)
            print("Gracias Por Usar el cajero") 
elif opcion == "3":
    while True:
        Depositar= int(input("CUento dinero te gustaria depositar?: "))
        if Depositar > 0:
            saldo+= Depositar
            print ("Nuevo saldo es:", saldo) 
            print("Gracias Por Usar el cajero")
            break
        else:
            print("el fondo debe ser en positivo, porfa ingrese de nuevo.")
else: 
    print ("opcion invalida")


