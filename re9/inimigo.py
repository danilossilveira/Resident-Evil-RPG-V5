import random
import time

from personagem import Personagem

class Inimigo(Personagem):

    def __init__(self, nome, equipamento, dano,vida,tipo,nivel = int):
        
        super().__init__(nome,equipamento,dano, vida,nivel)
        self.tipo = tipo
        self.nivel = nivel
        self.dano = dano
        self.vida = vida
                        
    def __str__(self):
        return f'{self.nivel} | {self.dano} | {self.vida}'

    def tela_de_morte(self):
        print(f'Você olha enquanto {self.nome} se desfaz no chão')
        time.sleep(0.5)

    def determir_nivel(self,nivel_heroi):
        vida = self.vida
        dano = self.dano
        self.nivel = random.randint(1,(nivel_heroi + 2))
        self.vida = vida + (self.nivel * 2)
        self.dano = dano + (self.nivel * 2)
        
  

