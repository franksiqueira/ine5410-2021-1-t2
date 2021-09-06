from time import sleep
from random import randint
import sys, argparse

from nadador import *
from funcionario import *

# Parâmetros do nadador
tempo_troca_min              = 5
tempo_troca_max              = 15
tempo_ducha_min              = 3
tempo_ducha_max              = 10
tempo_nadando_min            = 50
tempo_nadando_max            = 90
tempo_entre_nadadores_min    = 2
tempo_entre_nadadores_max    = 15

# Quantidades de recursos da academia
quant_armarios_por_vestiario = 10
quant_duchas_por_vestiario   = 3
quant_raias                  = 8
quant_pranchas               = 4

# Parâmetros do funcionário
tempo_limpeza_vestiario      = 20
tempo_limpeza_ducha          = 5
tempo_descanso               = 20

# Tempo total de simulação. Encerrado esse tempo, não crie mais nadadores.
tempo_total                  = 1000

# Uma unidade de tempo de simulação. Quanto menor, mais rápida a execução.
unidade_de_tempo             = 0.1 # 100ms

# Varíaveis e estruturas globais necessárias para implementação do programa
piscina = []                   # Adicione todos os nadadores que estão na piscina a essa lista
raias_ocupadas = 0             # Registre quantas raias estão em uso

# IMPLEMENTE AQUI:
# Defina outras varíaveis e estruturas globais necessárias para implementação do programa

if __name__ == "__main__":
    # Verifica a versão do python
    if sys.version_info < (3, 0):
        sys.stdout.write('Utilize python3 para desenvolver este trabalho\n')
        sys.exit(1)

    # Processa os argumentos de linha de comando
    parser = argparse.ArgumentParser()
    parser.add_argument("--unidade_de_tempo", "-u", help="valor da unidade de tempo de simulação")
    parser.add_argument("--tempo_total", "-t", help="tempo total de simulação")
    parser.add_argument("--tempo_entre_nadadores_min", "-nmin", help="intervalo mínimo entre a criação de dois nadadores")
    parser.add_argument("--tempo_entre_nadadores_max", "-nmax", help="intervalo máximo entre a criação de dois nadadores")

    args = parser.parse_args()
    if args.unidade_de_tempo:
        unidade_de_tempo = float(args.unidade_de_tempo)
    if args.tempo_total:
        tempo_total = int(args.tempo_total)
    if args.tempo_entre_nadadores_min:
        tempo_entre_nadadores_min = int(args.tempo_entre_nadadores_min)
    if args.tempo_entre_nadadores_max:
        tempo_entre_nadadores_max = int(args.tempo_entre_nadadores_max)
    
    # Tempo desde a abertura da academia
    tempo = 0

    # IMPLEMENTE AQUI: crie as varíaveis locais usadas pelo programa

    # IMPLEMENTE AQUI: Criação do funcionário
  
    # Enquanto o tempo total de simuação não for atingido
    while tempo < tempo_total:
        # IMPLEMENTE AQUI: Criação de um nadador, usando valores aleatórios

        # Aguarda um tempo aleatório antes de criar o próximo nadador
        intervalo = randint(tempo_entre_nadadores_min, tempo_entre_nadadores_max)  
        sleep(intervalo * unidade_de_tempo)     
        # Atualiza a variável tempo considerando o intervalo de criação dos nadadores
        tempo += intervalo

    # IMPLEMENTE AQUI:
    # Aguarde a finalização (término) de todos os nadadores e do funcionário 
    # antes de encerrar o programa.
