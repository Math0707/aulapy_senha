#SISTEMA DE SENHAS 
# 1- CRIE UM SISTEMA DE SENHAS, O COMPUTADPR CRIA UMA SENHA ALEATORIA
# 2- cAMPO PARA DIGITAR A SENHA 
# 3- VERIFICAR SE O USUARIO PODE ACESSAR 
import random

cadeado= random.randint(10,20)
senha= input('|Digite a senha ')

if senha == cadeado:
    print(cadeado, senha )
    print ('Acesso liberado!')
else :
    print('Senha incorreta tente novamente!')

# cadeado= ('784')
# senha= input('|Digite a senha ')

# if senha == cadeado:
#     print(cadeado,)
#     print ('Meus parabens!!')
# else :
#     print('Senha incorreta tente novamente!')

#     print('----//----')
#     print ('835: um número esta certo mas no lugar errado')
#     print ('----//----')
#     print ('584: dois numeros estão certos e no lugar certo') 
#     print ('----//----')
#     print ('623: nada esta correto aqui')
#     print ('----//----')
#     print ('795: um numero certo e no lugar certo') 
#     print('----//----')       