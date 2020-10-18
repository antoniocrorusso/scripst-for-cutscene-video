import pygame

# Criar a função de colocar texto
def colocar_texto(tela, texto, tamanho, cor, pos_x, pos_y):
    font = pygame.font.SysFont(None, tamanho)
    text_surface = font.render(texto, True, cor)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (pos_x, pos_y)
    tela.blit(text_surface, text_rect)

#Criar a classe gerenciador
class Gerenciador:
    # Criar o método de inicialização
    def __init__(self, janela):
        # Declarar as varáveis de armazenamento da cutscene
        self.cutscene = None
        self.cutscene_is_running = False

        # Declarar as variáveis dos parâmetros
        self.janela = janela
        self.altura_janela = 0

    # Criar o método start
    def cutscene_start(self, cutscene):
        # Colocar os valores dos parâmetros nas variáveis
        self.cutscene = cutscene
        self.cutscene_is_running = True

    # Criar o método end
    def cutscene_end(self):
        # Resetar os valores das variáveis
        self.cutscene = None
        self.cutscene_is_running = False

    # Criar o método update
    def update(self):
        # Checar se a cutscene está rodando ou não
        if self.cutscene_is_running:
            # Se estiver
            if self.altura_janela < self.janela.get_height() * 0.3:
                self.altura_janela += 3
                # Checar se a caixa de diálogo está desenhada
            self.cutscene_is_running = self.cutscene.atualizacao()
                # Chamar o método de atualização
        else:
            # Se não
            self.cutscene_end()
            # Chamar o método End

    # Criar o método draw
    def draw(self):
        # Desenhar a caixa de diálogo
        if self.cutscene_is_running:
            pygame.draw.rect(self.janela, (0, 0, 0), (0, 0, self.janela.get_width(), self.altura_janela))

            # Desenhar a fala da cutscene
            self.cutscene.desenhar_o_texto(self.janela)
