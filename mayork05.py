#coding: utf-8
x = input("Introduce un numero:")
suma = 0
cont = 0
while(cont<x) :
	aux = input("Introduce un numero:")
	if (aux>0) :
		cont += 1
		suma = suma + aux
print suma
