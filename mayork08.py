#coding: utf-8
y = input("Introduce un numero par:")
suma = 0
while y%2!=0 :
	y == input("No es par. Introduce un numero par:")
p = raw_input("¿Quiere escribir otro número par? (S/N)")
while (p=="S" or p=="s") :
	y = input("Introduce un numero par:")
	while y%2!=0 :
		y == input("No es par. Introduce un numero par:")
	suma += 1
	p = raw_input("¿Quiere escribir otro número par? (S/N)")
print "Programa terminado."
