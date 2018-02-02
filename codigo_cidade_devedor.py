import os

with open(os.path.join('..', '..', 'AGTMAPTIREDUZIDO.txt'), 'r') as file:
    with open(os.path.join('codigo_cidade_devedor.txt'), 'w') as dest:
        for linha in file:
            if linha[431:435] != '7466':
                dest.write(linha)
input('Encerrar')