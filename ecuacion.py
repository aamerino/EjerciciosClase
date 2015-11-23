# Resolver ecuacion 2ndo grado


def ecuacionSegGrado(a, b, c):
	import math

	if a == 0:

		return None

	discriminante = b**2 - 4*a*c
    if b == 0  and -c/a < 0:
		return None

	if discriminante < 0:

		return None

	discriminante = math.sqrt(discriminante)

	discriminantePos = (-b + discriminante)/ (2 * a)

	discriminanteNeg = (-b - discriminante)/ (2 * a)

	return discriminantePos , discriminanteNeg



####################CASOS TEST#########################
a = 1
b = 2
c = 3

#########SIN SOLUCION  a = 0###########

a = 0

if None == ecuacionSegGrado( a , b , c):

	print ("Pass a=0")

else:

	print ("Fail a=0")

###########CASO GENERAL#########

a = 1
b = -5
c = 6
resultado1 , resultado2 = ecuacionSegGrado (a , b, c)
if resultado1 == 3 and resultado2 == 2:
	print ("Pass caso general")


###########B = 0 y C = 0############
b = 0
c = 0

resultado1 , resultado2 = ecuacionSegGrado (a , b , c)
if resultado1 == 0 and resultado2 == 0:
	print ("Pass b=0 y c=0")

##########B = 0 y -c/a < 0############

b= 0
c = 6

if None == ecuacionSegGrado (a, b , c):
    print ("Pass no solucion real")


############ C =0 ######################
a = 3
b = 7
c = 0

resultado1 , resultado2 = ecuacionSegGrado(a , b, c)

if resultado1==0 and resultado2 == -b/a:
		print ("Pass c=0")
else:
		print ("Fail c=0")
