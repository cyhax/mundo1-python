# Exercícios do Mundo 1 - Curso em Vídeo
# Autor: Cyhax
# Estrutura: Todos os exercícios em um único arquivo, com boas práticas aplicadas

# -------------------- Exercício 1 --------------------
print("Hello, World!")

# -------------------- Exercício 2 --------------------
nome = input('\033[7;30;41mDigite seu nome: \033[m')
print(f'\033[7;30;41mÉ um prazer te conhecer, {nome}!\033[m')

# -------------------- Exercício 3 --------------------
print('-=' * 10)
print('\033[7;31;40mCalculadora de Soma\033[m')
print('-=' * 10)
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print(f'A soma entre {n1:.2f} e {n2:.2f} é = {n1 + n2:.2f}')

# -------------------- Exercício 4 --------------------
print('-=' * 10)
print('\033[7;31;40mIdentificador de tipo\033[m')
print('-=' * 10)
algo = input('Digite algo: ')
print('O tipo primitivo é', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('Está em maiúsculas?', algo.isupper())
print('Está em minúsculas?', algo.islower())
print('Está capitalizado?', algo.istitle())

# -------------------- Exercício 5 --------------------
print('-=' * 10)
print('\033[7;31;40mAntecessor e Sucessor\033[m')
print('-=' * 10)
num = int(input('Digite um número: '))
print(f'Analisando o valor {num} seu sucessor é {num + 1} e seu antecessor é {num - 1}')

# -------------------- Exercício 6 --------------------
print('-='*10)
print('\033[7;31;40mDobro, Triplo e Raiz quadrada\033[m')
num = int(input('Digite um número: '))
print(f'O dobro é = {num*2}')
print(f'O triplo é = {num*3}')
print(f'A raiz quadrada é = {num ** (1/2)}')

# -------------------- Exercício 7 --------------------
print('-='*10)
print('\033[7;31;40mMédia do Enem\033[m')
nota1 = float(input('Digite sua nota em Linguagens, Códigos e suas Tecnologias: '))
nota2 = float(input('Digite sua nota em Ciências Humanas e suas Tecnologias: '))
nota3 = float(input('Digite sua nota em Ciências da Natureza e suas Tecnologias: '))
nota4 = float(input('Digite sua nota em Matemática e suas Tecnologias: '))
nota5 = float(input('Digite sua nota na Redação: '))
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print(f'A sua média no ENEM foi: {media:.2f}')

# -------------------- Exercício 8 --------------------
print('-='*10)
print('\033[7;31;40mMedida\033[m')
medida = float(input('Digite uma medida em metros: '))
print(f'Em cm é = {medida * 100:.0f}')
print(f'Em mm é = {medida * 1000:.0f}')

# -------------------- Exercício 9 --------------------
print('-='*10)
print('\033[7;31;40mTabuada\033[m')
num = int(input('Digite um número para ver a sua tabuada: '))
print(f'{num} x 1 = {num*1}')
print(f'{num} x 2 = {num*2}')
print(f'{num} x 3 = {num*3}')
print(f'{num} x 4 = {num*4}')
print(f'{num} x 5 = {num*5}')
print(f'{num} x 6 = {num*6}')
print(f'{num} x 7 = {num*7}')
print(f'{num} x 8 = {num*8}')
print(f'{num} x 9 = {num*9}')
print(f'{num} x 10 = {num*10}')

# -------------------- Exercício 10 --------------------
print('-='*10)
print('\033[7;31;40mConversor de Moeda\033[m')
n1 = float(input('Quanto dinheiro você deseja converter em R$? '))
print(f'{n1/5.71:.2f} U$D')
print(f'{n1/6.50:.2f} €')
print(f'{n1/0.040:.2f} ¥')
print(f'{n1/0.79:.2f} Yuan')

# -------------------- Exercício 11 --------------------
print('-='*10)
print('\033[7;31;40mTinta para parede\033[m')
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual é a altura? '))
area = largura * altura
print(f'A área é de {area:.2f}m² e você vai precisar de {area/2:.2f} litros de tinta.')

# -------------------- Exercício 12 --------------------
print('-='*10)
print('\033[7;31;40mDesconto de 5%\033[m')
num = float(input('Digite o preço: '))
print(f'O produto com valor de {num:.2f} R$ a 5% de desconto fica {num - (num * 5 / 100):.2f} R$')

# -------------------- Exercício 13 --------------------
print('-='*10)
print('\033[7;31;40mAumento de 15%\033[m')
n1 = float(input('Digite seu salário: '))
aumento = (15/100) * n1
print(f'O seu salário com aumento de 15% fica {n1 + aumento:.2f} R$')

# -------------------- Exercício 14 --------------------
print('-='*20)
print('\033[7;31;40mConversor de graus para Fahrenheit\033[m')
print('-='*20)
graus = float(input('Qual a temperatura em Cº? '))
faren = (graus * 9/5) + 32
print(f'A temperatura em Fahrenheit é {faren:.4f}')

# -------------------- Exercício 15 --------------------
print('-='*10)
print('\033[7;31;40mAluguel de carros\033[m')
print('-='*10)
dias = int(input('Quantos dias o carro foi alugado? '))
kms = float(input('Quantos kms ele rodou? '))
r1 = dias * 60
r2 = kms * 0.15
print(f'O total a pagar é R${r1 + r2:.2f}')

# -------------------- Exercício 16 --------------------
import math
print('-='*10)
print('\033[7;31;40mQuebrando um número\033[m')
print('-='*10)
num = float(input('Digite um número: '))
inteiro = math.trunc(num)
print(f'O número inteiro é {inteiro}')

# -------------------- Exercício 17 --------------------
import math
print('-='*10)
print('\033[7;31;40mHipotenusa\033[m')
print('-='*10)
n1 = float(input('Qual é o cateto oposto? '))
n2 = float(input('Qual é o cateto adjacente? '))
n3 = math.pow(n1, 2)
n4 = math.pow(n2, 2)
op = n3 + n4
hipotenusa = math.sqrt(op)
print(f'A hipotenusa é = {hipotenusa:.2f}')

# -------------------- Exercício 18 --------------------
import math
print('-='*12)
print('\033[7;31;40mSeno, Cosseno e Tangente\033[m')
print('-='*12)
a1 = int(input('Digite um ângulo: '))
r1 = math.radians(a1)
s1 = math.sin(r1)
c1 = math.cos(r1)
t1 = math.tan(r1)
print(f'O seno é {s1:.2f}\nO cosseno é {c1:.2f}\nA tangente é {t1:.2f}')

# -------------------- Exercício 19 --------------------
import random
print('-='*10)
print('\033[7;31;40mSorteando aluno\033[m')
print('-='*10)
nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f'A pessoa escolhida para apagar a lousa é {escolhido}')

# -------------------- Exercício 20 --------------------
import random
print('-='*14)
print('\033[7;31;40mOrdem de apresentação\033[m')
print('-='*14)
nome1 = input('Digite o nome do primeiro aluno: ')
nome2 = input('Digite o nome do segundo aluno: ')
nome3 = input('Digite o nome do terceiro aluno: ')
nome4 = input('Digite o nome do quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print(f'A ordem de apresentação é {lista}')

# -------------------- Exercício 21 --------------------
import pygame
print('-='*10)
print('\033[7;31;40mPlayer Happy Nation\033[m')
print('-='*10)
pygame.mixer.init()
pygame.mixer.music.load('ha.mp3')
pygame.mixer.music.play()
input('Aperte ENTER para parar a música')

# -------------------- Exercício 22 --------------------
print('-='*14)
print('\033[7;31;40mAnalisador de texto\033[m')
print('-='*14)
nome = input('Digite seu nome: ').strip()
print(f'Nome em maiúsculas: {nome.upper()}')
print(f'Nome em minúsculas: {nome.lower()}')
print(f'Total de letras: {len(nome.replace(" ", ""))}')
primeiro_nome = nome.split()
print(f'Seu primeiro nome tem {len(primeiro_nome[0])} letras')

# -------------------- Exercício 23 --------------------
print('-='*15)
print('\033[7;31;40mSeparando dígitos de um número\033[m')
print('-='*15)
num = input('Digite um número de 1 a 9999: ').zfill(4)
print(f'Milhar: {num[0]}')
print(f'Centena: {num[1]}')
print(f'Dezena: {num[2]}')
print(f'Unidade: {num[3]}')

# -------------------- Exercício 24 --------------------
print('-='*22)
print('\033[7;31;40mVerificando as primeiras letras de um texto\033[m')
print('-='*22)
cidade = input('Digite o nome da cidade: ').strip()
print(cidade.upper().startswith('SANTO'))

# -------------------- Exercício 25 --------------------
print('-='*20)
print('\033[7;31;40mProcurando uma string dentro de outra\033[m')
print('-='*20)
nome = input('Digite o seu nome: ').strip()
n1 = nome.upper()
print('SILVA' in n1)

# -------------------- Exercício 26 --------------------
print('-='*21)
print('\033[7;31;40mPrimeira e última ocorrência de uma string\033[m')
print('-='*21)
frase = input('Digite uma frase: ').strip()
maiuscula = frase.upper()
print(f'A letra A aparece {maiuscula.count("A")} vezes')
print(f'A primeira vez ela aparece na posição {maiuscula.find("A")+1}')
print(f'A última vez ela aparece na posição {maiuscula.rfind("A")+1}')

# -------------------- Exercício 27 --------------------
print('-='*18)
print('\033[7;31;40mPrimeiro e último nome de uma pessoa\033[m')
print('-='*18)
nome = input('Digite seu nome: ').strip()
v1 = nome.split()
print(f'O seu primeiro nome é {v1[0]}')
print(f'O seu último nome é {v1[len(v1)-1]}')

# -------------------- Exercício 28 --------------------
import random
print('-='*10)
print('\033[7;31;40mJogo da adivinhação\033[m')
print('-='*10)
res = int(input('Digite um número de 0 a 5: '))
sort = random.randint(0, 5)
print('Você acertou!' if sort == res else f'Você errou! O número era {sort}.')

# -------------------- Exercício 29 --------------------
print('-='*10)
print('\033[7;31;40mCálculo de multa\033[m')
print('-='*10)
vel = int(input('Digite sua velocidade: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado!')
    print(f'A multa ficou em R${multa:.2f}')
else:
    print('Tenha um bom dia')

# -------------------- Exercício 30 --------------------
print('-='*10)
print('\033[7;31;40mPar ou Ímpar\033[m')
print('-='*10)
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('É par')
else:
    print('É ímpar')

# -------------------- Exercício 31 --------------------
print('-='*10)
print('\033[7;31;40mCusto da Viagem\033[m')
print('-='*10)
km = float(input('Quantos km tem a viagem? '))
if km < 200:
    cal = km * 0.50
    print(f'A passagem vai ficar {cal:.2f} R$')
else:
    cal1 = km * 0.45
    print(f'A passagem vai ficar {cal1:.2f} R$')

# -------------------- Exercício 32 --------------------
from datetime import date
print('-='*10)
print('\033[7;31;40mAno bissexto\033[m')
print('-='*10)
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')

# -------------------- Exercício 33 --------------------
print('-='*11)
print('\033[7;31;40mMaior e menor valores\033[m')
print('-='*11)
num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
maior = num
menor = num
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')

# -------------------- Exercício 34 --------------------
print('-='*11)
print('\033[7;31;40mAumento de salário\033[m')
print('-='*11)
salario = float(input('Qual o seu salário? '))
if salario > 1250:
    cnt = (10 / 100) * salario
    print(f'O seu salário com aumento de 10% é {cnt + salario:.2f} R$')
else:
    cnt2 = (15 / 100) * salario
    print(f'O seu salário com aumento de 15% é {cnt2 + salario:.2f} R$')

# -------------------- Exercício 35 --------------------
print('-='*11)
print('\033[7;31;40mAnalisando Triângulo\033[m')
print('-='*11)
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos PODEM formar um triângulo!')
else:
    print('Os segmentos NÃO podem formar um triângulo.')
