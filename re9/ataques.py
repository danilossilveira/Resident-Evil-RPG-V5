
import random
class Ataques():
    #def ataque_critico(self, inimigo_vida, heroi_dano):
        

        
    
    def ataque_normal(self,modificador_dano,heroi_dano, inimigo_vida ):
            inimigo_vida = (inimigo_vida - (heroi_dano * modificador_dano))
            if inimigo_vida < 0:
                inimigo_vida = 0


    def dano_critico(self,heroi_dano, inimigo_vida ):       
        dano_critico = round((heroi_dano + (heroi_dano * 1.5)),1)
        inimigo_vida = (inimigo_vida - dano_critico)
        if inimigo_vida < 0:
            inimigo_vida = 0

    
    def ataque_inimigo(self, heroi_vida, inimigo_dano):
        heroi_vida = (heroi_vida - inimigo_dano)
        if heroi_vida < 0:
            heroi_vida = 0
        
