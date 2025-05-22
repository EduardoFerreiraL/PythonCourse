# if  / elif      / else
# se  / se não se / se não

condicao1 = False
conficao2 = False
conficao3 = True
conficao4 = True

if condicao1:
    print("Código para a condição1")
    #Dentro da hierarquia podem se ter mais linhas de código

elif conficao2:
    print("Código para a condição2")

elif conficao3:
    print("Código para a condição3")

elif conficao4:
    print("Código para a condição4")

else:
    print("Nenhuma confição foi satisfeita")

#Funcionamento com debuguer, funcionamento do "if" prático com o debuguer

if 10 == 10:
    print("Outro if")

print("Fora do if")