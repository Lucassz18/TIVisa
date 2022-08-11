import time, sys, os
count = 0
vezes = 0
achados = 0

achou = []
notificar = []
lista = [
	1,25875,112634,32404,22612,25362,18233,25739,20469,20163,22834,51556,56941,69787,63880,19570,25268,90976,112597,18081,83967,23709,60226,108298,22214,16668,44764,30968,18450,
	90974,18569,32608,23287,60929,47300,39825,115567,56949,70403,117224,48519,23304,23283,116680,108300,20169,24938,115253,108352,70038,49981,25352,51558,43823,44561,58407,112610,
	49206,21386,23831,115271,25036,17457,116060,69764,18240,1752,60228,116665,116675,18564,41856,18382,44645,20193,25377,18354,67011,46441,23360,25886,46161,25855,65338,40032,12489,
	26136,12487,39846,24881,21151,66464,19001,16247,24952,24978,23069,29604,40974,40969,23416,18344,25001,18753,23415,1751,29787,40126,24899,23097,26171,18571,2,3,4,5,6,7,8,9,10
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
		print('Consta na Lista das Medidas Administrativas')
		print(f'O auto é o número {lista.index(auto)} no bloco das Medidas Administrativas\n')
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
				print(f'Número {lista.index(auto)} da lista, continue.')
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
		print('\n')
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
