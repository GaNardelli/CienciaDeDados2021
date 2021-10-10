""" O jogo da vida """

import copy, random, sys, time

# Preparando o ambiente inicial do jogo, colocando as células em posições vivas e mortas aleatoriamente

largura = 79 # largura do tabuleiro
altura = 20 # altura do tabuleiro

vivo = 'O' # representa celula viva
morto = ' ' # representa celula morta

proximaCelula = {}

for x in range(largura):
    for y in range(altura):
        # fazer uma chance de 50%
        if random.randint(0,1) == 0:
            proximaCelula[(x,y)] = vivo
        else:
            proximaCelula[(x,y)] = morto

while True: # Script de loop principal
    celulas = copy.deepcopy(proximaCelula) # copia a posição inicial
    
    # Mostar as celulas na tela
    for y in range(altura):
        for x in range(largura):
            print(celulas[(x,y)], end='')
        print()

    # Calcular o proximo grupo de celulas baseado nas celulas antigas
    for x in range(largura):
        for y in range(altura):
            # Pegar as coordenadas vizinhas
            esquerda = (x-1) % largura
            direita = (x+1) % largura
            acima = (y-1) % altura
            abaixo = (y+1) % altura

            # Contar o numero de vizinhos vivos
            numero_de_vizinhos = 0
            if celulas[(esquerda, acima)] == vivo:
                numero_de_vizinhos += 1 # Acima a equerda
            if celulas[(x, acima)] == vivo:
                numero_de_vizinhos += 1 # Diretamente acima
            if celulas[(direita, acima)] == vivo:
                numero_de_vizinhos += 1 # Direita acima
            if celulas[(esquerda, y)] == vivo:
                numero_de_vizinhos += 1 # a esquerda
            if celulas[(direita, y)] == vivo:
                numero_de_vizinhos += 1
            if celulas[(esquerda, abaixo)] == vivo:
                numero_de_vizinhos += 1
            if celulas[(x, abaixo)] == vivo:
                numero_de_vizinhos += 1
            if celulas[(direita, abaixo)] == vivo:
                numero_de_vizinhos += 1

            if celulas[(x, y)] == vivo and (numero_de_vizinhos == 2 or numero_de_vizinhos ==3):
                proximaCelula[(x,y)] = vivo 
            elif celulas[(x,y)] == morto and numero_de_vizinhos == 3:
                proximaCelula[(x,y)] = vivo
            else:
                proximaCelula[(x,y)] = morto

    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        print("O jogo da vida :D")
        sys.exit()