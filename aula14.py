a = 'A'
b = 'B'
c = 1.1
string = 'a={nome0} b={nome1} c={nome2:.2f} ' #Usar os indices, (0,1,2) ao inves de deixar ele procurar por sequencia
formato = string.format(nome0=a, 
                        nome1=b,#Um jeito de nomear as Var sem precisar mudar o nome delas em si, dando um rotulo
                        nome2=c) #Referencia a ordem q sera pego os valores com relação a VAR

print(formato)