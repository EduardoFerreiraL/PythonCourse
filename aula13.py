nome = 'Eduardo Ferreira'
altura = 1.80
peso = 78
imc = peso / (altura * altura)

"f-strings"
print (nome, "tem", altura, "de altura,\npesa", peso, "Kg e seu IMC é\n", imc)
print (f"{nome} tem {altura:.2f} de altura,\n pesa {peso:.2f} Kg e seu IMC é\n {imc:.2f}")