import os

with open(os.path.join('..', '..', 'AGTMAPTIREDUZIDO.txt'), 'r') as file:
    with open(os.path.join('codigo_portador.txt'), 'w') as dest:
        for linha in file:
            if linha[389] != '0':
                dest.write(linha)
input('Encerrar')