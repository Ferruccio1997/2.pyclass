# #### Inteiros (`int`)
#import math

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#print(int(input('Digite um valor: ')) + int(input('Digite outro valor: ')))

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#print(int(input('Digite um valor: ')) % 5)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#print(int(input('Digite um valor: ')) * int(input('Digite outro valor: ')))

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#print(int(input('Digite um valor: ')) // int(input('Digite outro valor: ')))

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#print(int(input('Digite um valor: '))**2)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
#print(float(input('Digite um valor: ')) + float(input('Digite outro valor: ')))

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
#print((float(input('Digite um valor: ')) + float(input('Digite outro valor: ')))/2)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
#print(float(input('Digite um valor: '))**float(input('Digite outro valor: ')))

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#print(float(input('Digite um valor: '))*(9/5) + 32)

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#print((float(input('Digite um valor: '))**2)*math.pi)

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#print(input('Digite uma palavra: ').upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#print(input('Digite uma palavra: ').lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
#print(''.join(input('Digite uma palavra: ').split(' ')))

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#print(input('Digite uma data: ').split('/'))

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
#print(input('Digite seu primeiro nome: ') + ' ' + input('Digite seu sobrenome: '))

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
#print(bool(input('Voce e o Ferruccio? ')) and bool(input('Ferruccio Leal? ')))

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
#print(bool(input('Voce é homem? ')) or bool(input('Joga futebol? ')))

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#print( not bool(input('Voce e Jon Wick? ')))

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#print(input('Forneça um numero: ') == input('Forneça o mesmo número: '))

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
#print(input('Forneça um numero: ') != input('Forneça o mesmo número: '))


# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     print(float(input('Digite os graus em Celsius: ')) * (9/5) + 32)
# except ValueError:
#     print('Voce digitou um texto')


# 22: Verificador de Palíndromo
# palavra = input('Digite um palindromo: ')
# if palavra == palavra[::-1]:
#     print('Palindromo')
# else:
#     print('Nao palindromo')


# 23: Calculadora Simples
# try:
#     numero1 = float(input('Digite um numero: '))
# except ValueError:
#     print('Voce digitou uma string')

# oper = input('Digite a operação: ')
# while oper not in ['+', '-', '*', '/']:
#     oper = input('Digite a operação valida: ')

# try:
#     numero2 = float(input('Digite um numero: '))
# except ValueError:
#     print('Voce digitou uma string')

# print(f'O resultado é {eval(str(numero1) + oper + str(numero2))}')


# 24: Classificador de Números
# try:
#     numero = int(input('Digite um numero inteiro: '))

#     if numero > 0:
#         print('Positivo')
#     elif numero < 0:
#         print('Negativo')
#     else:
#         print('Zero')
    
#     if numero % 2 == 0:
#         print('Par')
#     else:
#         print('Inpar')
# except ValueError:
#     print('Digite um valor inteiro possivel!')


# 25: Conversão de Tipo com Validação
# lista_num = input('Digite numeros inteiros separados por (,): ')
# lista_num = lista_num.split(',')
# num_int = []

# try:
#     for i in lista_num:
#         num_int.append(int(i))
#     print('Os numeros sao: ', num_int)
# except ValueError:
#     print('Digite valores inteiros!')