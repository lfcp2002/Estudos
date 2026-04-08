
/* 

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



console.log("ola mundo");


let numero =  prompt("qual o numero? ");
console.log(numero);
alert(numero);


let numero1 = Number(prompt("numero 1? "))
let numero2 = Number(prompt("numero 2? "))
let soma = (numero1) + (numero2);
alert (soma);


let nota1 = Number(prompt("1 nota? "));
let nota2 = Number(prompt("2 nota? "));
let nota3 = Number(prompt("3 nota? "));
let nota4 = Number(prompt("4 nota? "));
let media = ((nota1) + (nota2) + (nota3) + (nota4)) / 4;
alert(media);


let valor = Number(prompt("Qual sua altura? "));
let cm = valor * 100;
alert("sua altura em cm e: " + cm);



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



let raio = 3;
let areaa = Math.PI * raio ** 2;
console.log(areaa);


let lado1 = 5;
let area = lado1 * lado1;
let dobro = area * 2;
console.log(area);
console.log(dobro);


let horast = 8;
let valorph = 7.50;
let salario = horast * valorph
let salarioM = salario * 30;
console.log(salario);
console.log(salarioM);


let tempF = 230
let FpC = 5 / 9 * (tempF - 32); 
console.log(FpC);


let tempC = 30;
let CpF = 1.8 * tempC + 32;
console.log(CpF);



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



let numer00 = prompt("numero 0? ");
let numer01 = prompt("numero 1? ");
if (numer00 > numer01){
    console.log("Numero 0 e maior!")
} else{
    console.log("Numero 1 e maior!")
}


let numero = 2
if (numero > 0){
    console.log("positivo")
} else {
    console.log("negativo")
}


let nalea = 28;
if (nalea %  2 == 0){
    console.log("par")
} else{
    console.log("impar")
}


let vogal = ["a", "e", "i", "o", "u"];
let teste = prompt("letra? ").toLowerCase();
if (vogal.includes(teste)){
    console.log("Vogal! ")
} else {
    console.log("Consoante! ")
}


let numeros = 1;
let numero = 2;
let numer = 3;

if (numeros > numero && numeros > numer) {
    console.log(numeros);
} else if (numero > numeros && numero > numer) {
    console.log(numero);
} else {
    console.log(numer);
}



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



let numeros = [2,4,6];

numeros.sort((a,b) => b - a);
console.log(numeros);


let ano = 2026;

if ((ano % 4 == 0 && ano % 100 != 0) || ano % 400 == 0){
    console.log("ano bissexto");
} else {
    console.log("nao");
}


let triangulo = lado1 + lado2 > lado3 && lado2 + lado3 > lado1 && lado3 + lado1 > lado2;
if (triangulo) {
    console.log("sim");
} else {
    console.log("nao");
}


let nmax = 20;
let nmin = 1;

while(nmin <= nmax){
    nmin += 1
    console.log(nmin)
}


let fim = 50;
let comeco = 0;
while (comeco <= fim){
    if (comeco % 2 != 0){
        console.log(comeco);
    }
    comeco ++
}

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



let tabuada = 1;
let numero = (prompt("numero?"));

while (tabuada <= 10){
     console.log(numero * tabuada)
     tabuada += 1
}


let numero = Number(prompt("Digite um número:"));
let resultado = 1;

while (numero > 1) {
    resultado *= numero;
    numero--;
}

console.log("Fatorial =", resultado);


let max = 1000;
let n1 = 0;
let n2 = 1;

while (n1 <= max) {
    console.log(n1);

    let proximo = n1 + n2;
    n1 = n2;
    n2 = proximo;
}


let numero = Number(prompt("Digite um número:"));

while (numero !== 0) {
    numero = Number(prompt("Digite outro número:"));
}

console.log("fim"); 


let numero = Number(prompt("número? (0 para parar):"));
let pares = 0;

while (numero !== 0) {
    if (numero % 2 === 0) {
        pares++;
    }
    numero = Number(prompt("Digite outro número:"));
}

console.log("Quantidade de pares:", pares);

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


let contagem = 0;
let numeros = [];
let teste;

while (contagem != 5){
    teste = prompt("Numeros?");
    contagem += 1;
    numeros.push(teste) 
}

if (numeros.length == 5) {
    console.log(numeros);
}


let lista = [1,2,3];
console.log(lista.reverse());


let list = [5,4,8,9,2,4];
let soma = 0;
let i = 0;

while (i < list.length) {
    console.log(list[i]);
    soma += list[i];
    i++;
    
}

console.log(soma / list.length);


let list = [1,2,3,4,5,6];
let listP = [];
let listI = [];
let i = 0;

function Separador () {
    while (i < list.length){
        console.log(list[i])
        if (list[i] % 2 == 0) {
            listP.push(list[i]);
        } else {listI.push(list[i]);}
        i++
    }
return `Lista Par: ${listP} | Lista Impar: ${listI}`;
}
Separador();


let list1 = [1,3,5];
let list2 = [2,4,6];
let list3 = [];
let tt = list1.length + list2.length;
let i1 = 0;
let i2 = 0;

function Intercalador () {

    while (tt > list3.length) {
        if (i1 < list1.length){
        console.log(list1[i1])
        list3.push(list1[i1])
        i1 ++
        }
        if (i2 < list2.length){
        console.log(list2[i2])
        list3.push(list2[i2])
        i2 ++
        }
    }
return list3
}

*/







