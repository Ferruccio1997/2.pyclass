CONSTANTE_BONUS = 1000

nome = input('Digite seu nome: ')

if nome.isdigit():
    print('Digitou um numero no nome. Digite um nome valido!')
elif len(nome) == 0:
    print('Digite um nome válido!')
elif nome.isspace():
    print('Digitou somente espaço. Digite um nome valido!')
else:
    try:
        salario = round(float(input('Digite seu salario: ')),2)
        bonus = round(float(input('Digite o bonus: ')),2)
    except ValueError:
        print('Digite um numero valido!')
        exit()

    resultado_b = CONSTANTE_BONUS + round(salario * (bonus),2)

    print(f'Ola {nome}, tudo bem? \n Seu salário é R${salario} e com o percentual de {bonus}% o se bonus é R${resultado_b}')