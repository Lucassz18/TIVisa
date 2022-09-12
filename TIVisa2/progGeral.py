import time, sys, os
from listasTest import Listas

vezes = 0

listaPagoCheio = Listas.lista_Pago_Cheio()
listaPago20C = Listas.lista_Pago20C()
listaCobranca = Listas.lista_Cobranca()
listaAdvertencia = Listas.lista_Advertencia()
listaMedidaAdm = Listas.lista_Medida_Adm()

print(f'{"-" * 85:^40}')
print(f'\nOlá, veja em qual dos blocos encontra-se o auto que quer pesquisar.'
f"\n\nFavor colocar somente números."
f"\n\nCaso queira finalizar a busca, digite 0.\n"
f'{"-" * 85:^40}')

listaTot = len(listaAdvertencia + listaCobranca + listaMedidaAdm + listaPago20C + listaPagoCheio)
listaTotAdv = len(listaAdvertencia)
listaTotCo = len(listaCobranca)
listaTotMadm = len(listaMedidaAdm)
listaTotPagoCD = len(listaPago20C)
listaTotPagoCh = len(listaPagoCheio)

print(f"Existem {listaTot} autos somando todas as listas.\n"
f"Existem {listaTotAdv} autos na lista de Advertência.\n"
f"Existem {listaTotCo} autos na lista de Cobrança.\n"
f"Existem {listaTotMadm} autos na lista de Medida Administrativa.\n"
f"Existem {listaTotPagoCD} autos na lista de Pagos com desconto.\n"
f"Existem {listaTotPagoCh} autos na lista de Pagos cheio.\n"
f"Quantidade de processos atualizada em: 15/07/2022.")
print('-' * 85)

while True:
    
    auto = int(input("Digite o número do auto: "))
    vezes += 1

    class ListasTotais():   
        #Função para declarar dentro da classe que cada parametro receberá o valor da variável 
        def __init__(self, listaPagoCheio, listaPago20C, listaCobranca, listaAdvertencia, listaMedidaAdm, vezes):

            self.listaPagoCheio = listaPagoCheio
            self.listaPago20C = listaPago20C
            self.listaCobranca = listaCobranca
            self.listaAdvertencia = listaAdvertencia
            self.listaMedidaAdm = listaMedidaAdm
            self.vezes = vezes

        def listas(self, auto, vezes):

            '''if vezes == 5:
                print('Aguarde...')
                for i in range(0, 2):
                    sys.stdout.flush()
                    time.sleep(1)
                os.system('cls')
                print(f'Você parou no auto {auto},')
                vezes -= 5'''

            if auto in self.listaPagoCheio:
                print("O auto está na lista dos Pagos cheios.\n")

            elif auto in self.listaPago20C:
                print("O auto está na lista dos Pagos com desconto.\n")

            elif auto in self.listaCobranca:
                print("O auto está na lista de Cobrança.\n")

            elif auto in self.listaAdvertencia:
                print("O auto está na lista de Advertencia.\n")

            elif auto in self.listaMedidaAdm:
                print("O auto está na lista de Medida Administrativa.\n")

            elif auto == 0:
                print("Solicitação recebida.\n")

            else:
                print("O auto não está em nenhuma lista.\n")

    if __name__=="__main__":
        mostrarLista = ListasTotais(listaPagoCheio, listaPago20C, listaCobranca, listaAdvertencia, listaMedidaAdm, vezes)
        mostrarLista.listas(auto, vezes)

    if auto == 0:
        continuar = int(input("\nDeseja continuar procurando: SIM = 1 / NÃO = 2: "))

        if continuar == 1:
            print("\n")
            print('-' * 40)
            print('Fechando Programa...')
            print('-' * 40)
            for i in range(0, 3):
                sys.stdout.flush()
                time.sleep(1)
            break
