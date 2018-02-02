import os

with open(os.path.join('..', '..', 'AGTMAPTIREDUZIDO.txt'), 'r') as file:
    with open(os.path.join('COLUNA_188.txt'), 'w') as dest:
        for linha in file:
            if linha[188] == 'N':
                dest.write(linha)
input('Encerrar')