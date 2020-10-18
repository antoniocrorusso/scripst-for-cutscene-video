import pygame
import sys
from gerenciador import Gerenciador
from cutscene import Cutscene
from dicionarios import *

pygame.init()
clock = pygame.time.Clock()

tela = pygame.display.set_mode((800, 900))

BRANCO = (255, 255, 255)

# criar um objeto gerenciador a partir da classe
gerenciador = Gerenciador(tela)

# Criar um objeto cutscene utilizando a classe em si e o dicionario de dialogos
cut = Cutscene(dialogo, 3)


is_cutscene_playing = True
while is_cutscene_playing:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Chamando os métodos para exibir a cutscene
    tela.fill(BRANCO)
    gerenciador.cutscene_start(cut)
    gerenciador.draw()
    gerenciador.update()

    pygame.display.flip()