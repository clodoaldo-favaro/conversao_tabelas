import os

with open(os.path.join('..', '..', 'AGTMAPTIREDUZIDO.txt'), 'r') as file:
    with open(os.path.join('coluna_428_431.txt'), 'w') as dest:
        for linha in file:
            if linha[428:431] != '000':
                dest.write(linha)
input('Encerrar')