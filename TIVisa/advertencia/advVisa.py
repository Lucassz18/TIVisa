import time, sys, os

count = 0
vezes = 0
achados = 0

achou = []
notificar = []
lista = [1,46177,18624,50414,23596,17040,65426,10624,24721,24017,117536,117514,66320,113673,65427,114606,27411,32401,60667,66337,87686,17236,25278,1805,64151,
    30800,19606,2312,20853,38232,86662,18701,11039,45911,31128,18617,24965,87691,68105,25035,2219,22338,14682,11574,24556,21815,3105,21140,38546,44563,48293,
    17490,17451,23151,18288,18121,66318,67001,69620,51341,17207,19318,2445,112003,31093,23331,58191,21181,12484,27009,108042,23479,7828,23923,11488,22997,32210,
    20817,31109,23352,10651,86663,26807,12514,23562,22583,23564,25627,18319,17709,40412,23122,90991,31514,14881,64191,16645,47822,116145,29988,29976,27713,31561,
    33154,18413,17714,1883,112639,22623,24969,112637,70082,67137,21565,31078,2094,29502,20434,30866,26125,18352,26148,18697,23991,25055,56822,27072,27221,27225,
    112519,66151,23632,2291,23987,30858,23837,27715,27005,26493,18616,21848,40783,21171,31865,42129,19320,17921,18573,18402,67006,13004,12464,9093,19321,24930,
    22222222222222,22222222222222,22222222222222,22222222222222,22222222222222,
    34497,59542,112657,103018,30854,23371,68958,25137,22536,56613,50055,41341,69781,21756,31118,29653,12467,15545,60005,
    66577,26487,22627,22566,21174,23904,41858
	]

print('-' * 40)
print(f'{"Bem-Vindo!":^40}')
print(f'{"Para parar a busca, digite 0":^40}')
print('-' * 40)

while True:

	auto = int(input('Digite o número do auto: '))
	vezes += 1
	notificar.append(auto)

	if auto == '17898':
		auto = '10651'

	elif auto in lista:

		print('\n')
		print('Consta na Lista das advertências')
		print(f'O auto é o número {lista.index(auto)} no bloco das advertências\n')
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
				print(f'Número {lista.index(auto)} da lista das advertências, continue.')
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
