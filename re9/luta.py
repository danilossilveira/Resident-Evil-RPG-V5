import random
import time
import os
import sqlite3
from datetime import datetime
from comentarios import Comentarios
from inimigo import Inimigo
from herois import Herois
from cores import Cores
from personagem_save import Save as s

class Luta():
    
    def voltar_menu():
        print('Opção inválida')
        input('ENTER para voltar')
        os.system('cls')
        Luta.escolher_personagem(Luta)

    def escolher_personagem(self): 

        escolha = input('''
 ╔══════════════════════════════════════════╗
 ║           ESCOLHA SEU PERSONAGEM         ║
 ╠══════════════════════════════════════════╣
 ║  [1] Leon    [2] Chris    [3] Ethan      ║
 ║  [4] Ada     [5] Jill     [6] Hunk       ║
 ║  [7] Wesker                              ║
 ╚══════════════════════════════════════════╝
        \n''')
        conn = s.criar_conexao()
        cursor = conn.cursor()
        cursor.execute(f"""
SELECT * FROM tabelaHerois WHERE id = ?
""", escolha)

        personagem = cursor.fetchall()
        for i in personagem:
            nome = i[1]
            equipamento = i[2]
            dano = i[3]
            vida = i[4]
            vida_maxima = i[5]
            especial = i[6]
            nivel = i[7]
            xp = i[8]
            heroi = Herois(nome,equipamento, dano,vida,vida_maxima,especial,nivel,xp)
            self.personagem_escolhido.__dict__.update(heroi.__dict__)
        print(self.personagem_escolhido, '\n')  
        conn.commit()
        conn.close()
            
    def escolher_inimigo(self):
        i = self.inimigo_escolhido
        equipamento_inimigo = random.randint(0,4)
        nome = ['Ganado','Javo','Cultista','Chrysalid','Walker']
        nome_inimigo = random.randint(0,4)
        vida = [35, 40, 50, 60, 65]
        vida_inimigo = random.randint(0,4)
        dano = [15, 17, 20, 25, 30]
        dano_inimigo = random.randint(0,4)
        
        equipamento = ['Punho','machado','Madeira','Facão','Foice',]
        inimigo = Inimigo(nome[nome_inimigo], equipamento[equipamento_inimigo],dano[dano_inimigo],vida[vida_inimigo],   'normal', 0)
        
        numero_inimigo = int(random.randint(1,12))
        if numero_inimigo >10:
            r = int(random.randint(1,2))
            inimigos = {
                1: self.nemesis,
                2: self.mr_x,
           }
        else:
            r = 1
            inimigos = {
                1: inimigo
            }
            
        i.__dict__.update(inimigos[r].__dict__)
        Inimigo.determir_nivel(i, i.nivel)
        Comentarios.mensagem_inimigo_proximo(self, i.nome, i.equipamento, i.nivel)
        
    def especial(self):

            if self.personagem_escolhido.nome == 'Ethan':
                    self.personagem_escolhido.vida = (self.personagem_escolhido.vida + int(15))
                    print(f'{Cores.AZUL}Você regenerou 15 de vida\n{Cores.RESET}')
            #Leon
            elif self.personagem_escolhido.nome == 'Leon':
                    self.personagem_escolhido.vida = (self.personagem_escolhido.vida + self.inimigo_escolhido.dano)
                    print(f'{Cores.AZUL}Leon deu um  mortal e desviou do ataque\n{Cores.RESET}')
            #Chris
            elif self.personagem_escolhido.nome == 'Chirs':                
                chance = random.randint(1,10)
                if chance >6:
                     Luta.dano_critico(Luta)
            #Ada
            elif self.personagem_escolhido.nome == 'Ada Wong':

                    self.personagem_escolhido.dano = (self.personagem_escolhido.dano + self.personagem_escolhido.dano)
                    print(f'{Cores.AZUL}Dano multiplicado\n{Cores.RESET}')
            #Hunk        
            elif self.personagem_escolhido.nome == 'Hunk':
                hitkill = random.randint(1,5)
                probabildade = random.randint(1,5)
                if hitkill == probabildade:
                    print(f'{Cores.AZUL}PESCOÇO DO INIMIGO QUEBRADO\n{Cores.RESET}')
                    self.inimigo_escolhido.vida = 0
            #Jill
            elif self.personagem_escolhido.nome == 'Jill Valentine':
                if self.personagem_escolhido.vida <= 130 and self.personagem_escolhido.vida > 100:
                    self.personagem_escolhido.dano = 15
                elif self.personagem_escolhido.vida <= 100 and self.personagem_escolhido.vida > 70:
                    self.personagem_escolhido.dano = 16
                elif self.personagem_escolhido.vida <= 70 and self.personagem_escolhido.vida > 30:
                    self.personagem_escolhido.dano = 17
                elif self.personagem_escolhido.vida <= 30 and self.personagem_escolhido.vida > 15:
                    self.personagem_escolhido.vida.dano = 19
                else:
                    self.personagem_escolhido.dano = 50   
                    print(f'{Cores.AZUL}DANO EXTRA\n{Cores.RESET}') 
                           
            elif self.personagem_escolhido.nome == 'Wesker':
                self.inimigo_escolhido.vida = (self.inimigo_escolhido.vida - 70)
                print(f'{Cores.AZUL} Ataque vertical {Cores.RESET}')
                time.sleep(0.5)
                print(f'{Cores.AZUL} Ataque horizontal {Cores.RESET}')
                time.sleep(0.5)
                print(f'{Cores.AZUL} Ataque transversal {Cores.RESET}')

    def barra_vida(self,vida):
        
        barra_personagem = "█" * int(vida // 5) + "░" * int((160 - vida) // 5)
        print(f" HP {vida:>4} HP |{barra_personagem}|")

    def dano_critico(self):
        dano_critico = 0
        dano_critico = round((self.personagem_escolhido.dano + self.personagem_escolhido.dano * 1.5),1)
        if self.inimigo_escolhido.vida < 0:
            self.inimigo_escolhido.vida = 0
        self.inimigo_escolhido.vida = (self.inimigo_escolhido.vida - dano_critico)
        mensagemm = Comentarios.mensagem_dano_critico(self,self.personagem_escolhido.dano, self.inimigo_escolhido.nome )    
        Luta.log_batalha(self)

    def ataque_normal(self,modificador_dano):               
        self.inimigo_escolhido.vida = (self.inimigo_escolhido.vida - (self.personagem_escolhido.dano * modificador_dano))
        if self.inimigo_escolhido.vida < 0:
            self.inimigo_escolhido.vida = 0
        Luta.log_batalha(self)

    def ataque_inimigo(self):
        self.personagem_escolhido.vida = (self.personagem_escolhido.vida - self.inimigo_escolhido.dano)
        if self.personagem_escolhido.vida < 0:
            self.personagem_escolhido.vida = 0
        mensagem = 1 
        Luta.log_batalha(self)

    def log_batalha(self):
        os.system('cls')
        heroi = self.personagem_escolhido
        inimigo = self.inimigo_escolhido
        print('''
============================================================
                     Fase de Combate                        
============================================================
              
              
              ''')
        print('[ JOGADOR ]')
        print(self.personagem_escolhido.nome)
        Luta.barra_vida(self, self.personagem_escolhido.vida)
        print('''
              
------------------------------------------------------------
                     LOG DE BATALHA                         
------------------------------------------------------------''')
        print(Comentarios.mensagem_ataque_heroi(self, self.inimigo_escolhido.nome, self.personagem_escolhido.equipamento))
        print(f'Dano causado: {heroi.dano}')
        print(Comentarios.mensage_ataque_inimigo(self, self.inimigo_escolhido.nome))
        print(f'Dano recebido: {inimigo.dano}')
        print('------------------------------------------------------------')
        #Comentarios.mensagem_ataque_heroi(self, self.inimigo_escolhido.nome, self.personagem_escolhido.equipamento)               
        print('[ INIMIGO ]')
        print(self.inimigo_escolhido.nome)
        Luta.barra_vida(self, self.inimigo_escolhido.vida)

    def drop(self):

        consumiveis = {
        1: 'Erva verde',
        2: 'Erva amarela',
        3: 'Spray',
        4: 'Estamina',
        5: 'Barre de proteina'
    } 
        drop = random.randint(1,5)
        
        self.personagem_escolhido.inventario.append(consumiveis[drop])
        s.drop_item(self, consumiveis[drop])
        print(f'{Cores.AZUL} DROP: {consumiveis[drop] } {Cores.RESET}')      

    def usar_consumivel(self):
        from inventario import Inventario 
        h = self.personagem_escolhido        
        try:
            os.system('cls')       
            menu = int(input(f'''
Seu inventario:
1- Erva verde - Você possui: {h.inventario.count('Erva verde')}                             
2- Erva amarela - Você possui: {h.inventario.count('Erva amarela')}
3- Spray - Você possui: {h.inventario.count('Spray')}
4- Estamina - Você possui: {h.inventario.count('Estamina')}
5- Barra de proteína - Você possui: {h.inventario.count('Barra de proteína')}
6- Granada de mão - Você possui: {h.inventario.count('Granada de mão')}
7- Granada de luz - Você possui: {h.inventario.count('Granada de luz')}
8- Carregador estendido - Você possui: {h.inventario.count('Carregador estendido')}
            '''))
                                        
            if menu == 1 and h.inventario.count('Erva verde') >= 1:
                Inventario.erva_verde(self)
                h.inventario.remove('Erva verde')
                s.remover_item(self,'Erva verde')
           
            elif menu == 2 and h.inventario.count('Erva amarela') >= 1:
                Inventario.erva_amarela(self)
                h.inventario.remove('Erva amarela')
                s.remover_item(self,'Erva amarela')

            elif menu == 3 and h.inventario.count('Spray') >= 1:    
                Inventario.spray(self)
                h.inventario.remove('Spray')
                s.remover_item(self,'Spray')

            elif menu == 4 and h.inventario.count('Estamina') >= 1:
                Luta.dano_critico(Luta)
                h.inventario.remove('Estamina')
                s.remover_item(self,'Estamina')

            elif menu == 5 and h.inventario.count('Barra de proteína') >= 1:
                Luta.especial(Luta)
                h.inventario.remove('Barra de proteína')
                s.remover_item(self,'Barra de proteína')

            elif menu == 6 and h.inventario.count('Granada de mão') >=1:
                Inventario.granada_de_mao(self)
                h.inventario.remove('Granada de mão')
                s.remover_item(self,'Granada de mão')

            elif menu == 7 and h.inventario.count('Granada de luz') >=1:
                Inventario.granada_luz(self) 
                h.inventario.remove('Granada de luz')
                s.remover_item(self,'Granada de luz')

            elif menu == 8 and h.inventario.count('Carregador estendido') >=1:
                Inventario.carregador_estendido(self) 
                h.inventario.remove('Carregador estendido') 
                s.remover_item(self,'Carregador estendido')

            else:
                print('Você não possui este consumivel')     
        except:  print('Escolha uma opção válida')
    
    def save(self):
        h = self.personagem_escolhido

        dataa = datetime.now()
        s.salvar_progresso(self, h.nome, h.equipamento, h.dano, h.vida_maxima, h.vida, h.especial, h.nivel, h.experiencia, dataa)
        print('Salvo com Sucesso')
    
    def carregar_save(self):
        h = self.personagem_escolhido
        conn = s.criar_conexao()
        cursor = conn.cursor()
        cursor.execute(f"""
SELECT id_saves, nome, data FROM  tabelaSaves;
""")
        save = cursor.fetchall()
        for i in save:
            id = i[0]
            nome = i[1]
            data = i[2]
            print(f'SAVE: {id} | PERSONAGEM: {nome} | DATA: {data}')
        escolha = input('Escolha teu save')
        conn.commit()

        cursor.execute(f"""    
        SELECT nome,arma,dano,vidaMaxima,vida,especial,nivel,
    experiencia FROM tabelaSaves WHERE id_saves = {escolha};
""")
        progresso = cursor.fetchall()
        for i in progresso:
            nome = i[0]
            equipamento = i[1]
            dano = i[2]
            vida = i[3]
            vida_maxima = i[4]
            especial = i[5]
            nivel = i[6]
            xp = i[7]
            aaa = Herois(nome,equipamento, dano,vida,vida_maxima,especial,nivel,xp)
            h.__dict__.update(aaa.__dict__)
            print(h, '\n')  
            print(f' {id} | {nome} | {equipamento} | {dano} | {vida} | {vida_maxima} | {especial} | {nivel} | {xp}' )
            
        cursor.execute(f"""
SELECT * FROM tabelaInventario;
""")    

        inventario = cursor.fetchall()
        for i in inventario:
            item = i[0]
            h.inventario.append(item)
            

    def luta(self):
        try:
            luta = Luta()


            #s.criar_tabela_herois()
            #s.criar_tabela_inventario()
            #s.criar_tabela_saves()
            
            
            save = int(input('''
    ┌──────────────┐   ┌───────────────┐
    │ [1] NEW GAME │   │ [2] CONTINUE  │
    └──────────────┘   └───────────────┘
    ''')) 
            if save == 1:
                luta.escolher_personagem()
            else:
                luta.carregar_save()

            luta.escolher_inimigo()
            contador_kills = []
            
            while True:
                opcoes = int(input('''
    ┌────────────┐   ┌──────────┐    ┌────────────┐     
    │ [1] ATACAR │   │ [2] ITEM │    │ [3] SALVAR │    
    └────────────┘   └──────────┘    └────────────┘    
    '''))
                if opcoes == 1:
                    os.system('cls')
                    critico = random.randint(1,20) 
                    especial = random.randint(1,20)          
                    if critico > 15:
                        luta.dano_critico()
                        time.sleep(0.5)
                    elif especial > 15:
                        luta.especial()
                        luta.ataque_normal(1)
                    else:
                        luta.ataque_normal(1)
                        
                    luta.ataque_inimigo()
                if self.inimigo_escolhido.vida <= 0:
                    print(f'''
____________________________________________________
{Cores.VERDE}Você Ganhou! 👌{Cores.RESET}
____________________________________________________
''')
                    contador_kills.append(Herois.contador_kills(self.inimigo_escolhido.tipo))
                    
                    Luta.drop(Luta)
                    Herois.ganhar_experiencia(self.personagem_escolhido,self.inimigo_escolhido.nivel,self.inimigo_escolhido.tipo)
                    Herois.subir_level(self.personagem_escolhido)
                    Herois.exibir_status(self.personagem_escolhido)
                    Luta.escolher_inimigo(Luta)           
                if self.personagem_escolhido.vida <= 0:
                    Herois.tela_de_morte(self.personagem_escolhido,contador_kills)          
                    Luta.escolher_personagem(Luta)
                elif opcoes == 2:
                    
                    Luta.usar_consumivel(Luta)
                elif opcoes == 3:
                    luta.save()  
        except Exception as e: print(f'Esse é o Erro: {e}')


    nemesis = Inimigo('Nemesis','Lança míssil', 25, 150 ,'boss', 0)
    mr_x = Inimigo('Mister X','Soco', 30, 140,'boss' , 0)
    #-
    personagem_escolhido = Herois('a','a',0,0,0,'a', 0, 0)
    inimigo_escolhido = Inimigo('a','a',0, 0,'a',0)

def main():
    luta = Luta()
    luta.luta()
if __name__ == '__main__':
    main() 