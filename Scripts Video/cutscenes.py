from gerenciador import *
from dicionarios import *


class Cutscene:
    def __init__(self, falas, fala_final):

        # Variáveis da Cutscene
        self.timer = pygame.time.get_ticks()

        self.fala_final = fala_final
        self.etapa = 0
        self.falas = falas

        # Parametros para escrever a fala na tela
        self.velocidade_fala = 0.2
        self.inicio_fala = 0
        self.numero_fala = self.falas[0]

        # Parametros da funcao colocar_texto
        self.tamanho = 40
        self.cor = BRANCO
        self.pos_x = 50
        self.pos_y = 50

        self.cutscene_running = True

    def update(self):
        apertar = pygame.key.get_pressed()
        espaco = apertar[pygame.K_SPACE]

        # print(self.numero_fala)
        if self.etapa < self.fala_final:
            if int(self.inicio_fala) < len(self.numero_fala):
                self.inicio_fala += self.velocidade_fala
            else:
                if espaco:
                    self.etapa += 1
                    self.inicio_fala = 0
                    self.numero_fala = self.falas[self.etapa]

        elif self.etapa >= self.fala_final:
            if int(self.inicio_fala) < len(self.numero_fala):
                self.inicio_fala += self.velocidade_fala
            else:
                if espaco:
                    self.cutscene_running = False
        return self.cutscene_running

    def draw(self, janela):

        text = self.numero_fala
        colocar_texto(
            janela,
            text[0:int(self.inicio_fala)],
            self.tamanho,
            self.cor,
            self.pos_x,
            self.pos_y
        )
