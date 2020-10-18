import pygame
from gerenciador import colocar_texto

# Criar a classe Cutscene
class Cutscene:
    # Criar o metodo de init
    def __init__(self, dialogos, fala_final):
        # Criar as variaveis para desenhar o texto pela função
        self.tamanho = 40
        self.cor = (255, 255, 255)
        self.pos_x = 50
        self.pos_y = 50

        # Criar as variáveis de exibição de fala
        self.fala_final = fala_final
        self.etapa = 0
        self.falas = dialogos

        # Criar as variáveis de controle da classe
        self.velocidade_fala = 0.2
        self.inicio_fala = 0
        self.numero_fala = self.falas[self.etapa]

        # Criar a variável de retorno da atualizaçãp
        self.cutscene_rodando = True

    # Criar o método atuialização e suas checagens
    def atualizacao(self):
        # Colocar o evento de apertar espaço
        apertar = pygame.key.get_pressed()
        espaco = apertar[pygame.K_SPACE]

        # Colocar as checagens
        if self.etapa < self.fala_final:
            if int(self.inicio_fala) < len(self.numero_fala):
                self.inicio_fala += self.velocidade_fala
            else:
                if espaco:
                    self.etapa += 1
                    self.inicio_fala = 0
                    self.numero_fala = self.falas[self.etapa]

        elif self.etapa == self.fala_final:
            if int(self.inicio_fala) < len(self.numero_fala):
                self.inicio_fala += self.velocidade_fala
            else:
                if espaco:
                    self.inicio_fala = 0
                    self.cutscene_rodando = False

        # Colocar o retorno de acordo com a variável anterior
        return self.cutscene_rodando

    # Criar o método de desenhar texto
    def desenhar_o_texto(self, janela):
        # atribuir a variável de texto ao parâmetro texto da função
        texto = self.numero_fala

        # Colocar a função de desenhar o texto
        colocar_texto(
            janela,
            texto[0:int(self.inicio_fala)],
            self.tamanho,
            self.cor,
            self.pos_x,
            self.pos_y
        )
