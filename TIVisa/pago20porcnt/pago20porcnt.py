import time, sys, os

count = 0
vezes = 0
achados = 0

achou = []
notificar = []
lista = [1,50352,22484,21447,72112,23640,59099,27988,67678,18154,25245,26407,23209,23980,22907,59665,26822,49906,59458,22222222222222222,
    222222222222222,25584,45178,66194,69735,54227,65533,23702,38741,103314,41850,29956,26492,120719,45933,18224,18119,11490,26104,18348,27690,
    120569,25054,44741,40586,38554,60850,70548,17948,60893,25603,52006,49032,45660,17894,59347,21750,18328,25136,30951,38206,40123,32240,
    54236,25246,18035,67052,26099,18567,31547,29798,48495,114614,50361,48854,112006,18434,26827,26485,27298,44758,65773,90907,64251,51679,
    18071,115557,41211,25721,39503,23059,50052,18524,26818,40526,25134,24768,46870,49043,71105,115038,18704,17777
	]

print('-' * 40)
print(f'{"Bem-Vindo!":^40}')
print(f'{"Para parar a busca, digite 0":^40}')
print('-' * 40)

while True:

	auto = int(input('Digite o número do auto: '))
	vezes += 1
	notificar.append(auto)



	if auto in lista:

		print('\n')
		print('Consta na Lista dos pagos com desconto')
		print(f'O auto é o número {lista.index(auto)} no bloco dos pagos com desconto\n')
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
