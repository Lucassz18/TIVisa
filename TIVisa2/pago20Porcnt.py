import time, sys, os
from listasTest import Listas

count = 0
vezes = 0
achados = 0

achou = []
notificar = []
lista = Listas.lista_Pago20C()

print('-' * 40)
print(f'{"Bem-Vindo!":^40}')
print(f'{"Para parar a busca, digite 0":^40}')
print('-' * 40)

while True:

	auto = int(input('Digite o número do auto: '))
	vezes += 1
	if auto not in lista and auto != 0:
		notificar.append(auto)

	if auto in lista:

		print('\n')
		print('Consta na Lista dos pagos com desconto.')
		print(f'O auto é o número {lista.index(auto)} no bloco dos pagos com desconto.\n')
		count += 1
		achados += 1
		achou.append(auto)
		
		if vezes == 5:

			vezes -= 5
			print('\n')
			print('Aguarde...')

			for i in range(0, 2):
					sys.stdout.flush()
					time.sleep(1)
			os.system('cls')
			print(f'Você parou no auto {auto},')

			if auto in lista:
				print(f'Número {lista.index(auto)} da lista dos pagos com desconto, continue.')
			else:
				print('O auto não foi encontrado na lista.')

		if count == 5:

			count -= 5
			print(f'Parabéns, você já encontrou {achados} autos!')
			print('\n')
			continuar = str(input('Deseja continuar procurando? [S/N] ')[0].upper().strip())

			if continuar == 'N':

				print('-' * 40)
				print(f'Você achou os seguintes autos...\n {achou}\n')
				print(f'Você achou', len(achou), 'autos\n')
				print(f'Você procurou os seguintes autos...\n {notificar}\n')
				print(f'Você pesquisou', len(notificar), 'autos')
				print('-' * 40)
				print('Até logo!')

				fechar = str(input('Fechar Programa? [S/N] ')[0].upper().strip())

				if fechar == 'S':

					print('Fechando Programa...')
					print('-' * 40)
					for i in range(0, 3):
						sys.stdout.flush()
						time.sleep(1)
					break

	elif auto == 0:
		continuar = int(input("\nDeseja continuar procurando: SIM = 1 / NÃO = 2: "))
		if continuar == 2:
			print('-' * 40)
			print(f'Você achou os seguintes autos...\n {achou}\n')
			print(f'Você achou', len(achou), 'autos\n')

			print(f'Você procurou os seguintes autos...\n {notificar}\n')
			print(f'Você pesquisou', len(notificar), 'autos')
			print('-' * 40)
			print('Até logo!')

			fechar = str(input('Fechar Programa? [S/N] ')[0].upper().strip())
			if fechar == 'S':
				print('Fechando Programa...')
				print('-' * 40)
				for i in range(0, 3):
					sys.stdout.flush()
					time.sleep(1)
				break

	else:

		print('Não consta na Lista.')
		print('\n')

		if vezes == 5:

			vezes -= 5
			print('Aguarde...')
			for i in range(0, 2):
					sys.stdout.flush()
					time.sleep(1)
			os.system('cls')
			print(f'Você parou no {auto}, continue.')
