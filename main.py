from Classes.Cliente import Cliente
from Classes.Cuenta import Cuenta

# Menú

# 1. Registrar Cliente Nuevo/ Crea una cuenta

opcion=1

print("Bancolombia")
print("1. Registrar cliente. ")
print("0. Salir.")
print("______________________")

while(opcion!=0):

    opcion=int(input("Digita una opción: "))

    if(opcion==1):
        name=input("Digite el nombre del usuario: ")
        lastName=input("Digite los apellidos del usuario: ")
        id=input("Digita la cedula del usuario: ")
        balance=0
        accountNumber=input("Digite el número de cuenta: ")

        cliente = Cliente(name,lastName,id,accountNumber)
        cuenta = Cuenta(accountNumber,balance)
