## EXERCÍCIOS:

# **Exercício 1:** Escreva um programa que use a função `range()` para gerar os números pares de 2 a 20 e, em seguida, imprima cada número. Utilize os métodos que vimos até então. 

list1= [1,2,33,44,55,77]
print(list(range(2,22,2)))

print('-----//-----')

# **Exercício 2:** Escreva um programa que use a função `range()` para gerar os múltiplos de 5 em 5 a 50 e, em seguida.

print(list(range(5,55,5)))
print('-----//-----')

# **Exercício 3:** Escreva um programa que use a função `type()` para verificar o tipo de uma variável.

n1= 'ola mundo'
print(type(n1))
print('-----//-----')

# **Exercício 4:** Escreva um programa que use a função `print()` para imprimir uma mensagem de saudação personalizada, incluindo o nome do usuário.

name= input('Digite seu nome :')
print ('Saudações',name,'!Tenha uma boa aula')
print('-----//-----')

# **Exercício 5:** Escreva um programa que use a função `range()` para gerar os números ímpares de 1 a 10 e, em seguida, calcule e imprima a média desses números.
 
list2=[1,3,5,7,9]                    #lista= list(range(1,11,2))
print(list(range(1, 10, 2)))         #comprimento= len(lista)
soma1=(sum(list2))                   #total= sum(lista) 
media= soma1/4                       #media= total/comprimento 
print(media)                         #print(media)
print('-----//-----')

# **Exercício 6:** Descubra o máximo e o mínimo da sequência criada no  exercício 5
list2=[1,3,5,7,9]
print(max(list2))
print(min(list2))
print('-----//-----')
# **Exercício 7:** Ordene a lista  -  [10,56,40,5,4,9,7,1,0,56]
num=[10,56,40,5,4,9,7,1,0,56]
print(sorted(num))
print('-----//-----')
# **Exercícios 8:**  some todos os valores da lista ordenada no exercício 7
num=[10,56,40,5,4,9,7,1,0,56]
print(sum(num))
