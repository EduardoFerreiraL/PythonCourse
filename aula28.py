"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem (n) letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vázios."
"""

nome = input ("Digite seu nome: ")
idade = (input("Digite sua idade: "))

if nome and idade: #Usou apenas o "and" para unir e testar se as str estão vázias ou não
    print(f"\nSeu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")

    if ' ' in nome:
        print(f"Seu nome contem espaços")
    
    else:
        print(f"Seu nome não contem espaços")
    
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A primeira letra do seu nome é {nome[-1]}") #Usou o 1° para pegar a primeira letra, vindo de trás para frente

else:
    print(f"Desculpe, você deixou campos vázios")