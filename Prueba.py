import os


os.system("cls")

print("Hola mundo!"); 
#print("Hola")
Mi_nombre="Mi nombre es\
    Gaby"
print(Mi_nombre)
a=0
for i in range (5):
    a+=1
    print(a)

##Video 4
#Operadores
#print(5+6)
#print(10%3)
#print(5**3)
#print(9//2)
#Introduciendo a variable type
nombre=5
type(nombre)
print(type(nombre))
nombre="Juan"
print(type(nombre))
nombre=5.2
print(type(nombre))
#Introducción a las 3 comillas
mensaje="""Esto es un mensaje
con tres saltos
de línea"""
print(mensaje)
#Introducción comando "If"
numero1=5
numero2=7
if numero1>numero2:
    print("El número 1 es mayor")
else:
    print ("El número 2 es mayor")

#Video 5 
#Introducción a las funciones
def mensaje ():
    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo isntrucciones básicas")
    print("Poco a poco iremos avanzando")
mensaje() 

print("Ejecutando código fuera de función")
mensaje()
#print(mensaje())    Asigna un none por el print
#x = mensaje()
#print(x)   La misma wea por defecto


 