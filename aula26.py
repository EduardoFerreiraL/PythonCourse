"""

Formatação básica de strings
s - string
d - int
f - float 
.<núpumeor de digitos> f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esqueda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos 0
Sinal -+ ou -
Ex.: 0>-100,.1f
Conversion flags- !r !s !a (__repr__ __str?__ __asc__)
"""

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <10}.")
print(f"{variavel:^10}.")
#É possível colocar digitos ao invés de espaços add o digito após o ":", Ex: print(f"{variavel:H^10}.")

print (f'{-1000.354336347373:.2f}') #Colocando n° negativo
print (f'{1000.354336347373:+,.2f}') #Colocando o "+" para aparecer com o sinal de positivo 
print (f'{1000.354336347373:0=+10,.2f}') #Uso do "=" para o "+" apareder antes dos zeros e continuar tento o sianl de positivo e os zeros
print (f'{1000.354336347373:.2f}') 
#É possível separar o milhar por "," colocando-a após os ":" (Existem bibliotecas expecificas para formatação)
print (f'O hexadecimal de 1500 é {1500:08X}') #Outra manneira de se obter o hexadecimal formatando na própria especificação do n°

print(f"{variavel!r}")