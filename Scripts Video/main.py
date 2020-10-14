import sys
# Pygame já foi importada dos outros módulos
from cutscenes import *
from dicionarios import *
from gerenciador import Gerenciador

pygame.init()
tela = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

BRANCO = (255, 255, 255)

gerenciador = Gerenciador(tela)

cut1 = Cutscene(cutscene1, 2)
cut2 = Cutscene(cutscene2, 2)

cutscene_playing = True
while cutscene_playing:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill(BRANCO)

    gerenciador.cut_scene_start(cut1)

    gerenciador.draw()

    gerenciador.update()

    # Linha de debug, ignorar
    # print(gerenciador.cut_scene_running)

    pygame.display.flip()




