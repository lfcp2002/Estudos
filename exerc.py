"""
# ============================================================
# LISTA DE EXERCÍCIOS PYTHON – DETALHADA
# ============================================================

# -------------------------
# NÍVEL 1 — FUNDAMENTOS
# -------------------------

# 1. Mostrar "Olá Mundo" na tela
# Descrição: Exibir a mensagem "Olá Mundo" no console.

# 2. Solicitar um número ao usuário e mostrar: "O número informado foi X"
# Descrição: Receber um número do usuário e exibir uma mensagem informando o valor digitado.

# 3. Solicitar dois números e mostrar a soma
# Descrição: Receber dois números e exibir a soma entre eles.

# 4. Solicitar quatro notas e calcular a média
# Descrição: Receber quatro valores numéricos correspondentes às notas de um aluno e calcular a média aritmética.

# 5. Converter metros para centímetros
# Descrição: Receber um valor em metros e exibir o equivalente em centímetros.

# 6. Calcular a área de um círculo
# Descrição: Receber o raio do círculo e calcular a área usando a fórmula área = π * raio².

# 7. Calcular a área de um quadrado e mostrar o dobro
# Descrição: Receber o tamanho do lado de um quadrado, calcular a área e exibir também o dobro da área.

# 8. Calcular o salário mensal a partir de horas trabalhadas
# Descrição: Receber a quantidade de horas trabalhadas e o valor da hora, calcular e exibir o salário mensal.

# 9. Converter Fahrenheit para Celsius
# Descrição: Receber a temperatura em Fahrenheit e exibir o valor correspondente em Celsius.

# 10. Converter Celsius para Fahrenheit
# Descrição: Receber a temperatura em Celsius e exibir o valor correspondente em Fahrenheit.


# print("Hello World")


# numero = input("Numero?")
# print(numero)


# numero1 = input("Numero1?")
# numero2 = input("Numero2?")
# soma = numero1 + numero2
# print(soma)


# nota1 = input("nota1?")
# nota2 = input("nota2?")
# nota3 = input("nota3?")
# nota4 = input("nota4?")
# soma = float(nota1) + float(nota2) + float(nota3) + float(nota4)
# media = float(soma) / 4
# print(media)


# def conversao (met):
#    if not isinstance(met, (int,float)):
#        return "insira um numero como parametro!"
#    elif met <= 0:
#        return "insira um numero maior que 0!"
#    else: return 100 * met
# conversao(20)


# import math
# ra = float(input("raio?"))
# ar = math.pi * ra ** 2
# print(ar)


# la = float(input("lado?"))
# ar = float(la * la)
# dobro = ar + ar
# print(ar, dobro)


# horas = float(input("horas trabalhadas por dia?"))
# valor_h = float(input("qual o valor da sua hr?"))
# salario_dia = horas * valor_h
# salario_mes = salario_dia * 30
# print("salario dia: " + str(salario_dia) + "salario mes: " + str(salario_mes))


# Fa = float(input("temp?"))
# Ce = (Fa - 32) * 5 / 9
# print(Ce)


# Ce = float(input("temp?"))
# Fa = Ce * 1.8 + 32
# print(Fa)


# -------------------------
# NÍVEL 2 — CONDIÇÕES
# -------------------------

# 11. Solicitar dois números e mostrar o maior
# Descrição: Receber dois números e exibir qual é o maior.

# 12. Informar se um número é positivo ou negativo
# Descrição: Receber um número e indicar se ele é positivo, negativo ou zero.

# 13. Verificar se um número é par ou ímpar
# Descrição: Receber um número inteiro e informar se ele é par ou ímpar.

# 14. Verificar se uma letra é vogal ou consoante
# Descrição: Receber uma letra e informar se é vogal ou consoante.

# 15. Ler três números e mostrar o maior
# Descrição: Receber três números e identificar qual é o maior valor.


numero_1 = int(input("1 Numero?"))
numero_2 = int(input("2 Numero?"))

if numero_1 > numero_2:
    print("Numero 1 maior")
else:
    print("Numero 2 maior")


numero = float(input("numero?"))
if numero >= 0: print("Numero Positivo")
else: print("Numero Negativo")


numero = float(input("numero?"))
if numero % 2 == 0: print("Numero Par")
else: print("Numero impar")


letra = str(input("qual a letra?")).lower()
vogal = ('a','e','i','o','u')
if letra in vogal:
    print("Vogal")
else: print("Consoante")


n1 = float(input("primeiro número: "))
n2 = float(input("segundo número: "))
n3 = float(input("terceiro número: "))
if n1 >= n2 and n1 >= n3:
    print("Maior", n1)
elif n2 >= n1 and n2 >= n3:
    print("Maior", n2)
else:
    print("Maior", n3)


# 16. Ler três números e mostrar em ordem crescente
# Descrição: Receber três números e exibir todos em ordem crescente.

# 17. Verificar se um ano é bissexto
# Descrição: Receber um ano e informar se ele é bissexto ou não.

# 18. Verificar se três lados formam um triângulo
# Descrição: Receber três valores correspondentes aos lados de um triângulo e verificar se eles podem formar um triângulo válido.

# ============================================================
# LISTA DE EXERCÍCIOS PYTHON – DETALHADA COMPLETA
# ============================================================

# -------------------------
# NÍVEL 3 — LOOPS
# -------------------------

# 19. Mostrar números de 1 até 20
# Descrição: Exibir todos os números inteiros de 1 até 20.

# 20. Mostrar números ímpares de 1 até 50
# Descrição: Exibir todos os números ímpares entre 1 e 50.


n1 = int(input("n1?"))
n2 = int(input("n2?"))
n3 = int(input("n3?"))

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print(n1 , n2 , n3)
    else: print(n1 , n3 , n2)
elif n2 >= n1 and n2 >= n3:
    if n3 >= n1:
        print(n2 , n3 , n1)
    else: print(n2, n1 , n3)
elif n3 >= n1 and n3 >= n2:
    if n1 >= n2:
        print(n3,n1,n2)
    else: print(n3,n2,n1)


def bix(n):
    if n % 4 == 0 and not n % 100 == 0 or n % 400 == 0:
        print('e b')
    else: print('n e')
bix(2020)


l1 = int(input("l1?"))
l2 = int(input("l2?"))
l3 = int(input("l3?"))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l1 == l3: print("equilatero")
    elif l1 == l2 or l1 == l3 or l2 == l3: print("isosceles")
    elif l1 != l2 and l1 != l3 and l2 != l3: print("escaleno")
    else: print("n e")
else: print("n e")


for n in range(1, 21):
    print(n)


for n in range (1 ,51 ,2):
    print(n)


# 21. Gerar tabuada de um número
# Descrição: Receber um número e exibir sua tabuada de multiplicação do 1 ao 10.

# 22. Calcular o fatorial de um número
# Descrição: Receber um número inteiro e calcular seu fatorial.

# 23. Gerar sequência de Fibonacci
# Descrição: Exibir os primeiros números da sequência de Fibonacci até um determinado valor.

# 24. Ler números até o usuário digitar 0
# Descrição: Receber números continuamente do usuário até que ele digite zero.

# 25. Contar quantos números pares foram digitados
# Descrição: Receber vários números e informar quantos deles são pares.


num = int(input("Numero?"))
cont = 1

while cont <= 10:
    print(num * cont)
    cont += 1


import math
n = int(input("Numero?"))
resultado = math.factorial(n)
print(resultado)


a = 1
b = 1

for n in range(1, 10):
    c = a + b  # 1 + 1 = 2
    a = b  #  a = 1
    b = c   # b = 2
    print(c)


n = 1
while n != 0:
    n = int(input("n?"))
    print("Digite 0 para parar!")


n = 1
a = 0
while n != 0:
    n = int(input("n?"))
    print("Digite 0 para parar!")
    if n % 2 == 0:
        a += 1
print("a quantidade de pares foi: " ,  a)


# -------------------------
# NÍVEL 4 — LISTAS
# -------------------------

# 26. Ler 5 números e armazenar em lista
# Descrição: Receber cinco números do usuário e guardar todos em uma lista.

# 27. Mostrar a lista em ordem inversa
# Descrição: Exibir os elementos da lista do último para o primeiro.

# 28. Calcular a média de uma lista de notas
# Descrição: Receber uma lista de notas e calcular a média aritmética.

# 29. Separar números pares e ímpares
# Descrição: Receber uma lista de números e criar duas listas separadas: uma de pares e outra de ímpares.

# 30. Intercalar duas listas
# Descrição: Receber duas listas e criar uma terceira lista intercalando os elementos das duas.


lista = []
t = 0
while t != 5:
    lista.append(int(input("Numero? ")))
    t += 1
    if t == 5:
        print(lista)


l = [1,2,3,4,5]
print(l)
l.reverse()
print(l)


no = [2,4,6,8,10]
a = 0
b = 0
tn = len(no)
count = 0
for n in no:
    a += n
    count += 1
    if count == tn:
        b = a / count
        print('media e: ', b)


li = [1,2,3,4,5,6,7,8,9,10]
p = []
i = []
for l in li:
    if l % 2 == 0:
        p.append(l)
    else:
        i.append(l)
print(p)
print(i)


li1 = [0,2,4,6,8]
li2 = [1,3,5,7,9]
li3 = []
for i in range(len(li1)):
    li3.append(li1[i])
    li3.append(li2[i])
print(li3)


# -------------------------
# NÍVEL 5 — FUNÇÕES
# -------------------------

# 31. Criar função que soma dois números
# Descrição: Criar uma função que recebe dois números como parâmetro e retorna a soma.

# 32. Criar função que retorna o maior número
# Descrição: Criar uma função que recebe dois ou mais números e retorna o maior valor.

# 33. Criar função que calcula fatorial
# Descrição: Criar uma função que recebe um número e retorna seu fatorial.

# 34. Criar função que calcula média
# Descrição: Criar uma função que recebe uma lista de números e retorna a média.

# 35. Criar função que verifica se um número é primo
# Descrição: Criar uma função que recebe um número e retorna True se ele for primo ou False caso contrário.


def soma(s1,s2):
    s3 = s1 + s2
    return s3
soma(2,4)


def maio():
    ma = []
    cont = 0
    while len(ma) != 5:
        ma.append(int(input('5 numeros?')))
    ma.sort()
    print(ma[-1])
maio()


import math
def fat(o):
    r = math.factorial(o)
    return r


def media():
    me = []
    a = 0
    ml = 0
    while len(me) != 5:
        me.append(int(input('5 numeros para media?')))
        ml += 1
    for m in me:
        a += m
    b = (a / ml)
    print(b)
media()


def primo(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
print(primo(12))


# -------------------------
# NÍVEL 6 — STRINGS
# -------------------------

# 36. Contar caracteres em uma frase
# Descrição: Receber uma frase do usuário e informar a quantidade de caracteres.

# 37. Contar vogais em uma frase
# Descrição: Receber uma frase e contar quantas vogais ela possui.

# 38. Verificar se uma palavra é palíndromo
# Descrição: Receber uma palavra e verificar se ela é igual quando lida de trás para frente.

# 39. Inverter uma string
# Descrição: Receber uma string e exibir sua versão invertida.

# 40. Converter texto para maiúsculo
# Descrição: Receber uma frase e exibir toda em letras maiúsculas.


frase = "Ola Mundo"
print(len(frase))


frase = "Ola Mundo"
vog = ("a","e","i","o","u")
v = 0
for l in frase:
    for g in vog:
        if l == g:
            v += 1
print(v)


pala = input("Digite uma palavra")
mini = pala.lower()
sepa = []
for m in mini:
    sepa += m
sepa.reverse()
j = "".join(sepa)
if j == mini:
    print("e p")
else: print('n e')


st = input("palavra? ")
sep = []
for s in st:
    sep += s
sep.reverse()
j = ''.join(sep)
print(j)


tex = 'ola mundo'
m = tex.upper()
print(m)


# -------------------------
# NÍVEL 7 — ARQUIVOS
# -------------------------

# 41. Ler arquivo e contar linhas
# Descrição: Abrir um arquivo de texto e informar quantas linhas ele possui.

# 42. Contar palavras em arquivo
# Descrição: Abrir um arquivo e contar o número total de palavras.

# 43. Contar caracteres em arquivo
# Descrição: Abrir um arquivo e contar o número total de caracteres.

# 44. Ler números de arquivo e calcular média
# Descrição: Ler números de um arquivo e calcular a média aritmética.

# 45. Salvar dados digitados em arquivo
# Descrição: Receber informações do usuário e armazená-las em um arquivo de texto.


with open("arquivo.txt", "r") as f:
    t = 0
    for l in f:
        t += 1
print(t)


with open("arquivo.txt", "r") as f:
    t = 0
    for l in f:
        t += len(l.split())
print(t)


with open("arquivo.txt", "r") as f:
    t = 0
    for l in f:
        for p in l:
            t += 1
print(t)


with open("arquivo.txt", "r") as f:
    n = 0
    c = 0
    for l in f:
        for v in l.split():
                n += float(v)
                c += 1
m = n / c
print(m)


with open("arquivo.txt", "a") as v:
    f = input("Digite algo: ")
    v.write(f + "\n")


# -------------------------
# NÍVEL 8 — CLASSES
# -------------------------

# 46. Criar classe Bola
# Descrição: Criar uma classe Bola com atributos de cor, circunferência e material.

# 47. Criar classe Quadrado
# Descrição: Criar uma classe Quadrado com atributo lado e métodos para calcular área e perímetro.

# 48. Criar classe Pessoa
# Descrição: Criar uma classe Pessoa com atributos nome, idade e métodos para apresentar informações.

# 49. Criar classe ContaBancaria
# Descrição: Criar uma classe ContaBancaria com métodos para sacar, depositar e verificar saldo.

# 50. Criar classe Produto
# Descrição: Criar uma classe Produto com atributos nome, preço e quantidade, e método para calcular valor total.


class Bola:
    def __init__(self,cor,circunfer,material):
        self.cor = cor
        self.circunfer = circunfer
        self.material = material
Bola1 = Bola("amarelo", 2 ,"Plastico")
print(Bola1.cor)


class Quadrado:
    def __init__(self,lado):
        self.lado = lado
    def Metodo(self):
        return "P = ", self.lado * 4 , ", A = ", self.lado * self.lado
Quadrado1 = Quadrado(4)
print(Quadrado1.Metodo())


class pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def metodo(self):
        return "My name is ",self.nome,"I have", self.idade
pessoa1 = pessoa("Luis",23)
print(pessoa1.metodo())


class contaB:
    def __init__(self,saldo):
        self.saldo = saldo
    def sacar(self,saque):
        self.saldo = self.saldo - saque
    def depositar(self,deposito):
        self.saldo = self.saldo + deposito
    def checar(self):
        return self.saldo
contaB1 = contaB(10)


class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def calcular(self):
        return self.nome, " Preço: ",self.quantidade * self.preco
Produto1 = Produto('lapis',12.99,4)
print(Produto.calcular(Produto1))


# -------------------------
# NÍVEL 9 — PROJETOS REAIS
# -------------------------

# 51. Criar jogo de adivinhação
# Descrição: Desenvolver um jogo onde o usuário tenta adivinhar um número aleatório.


import random
numero = random.randint(1, 100)
tent = 0
cont = 0
print("Voce tem ate 6 tentativas para conseguir acertar o numero!\nO Numero esta entre 1 e 100")
while cont != 6:
    tent = int(input("Chute?"))
    if tent != numero:
        if numero > tent:
            print("Numero e Maior! ")
        else: print("Numero e Menor! ")
    cont += 1
    if numero == tent:
        print("Parabens, voce conseguiu!")
        break


# 52. Criar jogo da forca
# Descrição: Criar um jogo de forca com palavras pré-definidas ou carregadas de arquivo.


plv = "forca"
plv2 = list(plv)
cont = 5
progresso = ["_"] * len(plv2)
print("Voce possui 5 tentativas!\nDica: Jogou ou joga a muito pouco tempo!")
while cont != 0:
    print("\nPalavra:", " ".join(progresso))
    tent = input("Chute uma letra: ")
    acertou = False
    for i in range(len(plv2)):
        if tent == plv2[i]:
            progresso[i] = tent
            acertou = True
    if acertou:
        print("Você acertou uma letra!")
    else:
        cont -= 1
        print("Erro! Tentativas restantes:", cont)
    if "_" not in progresso:
        print("\nVocê ganhou!")
        print("Palavra:", "".join(progresso))
        break
if "_" in progresso:
    print("\nVocê perdeu")
    print("A palavra era:", plv)


# 53. Criar agenda de contatos
# Descrição: Criar um sistema que armazena nomes, telefones e e-mails de contatos.


contatos = {
    "Luis":{"nome":"luis", "numero":123 ,"email":"luis@"},
    "Felipe":{"nome":"felipe", "numero":456 ,"email":"felipe@"}
}
def menu():
    print("selecione uma opção:")
    op = input("1 - Adicionar contato\n2 - Ver contatos\n3 - Sair")
    if op == "1":
        adicionar()
    elif op == "2":
        ver()
    elif op == "3":
        return False
    else: print("Selecione uma opção válida!")
def adicionar():
    r = input("Deseja adicionar um novo contato?\nTecle 1 para sim e 0 para não!")
    if r == "1":
        nome = input("Digite o nome: ")
        numero = input("Digite o número: ")
        email = input("Digite o email: ")
        contatos[nome] = {
            "nome": nome,
            "numero": numero,
            "email": email
        }
        print("Contato adicionado!")
    else: return
def ver():
    print(contatos)
    return
def sair():
    print("Voce saiu.")
while True:
    if menu() == False:
        sair()
        break


# 54. Criar sistema bancário simples
# Descrição: Criar um sistema que permita criar contas, depositar, sacar e verificar saldo.


conta = {
    "Luis":{"nome":"luis", "saldo":20},
    "Felipe":{"nome":"felipe", "saldo":45}
}

def menu():
    print("Selecione uma opçao:")
    op = input("1 - Criar Conta\n2 - Depositar\n3 - Sacar\n4 - Ver\n5 - Sair")
    if op == "1":
        criar()
    elif op == "2":
        depositar()
    elif op == "3":
        sacar()
    elif op == "4":
        ver()
    elif op == "5":
        return False
    else:
        print("Selecione uma opção válida!")

def criar():
    nome = input("Digite o nome do usuario: ")
    if nome in conta:
        print("Usuario ja Existente!")
        return False
    saldo = 0
    conta[nome] = {
        "nome": nome,
        "saldo": 0
    }
    print(f"Usuário {nome} foi criado com sucesso!")
    return False

def depositar():
    n = input("Qual o nome do usuario desejado?")
    if n in conta:
        saldo = int(input("Digite o valor do deposito: "))
        conta[n]["saldo"] += saldo
    else: print("Digite um usuario valido!")
    return False

def sacar():
    n = input("Qual o nome do usuario desejado?")
    if n in conta:
        saldo = int(input("Digite o valor do saque: "))
        if conta[n]["saldo"] >= saldo:
            conta[n]["saldo"] -= saldo
        else: print("Valor insuficiente! ")
    else: print("Digite um usuario valido!")
    return False

def ver():
    n = input("Qual o nome do usuario desejado?")
    if n in conta:
        print(conta[n]["saldo"])
    else: print("Digite um usuario valido!")
    return False


# 55. Criar gerenciador de tarefas
# Descrição: Criar um sistema para adicionar, remover e listar tarefas.


lista = []
def adcinar():
    t = input("Tarefa a ser adicionada? ")
    if t in lista:
        print("Tarefa já existe!")
    else: lista.append(t)
    return
def remover():
    t = input("Tarefa a ser removida? ")
    if t in lista:
        lista.remove(t)
        print("Tarefa removida!")
    else: print("Tarefa não listada!\nTente novamente!")
    return
def listar():
    print(lista)
    return


# 56. Criar calculadora completa
# Descrição: Criar uma calculadora que realize operações básicas como soma, subtração, multiplicação e divisão.


def menu():
    print("Calculadora, Qual tipo de operação você quer fazer?")
    r = input("1 Para soma:\n2 Para subtração:\n3 Para multiplicação:\n4 para divisão: ")
    if r == "1":
        soma()
    elif r == "2":
        sub()
    elif r == "3":
        multi()
    elif r == "4":
        divi()
    else: print("Escolha um op valida!")
    return False

def soma():
    x1 = float(input("Primeiro numero a ser somado? "))
    x2 = float(input("Segundo numero a ser somado? "))
    print("O resultado e: " , (x1 + x2))
    return
def sub():
    x1 = float(input("Primeiro numero a ser subtraido? "))
    x2 = float(input("Segundo numero a ser subtraido? "))
    print("O resultado e: " , (x1 - x2))
    return
def multi():
    x1 = float(input("Primeiro numero a ser multiplicado? "))
    x2 = float(input("Segundo numero a ser multiplicado? "))
    print("O resultado e: " , (x1 * x2))
    return
def divi():
    x1 = float(input("Primeiro numero a ser dividido? "))
    x2 = float(input("Segundo numero a ser dividido? "))
    print("O resultado e: ", (x1 / x2))
    return


# 57. Criar controle de estoque
# Descrição: Criar um sistema que gerencia produtos, quantidades e preços em estoque.


produtos = {
    "Mesas":{"nome":"mesa_grande", "quantidade":2 , "valor": 80.99},
    "Cadeiras":{"nome":"cadeira_grande", "quantidade":5 , "valor": 20.00}
}
def menu():
    print("Produtos Cadastrados: " , produtos)
    r = input("Qual Produto deseja gerenciar? ")
    if r in produtos:
        print(produtos[r]["nome"])
        gerenciar(r)
    else: print("Não Encontrado, tente novamente!")
    return
def gerenciar(r):
    if r in produtos:
        x = input("Se deseja alterar a quantidade ou valor digite 1!\n"
              "Se deseja adicionar a quantidade ou valor digite 2!\n"
              "Se deseja reduzir a quantidade ou valor digite 3!")
        if x == "1":
            q = int(input("Nova Quantidade: "))
            produtos[r]["quantidade"] = q

        elif x == "2":
            q = int(input("Quantidade a ser adicionada: "))
            produtos[r]["quantidade"] += q

        elif x == "3":
            q = int(input("Quantidade a ser subtraida: "))
            produtos[r]["quantidade"] -= q
menu()


# 58. Criar sistema de login
# Descrição: Criar um sistema de autenticação de usuários com cadastro e senha.


usuario = {"luis123": "123luis"}
def menu():
    print("Bem vindo a autentificação, para continuar informe: ")
    r = input("Caso ja possua uma conta digite 1!\nCaso queira fazer um cadastro digite 2!")
    if r == "1":
        l = input("Digite seu login: ")
        if l in usuario:
            s = input("Digite sua senha: ")
            if s == usuario[l]:
                print("Bem vindo!")
            else: print("Senha Incorreta!")
            return
        else: print("Usuario Incorreto!")
        return
    elif r == "2":
        print("Bem vindo ao Cadastro!")
        cadastro()
    else: print("De uma resposta valida!")
    return
def cadastro():
    n = input("Digite seu novo Login: ")
    if n in usuario:
        print("Usuario ja existe! ")
        return
    else: s = input("Digite sua senha: ")
    usuario[n] = s
    print("Sua conta foi criada, Parabens.")


# 59. Criar gerador de senhas
# Descrição: Criar um sistema que gera senhas aleatórias com diferentes níveis de complexidade.


import random
def n1():
    c = ""
    while len(c) < 8:
        c += random.choice("abcdefghijklmnopqrstuvwxyz")
    print("Sua senha e: " , c)

def n2():
    c = ""
    while len(c) < 8:
        l = random.choice("abcdefghijklmnopqrstuvwxyz")
        n = random.choice("0123456789")
        c += l
        c += n
    print("Sua senha e: ", c)

def n3():
    c = ""
    c += random.choice("abcdefghijklmnopqrstuvwxyz").upper()
    while len(c) < 7:
        c += random.choice("abcdefghijklmnopqrstuvwxyz")
        c += random.choice("0123456789")
    while len(c) < 8:
        c += random.choice("!@#$%*")
    print(c)
# Letra maiúscula no início de propósito, para seguir o normalmente feito!

def gerar():
    r = int(input("Qual o Nivel de complexidade você deseja?\n1 - Somente letras\n2 - Letras e numeros\n3 - Completo!"
                  "\n Numero 1 a 3? "))
    if r == 1:
        n1()
    elif r == 2:
        n2()
    elif r == 3:
        n3()
    else:
        print("Digite um numero de 1 a 3!")
        return
gerar()


# 60. Criar simulador de caixa eletrônico
# Descrição: Criar um sistema que simula operações de um caixa eletrônico, como saque, depósito e consulta de saldo.


conta = {"nome":"luis", "senha":"luis123", "saldo":20}

def menu():
    r = input("Digite o nome para começar: ")
    if r == conta["nome"]:
        r2 =  input("Digite a Senha: ")
        if r2 == conta["senha"]:
            print("Bem vindo!")
            caixa()
        else:
            print("Senha incorreta!")
            return menu()
    else:
        print("Usuario Incorreto!")
        return menu()

def caixa():
    r = int(input("Tecle 1 para verificar o saldo!\nTecle 2 para realizar um saque!"
                  "\nTecle 3 para realizar um deposito!\nTecle 4 para sair!\nResposta: "))
    if r == 1:
        saldo()
    elif r == 2:
        saque()
    elif r == 3:
        deposito()
    elif r == 4:
        print("Obrigado.")
        return menu()
    else:
        print("Digite uma opçao valida")
        return caixa()

def saldo():
    s = conta["saldo"]
    print("O saldo da sua conta e : " , s)
    return caixa()

def saque():
    r = float(input("Digite um valor a ser sacado!"))
    if r <= conta["saldo"]:
        conta["saldo"] -= r
        return caixa()
    else:
        print("Saldo insuficiente!")
        return caixa()
def deposito():
    r = float(input("Digite um valor a ser depositado!"))
    conta["saldo"] += r
    return caixa()


# 61. Jogo de adivinhação avançado
# Descrição: Criar uma versão do jogo de adivinhação com dicas para o usuário.


palavra = "arroz"
i = palavra[0]
f = palavra[-1]
c = 0
print("A palavra estará em letra minuscula!\n"
      "Você tem 3 tentativas!\n"
      "Dica 1: A palavra começa com a letra:", i, ","
      " e termina com a letra:", f,
      "\nDica 2: A palavra tem exatas:", len(palavra), "Letras!")
while c < 3:
    r = input("Chute uma palavra: ").lower()
    if r != palavra:
        print("Tente novamente!")
        c += 1
    else:
        print("Você acertou!")
        break
if c == 3 and r != palavra:
    print("Número máximo de tentativas atingido!")


# 62. Sistema de votação
# Descrição: Criar um sistema que registra votos e mostra o resultado final.


v1 = 0
v2 = 0
t = 0
while t != 5:
    r = int(input("Qual se voto?\n1 para v1 e 2 para v2"))
    if r == 1:
        v1 += 1
        t += 1
    elif r == 2:
        v2 += 1
        t += 1
    else: print("Digite um numero valido!")
if v1 > v2:
    print("V1 ganhou")
else:
    print("V2 ganhou")


# 62. Agenda com arquivos
# Descrição: Criar uma agenda de contatos que salva e lê dados de arquivos.


def menu():
    print("Bem, vindo ao menu!")
    r = int(input("Para adicionar um contato digite 1!\n"
                  "Para visualizar um contato digite 2!\n"))
    if r == 1:
        adicionar()
    elif r == 2:
        visualizar()
    else:
        print("Digite um numero valido!")
        return menu()
def adicionar():
    with open("agenda.txt", "r+") as r:
        conteudo = r.read()
        nome = input("Digite o nome do contato: ")
        if nome in conteudo:
            print("Contato ja existe!")
        else:
            numero = input("Digite o numero do contato: ")
            r.write(f"{nome}:{numero}\n")
            print("Contato adicionado!")
def visualizar():
    with open("agenda.txt", "r") as r:
        conteudo = r.read()
        print(conteudo)
menu()

# 63. Sistema financeiro simples
# Descrição: Criar um sistema que registra receitas, despesas e calcula saldo.


receitas = 0
despesas = 0

def menu():
    print("Bem vindo(a) ao menu!")
    r = int(input("Para visualizar seu total de Despesas ou receitas? tecle 1!\n"
                  "Para gerenciar as receitas, tecle 2!\n"
                  "Para gerenciar as despesas tecle 3!"))
    if r == 1:
        visu()
    elif r == 2:
        rece()
    elif r == 3:
        desp()
    else:
        print("Digite um numero valido!")
        return menu()
def visu():
    r = int(input("Para visualizar suas despesas e suas receitas? tecle 1!\n"
              "Para visualizar suas Receitas, tecle 2\n"
              "Para visualizar suas Despesas, tecle 3!"))
    if r == 1:
        print("Seu total de receitas e: ",receitas)
        print("Seu total de despesas e: ",despesas)
        saldo = receitas - despesas
        print("Seu saldo é:", saldo)
    elif r == 2:
        print("Seu total de receitas e: ",receitas)
        saldo = receitas - despesas
        print("Seu saldo é:", saldo)
    elif r == 3:
        print("Seu total de despesas e: ",despesas)
        saldo = receitas - despesas
        print("Seu saldo é:", saldo)
    else:
        print("Digite um valor valido!")
        return visu()
def rece():
    global receitas
    r = int(input("Para retirar um valor das receitas, tecle 1!\n"
                  "Para acresentar um valor as receitas, tecle 2!"))
    if r == 1:
        v = int(input("Digite o valor que gostaria de retirar: "))
        if  receitas >= v:
            receitas -= v
            print("Valor alterado!")
            saldo = receitas - despesas
            print("Seu saldo é:", saldo)
            return menu()
        else:
            print("Valor insuficiente!")
            return rece()
    elif r == 2:
        v = int(input("Digite o valor que gostaria de acresentar: "))
        receitas += v
        print("Valor alterado!")
        saldo = receitas - despesas
        print("Seu saldo é:", saldo)
        return menu()
    else:
        print("Digite um valor valido!")
        return rece()
def desp():
    global despesas
    r = int(input("Para retirar um valor das despesas, tecle 1!\n"
                   "Para acresentar um valor as despesas, tecle 2!"))
    if r == 1:
        v = int(input("Digite o valor que gostaria de retirar: "))
        if  despesas >= v:
            despesas -= v
            print("Valor alterado!")
            saldo = receitas - despesas
            print("Seu saldo é:", saldo)
            return menu()
        else:
            print("Valor insuficiente!")
            return desp()
    elif r == 2:
        v = int(input("Digite o valor que gostaria de acresentar: "))
        despesas += v
        print("Valor alterado!")
        saldo = receitas - despesas
        print("Seu saldo é:", saldo)
        return menu()
    else:
        print("Digite um valor valido!")
        return desp()

"""















