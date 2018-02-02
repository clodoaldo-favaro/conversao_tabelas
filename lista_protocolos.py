from sys import argv
from os.path import join

lista = {}

with open( join('..', '..', 'AGTMAPTI'), 'rb') as file:
    with open(argv[0][:len(argv[0]) - 2] + 'csv', 'w') as relatorio:
        for linha in file:
            protocolo = linha[1:11].decode('utf-8').lstrip('0')
            
            data_aponte = linha[15:23].decode('utf-8')
            ano = data_aponte[0:4]
            mes = data_aponte[4:6]
            dia = data_aponte[6:]
            data_aponte = dia +'/' + mes + '/' + ano
            lista[protocolo] = data_aponte


with open('DIGITALIZACOES.txt', 'w') as file:
    for protocolo, data in lista.items():
        file.write("{:<7} {}\n".format(protocolo, data))


            


input('Encerrar')            