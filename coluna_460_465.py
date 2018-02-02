import os

nome = 'coluna_459_465.txt'

with open(os.path.join('..', '..', 'AGTMAPTIREDUZIDO.txt'), 'r') as file:
    with open(nome, 'w') as dest:
        for linha in file:
            if linha[459:465] != '      ':
                dest.write(linha)
input('Encerrar')

os.startfile(nome)