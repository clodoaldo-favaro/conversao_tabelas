import os

nome = 'coluna_466_467_quant_reapontes.txt'

with open(os.path.join('..', '..', 'AGTMAPTIREDUZIDO.txt'), 'r') as file:
    with open(nome, 'w') as dest:
        for linha in file:
            if not linha[465:467].isdigit() :
                dest.write(linha)
input('Encerrar')

os.startfile(nome)