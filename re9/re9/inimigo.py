import random
import time

from personagem import Personagem

class Inimigo(Personagem):

    def __init__(self, nome, equipamento, dano,vida, vida_maxima, tipo,nivel):
        
        super().__init__(nome,equipamento,dano, vida, vida_maxima, nivel)
        self.tipo = tipo
        
                        
    def __str__(self):
        return (f'''
🔫 EQUIPAMENTO: {self.equipamento} 
❤️  VIDA:        {self.vida}
⚔️  DANO:        {self.dano}

''')

    def tela_de_morte(self):
        print(f'Você olha enquanto {self.nome} se desfaz no chão')
        time.sleep(0.5)

    def determir_nivel(self,nivel_heroi):
        self.nivel = random.randint(1,(nivel_heroi + 2))
        self.vida_maxima = self.vida_maxima + (self.nivel * 2)
        self.dano = self.dano + (self.nivel * 2)
        
        
  

