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

"""









