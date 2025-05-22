# Conversão de tipos, coerção 
# type convertion, typecasting, coercion
# tipos imutáveis e primitivos:
# str, int, float, bool

# print(1 + 1) # Soma de int's
# print('1'+ 1) #Não permite por é uma str ('') com um int
# print('a' + 'b') # Concatenou as duas strings

print('1', type('1')) # Acusara de ser uma str
print(int('1'), type(int(1))) # Foi feita a conversão para int

print(int('1') + 1) #Soma de str com int
print(float('1') + 1) #Soma de str com int
print(bool(''))
print(str(11) + "b") #transforma um int em str