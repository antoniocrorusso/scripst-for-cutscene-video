import pygame
import sys
from gerenciador import Gerenciador
from cutscene import Cutscene
from dicionarios import *

tela = pygame.display.set_mode((800, 900))

BRANCO = (255, 255, 255)

# criar um objeto gerenciador a partir da classe
gerenciador = Gerenciador(tela)

# Criar um objeto cutscene utilizando a classe em si e o dicionario de dialogos
cut = Cutscene(dialogo, 4)


is_cutscene_playing = True
while is_cutscene_playing:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Chamando os métodos para exibir a cutscene

    pygame.display.flip()