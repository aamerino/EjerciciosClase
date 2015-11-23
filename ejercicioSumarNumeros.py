def calcularMayor(numero, numeroMayor):
	if int(numero) > int(numeroMayor):
		return numero
	else:
		return numeroMayor

def calcularMenor(numero, numeroMenor):
	if int(numero) < int(numeroMenor):
		return numero
	else:
		return numeroMenor

def calcularMedia(sumaNumerosMedia, divisorMedia):
	return sumaNumerosMedia/divisorMedia


sumaNumerosMedia = 0
divisorMedia = 0
numero = input("Introduce Numero: ")
numeroMayor = numero
numeroMenor = numero
while numero != '.':
	numeroMayor = calcularMayor(numero, numeroMayor)
	numeroMenor = calcularMenor(numero, numeroMenor)
	sumaNumerosMedia += int(numero)
	divisorMedia += 1
	numero = input("Introduce Numero: ")
media = calcularMedia(sumaNumerosMedia, divisorMedia)

print("Número mayor: %s" % numeroMayor)
print("Número menor: %s" % numeroMenor)
print("Media de todos los números: %s" % media)
print("----------------------------------------------")


##########CASOS TEST###############

##########Caso test para calcularMayor#########
print("Casos test para calcularMayor")
casosTest = [((5, 6), 6),
             ((-4, 7), 7)]

for casoTest in casosTest:
	valores = casoTest[0]
	resultado = calcularMayor(valores[0], valores[1])
	if casoTest[1] == resultado:
		print ("En el caso test %s el mayor es %d OK" % (casoTest[0], resultado))
	else:
		print ("En el caso test %s el mayor es %d FAIL" % (casoTest[0], resultado))
print("----------------------------------------------")
##########Caso test para calcularMenor#########
print("Casos test para calcularMenor")
casosTest = [((5, 6), 5),
             ((-4, 7), -4)]

for casoTest in casosTest:
	valores = casoTest[0]
	resultado = calcularMenor(valores[0], valores[1])
	if casoTest[1] == resultado:
		print ("En el caso test %s el menor es %d OK" % (casoTest[0], resultado))
	else:
		print ("En el caso test %s el menor es %d FAIL" % (casoTest[0], resultado))

print("----------------------------------------------")
##########Caso test para calcularMedia#########
print("Casos test para calcularMedia")
casosTest = [((14 , 2), 2, 8),
             ((-4, 7), 2, 1.5)]

for casoTest in casosTest:
	for i in casoTest[0]:
                sumaNumerosMedia += i
        media = calcularMedia(sumaNumerosMedia, casoTest[1])
        if casoTest[2] == resultado:
		print ("En el caso test %s el menor es %d OK" % (casoTest[0], resultado))
	else:
		print ("En el caso test %s el menor es %d FAIL" % (casoTest[0], resultado))



















