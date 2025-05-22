"""
Introdução ao try/except
try -> tenta executar o código
except -> ocorreu algum erro ao executar o código
"""
#numero = float (input ('Vou dobrar o número que você digitar: ')) #Meu jeito já trasnfomando no input
numero_str = input ( #Usar o "F2" com a var selecionada, troca em TODOS os lugares q aquela var aparece
    'Vou dobrar o número que você digitar: ' 
)

try:
    numero_float = float(numero_str)
    print("FLOAT:", numero_float)
    print (f"O dobro de número {numero_str} é {numero_float * 2:.1f}")
except:
    print("Isso não é um número")
#Usado quando já se espera o erro no código, pulando imediatamente para o "except"

#if numero_str.isdigit(): #"".isdigit()" faz a verificação se o valor digitado é um n°
#    numero_float = float(numero_str)
#    print (f"O dobro de número {numero_str} é {numero_float * 2:.0f}")
#else: 
#    print("Isso não é um número")