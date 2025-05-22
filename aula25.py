"""

Interpolação básica de strings
s - string
dei - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = "Edaurdo"
preco = 1000.95897643
#variavel = 'Eduardo, o preço é R$1000.95' representação da forma "comum" de se escrever
variavel = '%s, o preço é R$%.2f' % (nome, preco) #Dessa forma o %s puxa a string da var "nome" e o %f o float da var "preco"
#Possivel arredondar as casas dps da virgula colocando o ".(n° de casas)" exemplo: "%.2f" puxara 2 casas dps da virgula
print(variavel)
# "%d" puxa o número inteiro do vetor
# "%x" converte o número q puxar para hexadecimal
# é possivel completar numeros colocando com zero colocando "0(n° de casas)" exemplo: "%04x"
print("O hexadecimal de %d é %04x" %(1500, 1500))
print("O hexadecimal de %d é %04x" %(1500, 1500))

#Tentar se padronizar com as "%", exemplo: usar o "%f" para puxar números (quando a função n exigir diferenciação de float e int)