import os

with open(os.path.join('..', '..', 'AGTMAPTIREDUZIDO.txt'), 'r') as file:
    with open(os.path.join('forma_intimacao.txt'), 'w') as dest:
        for linha in file:
            if linha[435:437] != 'AR' and linha[435:442] != 'PESSOAL' and linha[435:441] != 'EDITAL':
                dest.write(linha)
input('Encerrar')