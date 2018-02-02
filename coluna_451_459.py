import os

with open(os.path.join('..', '..', 'AGTMAPTIREDUZIDO.txt'), 'r') as file:
    with open(os.path.join('coluna_451_459.txt'), 'w') as dest:
        for linha in file:
            if linha[450:459] != 'PAGAMENTO':
                dest.write(linha)
input('Encerrar')