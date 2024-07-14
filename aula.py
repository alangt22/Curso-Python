

# Funções 
'''
def boas_vindas(nome,quantidade=6):
    print(f'Ola {nome}.')
    print(f"temos {str(quantidade)} laptops em estoque")


boas_vindas('Marcos')
'''
'''
def boas_vidas_alan():
    print('Ola Alan')
    print("temos 5 laptops em estoque")


    
def boas_vidas_gael():
    print('Ola Gael')
    print("temos 4 laptops em estoque")


    
def boas_vidas_paula():
    print('Ola Paula')
    print("temos 2 laptops em estoque")


boas_vidas_alan()
boas_vidas_gael()
boas_vidas_paula()
'''





# Qual e o numero fatorial de 4
# 4*3*2*1 = 24



#cidades = ['Sao paulo', 'Rio de janeiro', 'Salvador', 'Goias']
#              0               1              2          3

#cidades.append('santa catarina')
#cidades.remove('Salvador')
#cidades.insert(1, 'santa catarina')
#cidades.pop(0)
#cidades.sort()

#cores = ['amarelo', 'vermelho', 'azul', 'laranja']
#valores = [10, 20, 30, 40]
#duas_listas = zip(cores, valores)
#print(list(duas_listas))


#frutas_usuario = input('Digite o nome das frutas separados por virgula: ')
#frutas_lista = frutas_usuario.split(', ')

#print(frutas_lista)


#tuples
#Array
'''
from array import array
coreslista = ['a', 'b']
corestuple = ('alan', 'allan')
coreslista = array("u",['a', 'b'] )
print(coreslista)
'''

# Set (Listas)
    # similar a lista
    # Evita duplicidade
    # Não usa index
'''
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]
num1 = set(list1)
num2 = set(list2)
print(num1 | num2)  # Unir as duas lista e tira os iguais
print(num1 - num2)  # diference
print(num1 ^ num2)  # tira os iguais da lista 
print(num1 & num2)  #and
print()
'''
'''
list1 = set([1, 2, 3, 4, 5, 6])
s1 = {1, 2, 3, 4, 5, 6, 2}

s1.update([7,8,9,10])
s1.remove(10) # gera erro
s1.discard(9) # nao gera erro
print(s1)
'''
'''
set1 ={'a', 'b', 'c'}
set2 ={'a', 'd', 'e'}
set3 ={'c', 'd', 'f'}
set4 = set1.symmetric_difference(set3)
print(set4)
'''
# Dicionarios

'''aluno = {'nome': 'Ana', 
         'idade': 16, 
         'nota final': 'A', 
         'aprovação': True, 
         'materias': ['fisica', 'matematica', 'ingles'] 
         }
#print(aluno['idade'])
# #del aluno['idade']
#for keys, values in aluno.items():
#   print(keys, values)
print(aluno.items())
print(aluno.keys())
print(aluno.values())'''

# Função Lambda
   # e uma funçao sem nome
   # pode usar em outra funçao
   # codigo mais limpo

'''def somar(x):
    return x + 10
print(somar(2))
   '''

#x = lambda x,y: x + y + 10

#print(x(2,4))

'''
def somar(x): 
    func2 = lambda x: x + 10
    return func2(x) * 4
print(somar(2))'''


# Função Map


#lista1 = [1, 2, 3, 4]

'''def multi(x):
    return x * 2'''

#lista2 = map(lambda x: x * 2, lista1)
#print(list(map(lambda x: x * 2, lista1)))

'''lista1 = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: x+1+2,lista1)))'''

'''
valores = [10,12,34,44,57]

def remover20(x):
    return  x > 20

print(list(filter(remover20, valores)))

print(list(filter(lambda x: x > 20, valores)))'''


# list comprehension

#frutas = ['abacate','banana','morango','kiwi','abacaxi']
#frutas2 = []


'''for itens in frutas:
    if 'n' in itens:
        frutas2.append(itens)'''
#frutas2 = [iten for iten in frutas if 'a' in iten]
#print(frutas2)        


#valores = []

'''for x in range(6):
    valores.append(x*10)

print(valores)
'''

'''valores = [x * 10 for x in range(20)]

print(valores)'''

# Generator Expressions
'''from sys import getsizeof
numeros = [x*10 for x in range(1000000)]
print(type(numeros))

print(getsizeof(numeros))

print('===========')

numeros = (x*10 for x in range(1000000))
print(type(numeros))

print(getsizeof(numeros))'''


# Erros
     # Try  Except
     # execelente para testes

'''try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index nao existe')'''


'''try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em numeros')    
finally:
    print('codigo ok')
'''
'''else:
    print('Usuario digitou valor correto')
    resultado = valor * 2
    print(resultado)
'''
#print('mais codigo')



# OPP
# Classes

'''from datetime import datetime

# criar a classe
class Funcionarios:
   

   def __init__(self, nome, sobrenome, ano_nascimento):
      self.nome = nome
      self.sobrenome = sobrenome
      self.ano_nascimento = ano_nascimento

   def nome_completo(self):
      return self.nome + ' ' + self.sobrenome

   def idade_funcionario(self):
      ano_atual = datetime.now().year
      self.ano_nascimento = int(ano_atual - self.ano_nascimento)
      return self.ano_nascimento'''
      
# criar objeto
'''usuario1 = Funcionarios('Alan', 'Silva', 1996)    
usuario2 = Funcionarios('Paula', 'Soares', 2000)'''


'''# criar parametros do usuario1
usuario1.nome = 'Alan'
usuario1.sobrenome = 'Nunes'
usuario1.data_nascimento = '22/08/1996'

# criar parametros do usuario2
usuario2.nome = 'Paula'
usuario2.sobrenome = 'Soares'
usuario2.data_nascimento = '13/04/2000'''

# print
'''print(usuario1.nome_completo())
print(Funcionarios.idade_funcionario(usuario1))'''



'''temp_cel = int(input('Qual e a temperatura da carne ? '))

if temp_cel < 48:
    print('Cozinhar por mais alguns minutos. ')
elif temp_cel in range(48, 53):
    print('Selada')    
elif temp_cel in range(54, 59):
    print('ao ponto para o mal')        
elif temp_cel in range(60, 64):
    print('ao ponto')    
elif temp_cel in range(65, 70):
    print('ao ponto para o bem')    
elif temp_cel in range(71, 72):
    print('Bem passada') 
elif temp_cel >= 73:
    print("Queimada")               '''


'''rendimento = int(input('Qual o rendimento da lata? '))
largura = int(input('Qual a largura da parede?  '))
altura = int(input('Qual a altura da parede? '))

def calculo_tinta():
    area = altura * largura
    total = area / rendimento
    print(f'Você precisa de {total} latas de tintas ')

calculo_tinta()    '''

'''funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']


#lista1
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)
#lista2
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)
#lista3
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)'''

'''altura = float(input('Qual e a sua altura ? '))
peso = float(input('Qual e seu peso ? '))
imc = peso / (altura/100)**2


if imc < 18.5:
    print('Magreza')    
elif imc >= 18.5 and imc < 24.9:
    print('normal')        
elif imc >= 25.0 and imc < 29.9:
    print('sobrepeso')    
elif imc >= 30.0 and imc < 39.9:
    print('obesidade')    
else:
    print('obesidade grave')
'''
'''Nome = 'Alan'
idade = 26

print(f'ola, sou {Nome}, tenho {idade} anos' )'''

#frutas = ['abacaxi' , 'maça', 'morango', 'uva',]
'''# substituir item
frutas[1] = 'morango'
# adicionar no fim 
frutas.append('abacaxi')'''
'''frutas.remove('manga')
del frutas[-1] '''
# for loop
'''for frutas in frutas:
    print('Eu gosto de ' + frutas)'''
# contador de numeros
'''for x in range(1,11):
    print(x)'''

# loop dentro de loop
'''vegetais = ['cenoura', 'alface', 'brocolis']


for fruta in frutas:
    for vegetal in vegetais:
        print(fruta, vegetal)
frutas = ['maça', 'banana', 'manga']'''

'''numero  = 1

while numero <= 10:
    
    print(numero)
    numero = numero + 1'''


'''print('loop com o break:')
for num in range(1,11):
    if num > 5:
        break
    print(num)


print('\nloop com continue:')
for num in range(1,11):
    if num == 5:
       continue
    print(num)'''

#contador de itens 
'''
list = ['maça', 'banana', 'maça', 'abacaxi', 'maça', 'morango']
contador = 0

for fruta in list:
    if fruta == 'maça':
        contador += 1

print('Numero de maça na lista: ',contador)'''

'''num = int(input('Digite um numero: '))

if num > 10:
    print('o numero e maior que 10')
else:
    print('o numero e menor que 10')    '''

'''idade = int(input('Digite sua idade: '))

if idade < 13:
    print('Você é uma criança')
elif idade >=13 and idade <20:
    print('Você é um adolescente')
else:
    print('Você é um adulto')    '''



'''cars = ['BMW X6', 'BMW i5', 'BMW i8']
car_client = input('Digite o nome do Carro: ')

if car_client in cars:
    print('Carro disponivel')
else:
    print('Carro nao esta disponivel')    
'''

'''
while True:
    fruta = input('Digite o nome de uma fruta: ')
    if fruta.lower() == 'abacate':
        break
print('parabens vc acertou')'''



# LISTA 
'''numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))
for i in numeros:
    if i % 2 == 0:
       print(f'O numero {i} é par!')
    else:
       print(f'O numero {i} é impar!')'''


# TUPLA 
'''cidades = ('Sao Paulo', 'Rio de Janeiro', 'Salvador')
cid_usuario = input('Digite o nome da cidade ')

if cid_usuario in cidades:
    print('A cidade esta na lista ')
else:
    print('A cidade nao esta na lista ')    
'''


# DICIONARIO
'''cidades = {
    'Brasil': 'Brasilia',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Australia': 'Canberra',
    'Canada': 'Ottawa'
}

usuario_pais = input('Digite o nome do país: ')

if usuario_pais in cidades:
    print(f'A capital de {usuario_pais} é {cidades[usuario_pais]}! ')
else:    
    print('Nao temos informações')'''


# SETS
'''friends = {'Marcos', 'Ana', 'Sophia', 'Arthur', 'Amanda'}
friends1 = {'Jose', 'Arthur', 'Ana', 'Carol', 'Paulo'}

result = friends1.intersection(friends)
print(result)
'''

'''
# Função 
def quadrado (numero):
    return numero ** 2
num = int(input('Digite um numero: '))
print(f'O quadrado de {num} é {quadrado(num)}')'''

'''def somar (numeros, numero):
    return numeros + numero
num = int(input('Digite um numero: '))
num1 = int(input('Digite um numero: '))
print(f'A soma de {num} + {num1} é {somar(num, num1)}')'''

'''def potencia ( base, expoente=2):
    return base ** expoente
num1 = int(input('Digite o numero base: '))
num2 = input('Digite um expoente (default 2): ')

if num2:
    print(f' O resultado e: {potencia(num1,int(num2))}')
else:
    print(f'O resultado e: {potencia(num1)}')    '''

'''def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
user_number = int(input('Digite um numero: '))
print(f'O fatorial de {user_number} é {fatorial(user_number)}')    '''
'''
def dobrar(num):
    return num * 2

def quadrado(num):
    return dobrar(num) ** 2

user_number = int(input('Digite um numero: '))
print(f'O quadrado do dobro do numero {user_number} é {quadrado(user_number)}')'''


# LAMBDA
'''def cubo (num):
    return num ** 3'''

'''cubo = lambda num: num** 3
user_number = int(input('Digite um numero: '))
print(f'O cubo de {user_number} é {cubo(user_number)}')'''


'''user_number1 = int(input('Digite o primeiro numero: '))
user_number2 = int(input('Digite o segundo numero: '))
multiplicar = lambda num1, num2: num1 * num2
print(f'A multiplicação de {user_number1} e {user_number2} é {multiplicar(user_number1, user_number2)}') '''

'''def par_ou_impar(num):
    if num % 2 == 0:
        return 'Par'
    else:
        return 'Impar'''

'''par_ou_impar = lambda num: 'Par' if num % 2 == 0 else 'Impar'
user_number = int(input('Digite um numero: '))
print(f' O numero {user_number} é {par_ou_impar(user_number)}')'''

'''numeros = [1,2,3,4,5,6]
quadrado = lambda num: num ** 2
resultado = []
for  i in numeros:
    resultado.append(quadrado(i))
print(f'Os quadrados dos numeros {numeros} sao {resultado}')    '''



# CRIANDO INSTACIAS EC2
# REDUZINDO IMAGENS
# BACKUP EC2
# EC2 ON E OFF 
# BACKUP DYNAMODB                                  


# Desenvolvimento Web
# Css
# Sql
# Html


'''from PySimpleGUI import PySimpleGUI as sg 
 

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Ler os eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Alan' and valores['senha'] == '220896':
         janela = sg.WIN_CLOSED("bem v")         '''