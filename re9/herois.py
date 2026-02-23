import time
import random
from cores import Cores
from personagem import Personagem

class Herois(Personagem):
    
    def __init__(self, nome, equipamento, dano,vida,vida_maxima,especial,nivel,experiencia):
        super().__init__(nome,equipamento,dano,vida, vida_maxima, nivel)
        self.especial = especial
        self.experiencia = experiencia
        self.inventario = []

    def __str__(self):
        return (f'''
=========================================================
 👤 PERSONAGEM: {self.nome}
=========================================================
 🔫  EQUIP: {self.equipamento}      ❤️  VIDA: {self.vida}
 ⚔️  DANO:  {self.dano}              🛡️  ESP: {self.especial}
=========================================================

''')
            


    def exibir_status(self):
        XP_necessario = 1000 + (self.nivel * 200)
        if self.nivel == 10:
            pass
        else:    
            if self.vida_maxima < self.vida:
                self.vida = self.vida_maxima
            print(f'''
     ___________________________________
    |[STATUS ATUAL]              
    |❤️ Vida {round(self.vida,1)}/{round(self.vida_maxima,1)}
    |⭐ Nivel {self.nivel}
    |❇️ Experiência {self.experiencia}/{XP_necessario}
    |___________________________________
    ''')    
            time.sleep(0.5)

    def contador_kills(tipo_inimigo):
        if tipo_inimigo == 'normal':
            return 'n'
        elif tipo_inimigo == 'boss':
            return 'b'   

    def ganhar_experiencia(self, nivel_animigo,tipo_inimigo):
        XP_ganho = 0
        if self.nivel == 10:
            pass
        else:    
            if tipo_inimigo == 'boss':
                XP_ganho = (nivel_animigo * 200)
            elif tipo_inimigo == 'normal':
                XP_ganho = (nivel_animigo * 100) 
        
            self.experiencia += XP_ganho
            print(f'{Cores.VERMELHO}Você recebeu {XP_ganho} de experiencia{Cores.RESET}')
            time.sleep(0.5)

    def subir_level(self):
        if self.nivel == 10:
            print('Você já alcaçou o nivel maximo(10)')
        else:    
            XP_necessario = 1000 + (self.nivel * 500)
            if self.experiencia >= XP_necessario:
                self.nivel += 1
                self.dano = self.dano * 1.3
                #self.vida_maxima = self.vida_maxima * 1.5
                self.vida == self.vida_maxima
                self.experiencia -= XP_necessario
                print(f'{'\033[92m'}Parabéns! {self.nome} subiu para o nível {self.nivel}!{'\033[0m'}')
                time.sleep(0.5)

    def tela_de_morte(self,contador_kills): 
        kill_monstro = 0
        kill_boss = 0
        for contador in contador_kills:
            if contador == 'n':
                kill_monstro += 1
                
            elif contador == 'b':
                kill_boss += 1
        print(f'''
          {Cores.VERMELHO}Ꭹ𝔬𝔲 𝔞𝔯𝔢 𝔡𝔢𝔞𝔡!{Cores.RESET}
              
        Nivel alcançado: {self.nivel}
        Monstros mortos: {kill_monstro}
        Chefes mortos: {kill_boss}
        ''')
        time.sleep(0.5)

    def nivel_heroi (self):
        return self.nivel
    


    def especial_ethan(self):
        self.vida = (self.vida + int(15))
        print(f'{Cores.AZUL}Você regenerou 15 de vida\n{Cores.RESET}')
    def especial_leon(self):
        self.vida = (self.vida + self.dano)
        print(f'{Cores.AZUL}Leon deu um  mortal e desviou do ataque\n{Cores.RESET}')
    def especial_chris(self):
        pass
    def especial_ada(self):
        self.dano = (self.dano + self.dano)
        print(f'{Cores.AZUL}Dano multiplicado\n{Cores.RESET}')
    def especial_hunk(self):      
        hitkill = random.randint(1,5)
        probabildade = random.randint(1,5)
        if hitkill == probabildade:
            print(f'{Cores.AZUL}PESCOÇO DO INIMIGO QUEBRADO\n{Cores.RESET}')
    def especial_jill(self):
        vida = self.vida/15
        self.dano = (self.dano - vida)        
    def especial_wesker(self, vida_inimigo):
                vida_inimigo = (vida_inimigo - 70)
                print(f'{Cores.AZUL} Ataque vertical {Cores.RESET}')
                time.sleep(0.5)
                print(f'{Cores.AZUL} Ataque horizontal {Cores.RESET}')
                time.sleep(0.5)
                print(f'{Cores.AZUL} Ataque transversal {Cores.RESET}')    