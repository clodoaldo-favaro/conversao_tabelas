import os

with open(os.path.join('..', '..', 'AGTMAPTIREDUZIDO.txt'), 'r') as file:
    with open(os.path.join('coluna_394_398.txt'), 'w') as dest:
        for linha in file:
            if linha[393:398] != '00000':
                dest.write(linha)
input('Encerrar')