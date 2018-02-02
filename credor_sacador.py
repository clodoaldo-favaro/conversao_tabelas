import os

with open(os.path.join('..', '..', 'AGTMAPTIREDUZIDO.txt'), 'r') as file:
    with open(os.path.join('credor_sacador.txt'), 'w') as dest:
        for linha in file:
            if linha[235:280] != linha[280:325]:
                dest.write(linha)
input('Encerrar')