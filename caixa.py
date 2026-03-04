from time import sleep
saldo = 1000.0
nome = str(input('Digite seu nome: '))
while True:
    print(' ' * 30)
    print('Carregando...')
    print(' ' * 30)
    sleep(2)
    print('•' * 50)
    print(f'''O que você quer fazer hoje, {nome}?
    [1]Ver saldo
    [2]Sacar
    [3]Depositar
    [4]Sair''')
    print('•' * 50)
    op = int(input('Digite sua opção: '))
    if op == 1:
        print(f'Seu saldo é R${saldo}')
    elif op == 2:
        saque = float(input('Quanto você quer sacar? '))
        while True:
            if saque > saldo:
                print('Você não pode sacar essa quantia! Tente novamente.')
                break
            else:
                print('Carregando saque...')
                saldo -= saque
                print(f'Você sacou R${saque}, seu saldo atual é R${saldo}')
                break
    elif op == 3:
        deposito = float(input('Quanto você quer depositar? '))
        saldo += deposito
        print(f'Você depositou R${deposito}, seu saldo atual é R${saldo}')
    elif op == 4:
        break
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer voltar para o menu? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('Saindo...')