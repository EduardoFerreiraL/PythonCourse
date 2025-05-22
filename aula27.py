"""
Fatiamento de strings

012345678
Olá mundo
-987654321

Fatiamento [i:f:p] [::]
Obs: a função len retorna a qtd de caracteres da str
"""

variavel = "Olá mundo"
print(variavel[4:7]) #Escreveu o intervalo da str requisitada #S
print(variavel[4:]) #Se o intervalo n referir um final, o vetor irá até o final da string, apenas usando o 1° valor como inicio
print(variavel[:5]) #Se o intervalo n referir um incio, o vetor irá até a refencia da string, apenas usando o valor final como fim
#Os ":" que indica para o python que para fazer o fatiamento

print(len(variavel)) #Usado para contar as string da refencia
print(len(variavel[4:7])) #com [] é usado para contar o intervalo dentre as strings no vetor ou somente o n° do vetor referenciado

print(variavel[0:9:2]) #Usa do 3° valor como intervalo para pular, no Ex dessa linha ele pulou 1 str e foi pra a outra Ex: Olá = Oá
print(variavel[::-1]) #Se for o usando com ne negativo ele interte a String, dimindo mais o número ele faz o msm do de cima mas ao contrário
