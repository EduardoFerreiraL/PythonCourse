# if  / elif      / else
# se  / se não se / se não
entrada  = input("Você quer entrar ou sair? ")

if entrada == "entrar":
    print(f"Você entrou no sistema")

elif entrada == "sair":
    print(f"Você saiu do sistema")

else:
    print(f"Você não digitou nem 'entrar' nem 'sair'")