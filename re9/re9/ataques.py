
import random
class Ataques():

        

        
    
    def ataque_heroi(self,modificador_dano,heroi_dano, inimigo_vida ):
        critico = random.randint(1,20)
        if critico >14:
            if inimigo_vida < 0:
                inimigo_vida = 0            
            dano_critico = (heroi_dano + heroi_dano * 1.5)
            inimigo_vida = (inimigo_vida - (dano_critico))
            if inimigo_vida < 0:
                inimigo_vida = 0
        else:
            if inimigo_vida < 0:
                inimigo_vida = 0            
            inimigo_vida = (inimigo_vida - (heroi_dano * modificador_dano))
            if inimigo_vida < 0:
                inimigo_vida = 0


    def ataque_inimigo(self, heroi_vida, inimigo_dano):
        if heroi_vida < 0:
            heroi_vida = 0
        heroi_vida = (heroi_vida - inimigo_dano)
        if heroi_vida < 0:
            heroi_vida = 0
        
