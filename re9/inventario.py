import random
from luta import Luta
from cores import Cores
from luta import Luta
from comentarios import Comentarios
class Inventario():

    def erva_verde(self, vida, vida_maxima):
        vida += 30
        if vida > vida_maxima:
            vida = max(0,vida_maxima)
        print(f'{Cores.AMARELO}vida recuperada! \nVida: {vida}{Cores.RESET} ')

    def erva_amarela(self, vida, vida_maxima):
        vida += 35
        vida_maxima += 35
        if vida > vida_maxima -35:
            print(f'{Cores.AMARELO}Você aumentou o limite de vida!\nNova vida: {vida}{Cores.RESET}')
        else:
            print(f'{Cores.AMARELO}vida recuperada! \nVida: {vida}{Cores.RESET} ')    

    def spray(self, vida, vida_maxima):
        vida += 60
        if vida > vida_maxima:
            vida = vida_maxima 
        print(f'{Cores.AMARELO}vida recuperada! \nVida: {vida}{Cores.RESET} ')

    def granada_de_mao(self, vida_inimigo):
        vida_inimigo -= 70
        print(f'💣🔥{Cores.CIANO} Você explodiu o inimigo!{Cores.RESET}')
        print(f'Vida do inimigo: {vida_inimigo}')

    def granada_luz(self):
        luta = Luta()
        escolha = int(input(f'''{Cores.CIANO}Você atordoou o inimigo, você quer fugir da luta ou atacar de novo?
    ┌────────────┐   ┌────────────┐
    │ [1] FUGIR  │   │ [2] ATACAR │
    └────────────┘   └────────────┘
                             {Cores.RESET}'''))
        if escolha == 1:
            print('Você figiu da luta')
            luta.escolher_inimigo()
        else:
            luta.log_batalha(luta.ataque_heroi() )   


    def carregador_estendido(self):
        pass




