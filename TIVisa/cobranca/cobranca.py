import time, sys, os
count = 0
vezes = 0
achados = 0
achou = []
notificar = []
lista = [1,50932,112562,113118,42571,68101,67502,111981,21854,23712,22173,46548,50747,45388,51332,70074,40961,22793,90998,60007,49037,														
    120703,18028,34491,65208,15049,58996,18321,23830,39550,30859,23841,21474,31026,57756,33139,56335,26140,25552,115007,22856,57712,18665,														
    61589,44550,65207,60249,17426,69180,59633,70072,110229,63899,41919,51616,25121,26307,20280,25129,25370,18235,20288,23507,23393,27403,														
    23040,72502,18241,48772,26544,22613,17778,31076,25249,11570,32593,69175,53749,25658,21331,46863,65554,68017,31607,15221,26063,17773,														
    115009,46435,65194,44637,32604,57848,17222,18221,115579,112612,27979,28397,21617,50440,26678,21510,18535,17205,21390,45235,17422,17569,														
    27685,22535,18229,90979,26406,26149,57433,18178,18197,21152,23282,18016,23964,23205,27702,17753,22490,19387,11571,57434,26496,25876,														
    23111,18712,64158,66338,64173,27727,31637,12994,27679,23042,23567,26048,26803,29662,27080,18227,15174,26436,47805,27749,50244,29952,														
    23978,39830,137209,23072,23907,29452,18725,66285,21928,40801,25491,64467,60441,115024,44743,23958,17779,44742,90913,83703,18556,17892,														
    17739,25749,18173,17425,23984,17491,83966,26499,25345,18244,33158,80406,30943,70090,40585,112332,23221,50237,26634,26564,30957,60010,														
    117504,49580,18189,20812,17208,26573,112599,18014,41855,23208,26144,43711,27281,27689,18019,10638,47297,52005,25207,117522,114616,64782,														
    64491,23944,51317,18583,57996,70397,108039,18670,49665,22830,27623,115268,22481,22479,67357,49711,23578,18665,17830,90985,17446,70095,														
    109282,17421,46152,31069,26053,27624,18582,25149,83992,17513,66557,65430,51183,12481,18151,49908,22290,25165,27630,26824,23701,80619,														
    22587,11573,29668,18648,18259,23279,25499,38203,65416,56247,27007,45929,23339,18757,46741,83705,17568,25226,25582,25740,27993,48875,
    25184,29849,29703,17856,21785,22470,23737,25682,17931,14956
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
		print('Consta na Lista de cobrança')
		print(f'O auto é o número {lista.index(auto)} no bloco da cobrança\n')
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
