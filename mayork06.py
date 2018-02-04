#coding: utf-8
x = input("Valor limite:")
cont = 0
if (x<=0) :
	x = input("Debe ser mayor que 0. Intentalo de nuevo:")
while(cont<x):
	aux = input("Otro numero:")
	cont = cont + aux
print "Ha superado el límite. La suma de los números es",cont
	
