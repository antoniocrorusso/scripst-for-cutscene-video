import pygame

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)


def colocar_texto(tela, texto, tamanho, cor, pos_x, pos_y):
    font = pygame.font.SysFont(None, tamanho)
    text_surface = font.render(texto, True, cor)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (pos_x, pos_y)
    tela.blit(text_surface, text_rect)


class Gerenciador:
    def __init__(self, janela):
        self.cut_scene = None
        self.cut_scene_running = False

        # Variáveis
        self.janela = janela
        self.tamanho_janela = 0

    def cut_scene_start(self, cut_scene):
        self.cut_scene = cut_scene
        self.cut_scene_running = True

    def cut_scene_end(self):
        self.cut_scene = None
        self.cut_scene_running = False

    def update(self):

        if self.cut_scene_running:
            if self.tamanho_janela < self.janela.get_height() * 0.3:
                self.tamanho_janela += 2
            self.cut_scene_running = self.cut_scene.update()
        else:
            self.cut_scene_end()

    def draw(self):
        if self.cut_scene_running:
            pygame.draw.rect(self.janela, PRETO, (0, 0, self.janela.get_width(), self.tamanho_janela))

            self.cut_scene.draw(self.janela)
