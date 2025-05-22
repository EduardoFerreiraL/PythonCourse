# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisar ser verdadeiras
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu) 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

"""entrada = input("[E] entrar [S] sair: \n")
senha_digitada = input("Senha: \n")

senha_permitida = "123456"
if entrada == "E" and senha_digitada == senha_permitida:
    print("Entrar")

else:
    print("Acesso Negado")"""

#Avaliação de curso circuito
print(True and False and True)
print(True and 0 and True)
print(bool("")) #Uma string vazia retorna false, mas com um espaço retorna true