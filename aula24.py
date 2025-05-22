# Operadores in e not in (== in = está entre, not in = não está entre)
# Strings são iteráveis ( São "Navegaveis")
# 0 1 2 3 4 5 6
# E d u a r d o
# -7 -6 -5 -4 -3 -2 -1

# nome = "Eduardo"

# print(nome[2])  #Procura na string a locação correspondente ao número pedido de forma positiva ('u')
# print(nome[-5]) #Procura na string a locação correspondente ao número pedido de forma negativa ('u')

#-----------------------------------------------------------------------------

# print("Edu" in nome) #Procura o(s) digito(s) requerido(s) na variavel referencia, se encontralo retorna True
# print("zico" in nome) #Procura o(s) digito(s) requerido(s) na variavel referencia, se n encontralo retorna Falses
# print(10 * "-")
# print("Edu" not in nome) #Procura o contrário do requirimento acima, se encontrar dara "False"
# print("zico" not in nome) #Procura o contrário do requirimento acima, se n encontrar dara "True"

#------------------------------------------------------------------------------

nome = input("Digite o seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"`{encontrar}` está em {nome}")

else:
    print(f"`{encontrar}` não está em {nome}")