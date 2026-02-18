import time

from cores import Cores
from personagem import Personagem

class Herois(Personagem):
    
    def __init__(self, nome, equipamento, dano,vida,vida_maxima,especial,nivel,experiencia):
        super().__init__(nome,equipamento,dano,vida,nivel)
        self.vida_maxima = vida_maxima
        self.especial = especial
        self.experiencia = experiencia
        self.inventario = ['Erva verde','Erva amarela','Spray','Estamina','Barra de proteína','Granada de mão' ,'Granada de luz','Carregador estendido']

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
            input('Precione a tecla "[Enter] ⏎" para continuar...\n')
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
                XP_ganho = (nivel_animigo * 100)
            elif tipo_inimigo == 'normal':
                XP_ganho = (nivel_animigo * 200) 
        
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