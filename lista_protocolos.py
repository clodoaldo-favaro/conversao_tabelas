from sys import argv
from os.path import join

with open( join('..', '..', 'AGTMAPTI'), 'rb') as file:
    with open(argv[0][:len(argv[0]) - 2] + 'csv', 'w') as relatorio:
        for linha in file:
            protocolo = linha[1:11].decode('utf-8').lstrip('0')
            

input('Encerrar')            