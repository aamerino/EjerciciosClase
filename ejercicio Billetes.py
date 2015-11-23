def calcularBilletes (importe, billete):
	numeroDeBilletes = importe//billete
	return numeroDeBilletes

def calcularResto (importe, billete):
	importeResto = importe % billete
	return importeResto



def contadorBilletes (importe, billetes):
    for billete in billetes:
        numBilletes = int(calcularBilletes(importe, billete))
        if numBilletes == 0:
        	pass
        elif billete >= 2:
            print("%s billetes %s" % (numBilletes, billete))
        else:
            print("%s monedas %s" % (numBilletes, billete))
        importe = calcularResto(importe , billete)

billetes=[500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.10, 0.05, 0.02, 0.01]
importe = float(input('Ingresar Capital: '))

contadorBilletes(importe,billetes)

# ####
# Caso test calcularBilletes
if calcularBilletes(5000, 500) == 10:
	print("Caso test calcularBilletes OK")
else:
	print("Caso test calcularBilletes FAIL")

	# Caso test calcularResto
if calcularResto(5000, 500) == 0:
	print("Caso test calcularResto OK")
else:
	print("Caso test calcularResto FAIL")