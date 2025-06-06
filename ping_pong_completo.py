from direct.showbase.ShowBase import ShowBase   # Importa a classe base do Panda3D para criar a aplicação
from panda3d.core import CardMaker               # Importa ferramenta para criar formas retangulares 2D
from direct.task import Task                       # Importa a classe Task para usar tarefas que rodam a cada frame
from direct.task.TaskManagerGlobal import taskMgr # Gerenciador global de tarefas
import random                                     # Para gerar números aleatórios
import time                                       # (não usado aqui, pode ser removido)

# Classe principal do jogo, herda de ShowBase (base para apps Panda3D)
class MyApp(ShowBase):
    def __init__(self):
        super().__init__()   # Inicializa a classe base ShowBase
        self.disable_mouse()  # Desliga o controle do mouse para não interferir na câmera

        # Criamos o formato do paddle: um quadrado 0.2 x 0.2 (de -0.1 a 0.1 nas duas direções)
        cm = CardMaker("q")
        cm.setFrame(-0.1, 0.1, -0.1, 0.1)

        # Paddle esquerdo: cria um node 2D com o formato, pinta vermelho e posiciona no lado esquerdo
        self.q1 = self.render2d.attachNewNode(cm.generate())
        self.q1.setColor(1, 0, 0, 1)  # vermelho
        self.q1.setPos(-0.9, 0, 0)    # quase no limite esquerdo

        # Paddle direito: igual, mas azul e no lado direito
        self.q2 = self.render2d.attachNewNode(cm.generate())
        self.q2.setColor(0, 0, 1, 1)  # azul
        self.q2.setPos(0.9, 0, 0)

        # Cria a bolinha: um quadrado menor (0.1 x 0.1) amarelo no centro
        ball_cm = CardMaker("ball")
        ball_cm.setFrame(-0.05, 0.05, -0.05, 0.05)
        self.ball = self.render2d.attachNewNode(ball_cm.generate())
        self.ball.setColor(1, 1, 0, 1)  # amarelo
        self.ball.setPos(0, 0, 0)       # centro

        # Velocidade da bola nos eixos z inicializada com 0 (bola parada)
        self.ball_dz = 0

        # Posiciona a bola no centro e programa seu lançamento
        self.reset_ball()

        # Adiciona tarefa para atualizar a posição da bola a cada frame
        taskMgr.add(self.atualizar_bola, "atualizar_bola")

        # Mapeia teclas para mover os paddles
        self.accept("arrow_up", self.mover, [self.q1, 0, 0.05])    # seta cima move paddle esquerdo para cima
        self.accept("arrow_down", self.mover, [self.q1, 0, -0.05]) # seta baixo move paddle esquerdo para baixo
        self.accept("w", self.mover, [self.q2, 0, 0.05])           # 'w' move paddle direito para cima
        self.accept("s", self.mover, [self.q2, 0, -0.05])          # 's' move paddle direito para baixo

    # Função para mover paddles
    def mover(self, node, dx, dz):
        # Pega a posição atual e soma o deslocamento recebido
        x = node.getX() + dx
        z = node.getZ() + dz

        # Limita o movimento para não sair da tela (entre -0.9 e 0.9 no x, -0.9 e 0.9 no z)
        x = max(-1 + 0.1, min(1 - 0.1, x))
        z = max(-1 + 0.1, min(1 - 0.1, z))

        # Aplica a nova posição ao paddle
        node.setPos(x, 0, z)

    # Reposiciona a bola no centro e programa o lançamento com atraso
    def reset_ball(self):
        self.ball.setPos(0, 0, 0)   # posiciona no centro
        self.ball_dx = 0            # zera velocidade no eixo x
        self.ball_dz = 0            # zera velocidade no eixo z

        # Depois de 1 segundo, chama a função para lançar a bola
        taskMgr.doMethodLater(1, self.lancar_bola, "lancar_bola")

    # Função que dá velocidade inicial para a bola
    def lancar_bola(self, task):
        # Define velocidade aleatória entre -0.5 e 0.5 nos eixos x e z (direção e sentido aleatórios)
        self.ball_dx = 0.5 * random.choice([-1, 1])
        self.ball_dz = 0.5 * random.choice([-1, 1])
        return Task.done  # termina a tarefa agendada

    # Função chamada a cada frame para atualizar a posição da bola
    def atualizar_bola(self, task):

        # Calcula nova posição somando velocidade * tempo
        x = self.ball.getX() + self.ball_dx * dt
        z = self.ball.getZ() + self.ball_dz * dt

        # Verifica se bateu nas bordas superior ou inferior (limites da tela no eixo z)
        if z > 1 - 0.05 or z < -1 + 0.05:
            self.ball_dz *= -1  # inverte a direção vertical (rebote)

        # Verifica colisão com paddle esquerdo (x da bola próximo ao paddle esquerdo)
        if x - 0.05 <= self.q1.getX() + 0.1:
            # Se a bolinha está na altura do paddle (dentro da faixa do paddle)
            if abs(z - self.q1.getZ()) <= 0.1:
                self.ball_dx *= -1  # inverte a direção horizontal (rebote)
                # Ajusta a posição da bola para não "entrar" no paddle
                x = self.q1.getX() + 0.1 + 0.05

        # Verifica colisão com paddle direito
        if x + 0.05 >= self.q2.getX() - 0.1:
            if abs(z - self.q2.getZ()) <= 0.1:
                self.ball_dx *= -1
                x = self.q2.getX() - 0.1 - 0.05

        # Verifica se a bola passou da tela (gol)
        if x < -1 or x > 1:
            self.reset_ball()  # reposiciona a bola no centro e relança após 1 segundo
            return Task.cont  # continua a tarefa

        # Atualiza a posição da bola com os novos valores calculados
        self.ball.setPos(x, 0, z)
        return Task.cont  # continua a tarefa para o próximo frame

# Instancia a aplicação e roda o loop principal do Panda3D
MyApp().run()