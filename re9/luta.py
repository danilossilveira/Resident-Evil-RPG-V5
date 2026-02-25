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
import msvcrt
class Luta():
    def voltar_menu():
        print('Opção inválida')
        input('ENTER para voltar')
        os.system('cls')
        Luta.escolher_personagem(Luta)

    def escolher_personagem(self): 
        itens = ['Leon', 'Chris', 'Ethan','Ada','Jill','Hunk','Wesker']
        index = 0
        while True:
            print(Cores.AMARELO, Cores.RESET,end="", )
            print('''
╔════════════════════════════════════╗
║        ESCOLHA SEU PERSONAGEM      ║
╠════════════════════════════════════╣''')
            for i, item in enumerate(itens):
                if i == index:
                    print(f"║  {Cores.AMARELO}▶ [ {item.ljust(20)} ]{Cores.RESET}") 
                else:
                    print(f"║    {item.ljust(24)}        ║")
            print("╚════════════════════════════════════╝")
            print(" [W/S] Navegar  |  [ENTER] Selecionar")
            tecla = msvcrt.getch().lower()

  
            if tecla == b'w':
                index = (index - 1) % len(itens)
                os.system('cls')
            elif tecla == b's':
                index = (index + 1) % len(itens)
                os.system('cls')
            elif tecla == b'\r':
                os.system('cls')
                print(f"\n Selecionado: {itens[index]} \n".center(60, "-"))
                index+=1
                break

        conn = s.criar_conexao()
        cursor = conn.cursor()
        cursor.execute(f"""
SELECT * FROM tabelaHerois WHERE id = ?
""", (index,))

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
        self.personagem_escolhido.inventario.extend(['Erva verde','Erva amarela','Spray','Estamina','Barra de proteína','Granada de mão' ,'Granada de luz','Carregador estendido','Fita de tinta'])
            
    def escolher_inimigo(self):
        i = self.inimigo_escolhido
        equipamento_inimigo = random.randint(0,4)
        nome = ['Ganado','Javo','Cultista','Chrysalid','Walker']
        nome_inimigo = random.randint(0,4)
        vida = [35, 40, 50, 60, 65]
        vida_maxima = [35, 40, 50, 60, 65]
        vida_inimigo = random.randint(0,4)
        dano = [15, 17, 20, 25, 30]
        dano_inimigo = random.randint(0,4)
        
        equipamento = ['Punho','machado','Madeira','Facão','Foice',]
        inimigo = Inimigo(nome[nome_inimigo], equipamento[equipamento_inimigo],dano[dano_inimigo],vida[vida_inimigo],vida_maxima[vida_inimigo],   'normal', 0)
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
        Inimigo.determir_nivel(self.inimigo_escolhido, self.personagem_escolhido.nivel)
        mensagem = Comentarios.mensagem_inimigo_proximo(self, i.nome, i.equipamento, i.nivel)
        print(mensagem)
        print(inimigo)

    def barra_vida(self,vida, vida_maxima):
        barra_personagem = "█" * int(vida // 5) + "░" * int((vida_maxima - vida) // 5)
        estagio1 = (vida_maxima / 100) * 50
        estagio2 = (vida_maxima / 100) * 30
        cor = 0
        if vida < estagio1 and vida> estagio2:
            cor = Cores.AMARELO
        elif vida < estagio2:
            cor = Cores.VERMELHO
        else:
            cor = Cores.BRANCO
        print(f"{cor} HP {vida:>4} HP |{barra_personagem}|{Cores.RESET}")

    def ataque_heroi(self):
        heroi = self.personagem_escolhido
        inimigo = self.inimigo_escolhido
        chance = 1
        critico = random.randint(chance,20)
        chance = 14
        if heroi.nome == 'Chris':
            chance = 10
        if critico > chance:
            dano_normal = heroi.dano       
            vida_nova = (inimigo.vida - dano_normal)
            inimigo.vida = max(0,vida_nova)
            mensagem = Comentarios.mensagem_ataque_heroi(self, inimigo.nome, dano_normal)

        else:
            dano_critico = (heroi.dano + heroi.dano * 1.5)
            vida_nova = (inimigo.vida - heroi.dano)
            inimigo.vida = max(0,vida_nova)            
            mensagem = Comentarios.mensagem_dano_critico(self,dano_critico, inimigo.nome) 
        return (mensagem)      

    def ataque_inimigo(self):       
        heroi = self.personagem_escolhido
        inimigo = self.inimigo_escolhido        
        vida_nova = (heroi.vida - inimigo.dano)
        heroi.vida = max(0,vida_nova)

    def especial(self):
        heroi = self.personagem_escolhido
        inimigo = self.personagem_escolhido
        if heroi.nome == 'Ethan':
                heroi.vida = (heroi.vida + int(15))
                print(f'{Cores.AZUL}Você regenerou 15 de vida\n{Cores.RESET}')
        #Leon
        elif heroi.nome == 'Leon':
           heroi.vida = (heroi.vida + inimigo.dano)
           print(f'{Cores.AZUL}Leon deu um  mortal e desviou do ataque\n{Cores.RESET}')

        #Ada
        elif heroi.nome == 'Ada Wong':
            heroi.dano = (heroi.dano + heroi.dano)
            print(f'{Cores.AZUL}Dano multiplicado\n{Cores.RESET}')
            #Hunk        
        elif heroi.nome == 'Hunk':
            hitkill = random.randint(1,5)
            probabildade = random.randint(1,5)
            if hitkill == probabildade:
                print(f'{Cores.AZUL}PESCOÇO DO INIMIGO QUEBRADO\n{Cores.RESET}')
                inimigo.vida = 0
            #Jill
            elif heroi.nome == 'Jill Valentine':
                vida = heroi.vida/15
                self.dano = (self.dano - vida)         
                           
            elif heroi.nome == 'Wesker':
                inimigo.vida = (inimigo.vida - 70)
                print(f'{Cores.AZUL} Ataque vertical {Cores.RESET}')
                time.sleep(0.5)
                print(f'{Cores.AZUL} Ataque horizontal {Cores.RESET}')
                time.sleep(0.5)
                print(f'{Cores.AZUL} Ataque transversal {Cores.RESET}')    

    def log_batalha(self, ataque):
        luta = Luta()
        os.system('cls')
        heroi = self.personagem_escolhido
        inimigo = self.inimigo_escolhido
        print(f'''
{Cores.AZUL_CLARO}============================================================{Cores.RESET}
                     Fase de Combate                        
{Cores.AZUL_CLARO}============================================================{Cores.RESET}
              ''')
        print('[ JOGADOR ]')
        print(heroi.nome)
        Luta.barra_vida(self, heroi.vida, heroi.vida_maxima)
        print(f'''

{Cores.AZUL_CLARO}------------------------------------------------------------{Cores.RESET}
                     LOG DE BATALHA                         
{Cores.AZUL_CLARO}------------------------------------------------------------{Cores.RESET}''')
        print(ataque)
        print(f'Dano causado: {heroi.dano}\n')        
        print(Comentarios.mensage_ataque_inimigo(self, inimigo.nome))
        print(f'Dano recebido: {inimigo.dano}')
        print(f'{Cores.AZUL_CLARO}------------------------------------------------------------{Cores.RESET}\n')

        print('[ INIMIGO ]')
        print(inimigo.nome)
        Luta.barra_vida(self, inimigo.vida, inimigo.vida_maxima)

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
        print(f'{Cores.AZUL} DROP: {consumiveis[drop] } {Cores.RESET}')      

    def usar_consumivel(self):
        from inventario import Inventario 
        inventario = Inventario()
        luta = Luta()
        h = self.personagem_escolhido 
        i = self.inimigo_escolhido       
        #try:
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
            inventario.erva_verde(h.vida, h.vida_maxima)
            h.inventario.remove('Erva verde')

        elif menu == 2 and h.inventario.count('Erva amarela') >= 1:
            inventario.erva_amarela(h.vida, h.vida_maxima)
            h.inventario.remove('Erva amarela')
            h.vida_maxima = (h.vida_maxima + 35)
        elif menu == 3 and h.inventario.count('Spray') >= 1:    
            inventario.spray(h.vida, h.vida_maxima)
            h.inventario.remove('Spray')

        elif menu == 4 and h.inventario.count('Estamina') >= 1:
            dano_critico = (h.dano * 2.5)
            i.vida -= dano_critico
            mensagem = Comentarios.mensagem_dano_critico(self,dano_critico, i.nome)
            luta.log_batalha(mensagem)
            h.inventario.remove('Estamina')

        elif menu == 5 and h.inventario.count('Barra de proteína') >= 1:
            luta.especial()
            h.inventario.remove('Barra de proteína')

        elif menu == 6 and h.inventario.count('Granada de mão') >=1:
            inventario.granada_de_mao(i.vida)
            h.inventario.remove('Granada de mão')

        elif menu == 7 and h.inventario.count('Granada de luz') >=1:
            inventario.granada_luz() 
            h.inventario.remove('Granada de luz')

        elif menu == 8 and h.inventario.count('Carregador estendido') >=1:
            dano_extra = (h.dano *1.5)
            i.vida -= dano_extra
            print(f'{Cores.AMARELO} Dano extra aplicado\nDano: {dano_extra}{Cores.RESET}') 



            h.inventario.remove('Carregador estendido') 
            
        else:
            print('Você não possui este consumivel')     
        #except:  print('Escolha uma opção válida')
    
    def save(self):
        h = self.personagem_escolhido

        if h.inventario.count('Fita de tinta'):
            print(f'Fitas de tinta: {h.inventario.count('Fita de tinta') - 1}')
            data_agora = datetime.now()
            s.salvar_progresso(self, h.__dict__,h.inventario, data_agora)
            print('Salvo com Sucesso')
        else:
            print(f'Fitas de tinta: {h.inventario.count('Fita de tinta')}')
            print('Você não possui nenhuma fita para salvar')
    
    def carregar_save(self):
        h = self.personagem_escolhido
        conn = s.criar_conexao()
        cursor = conn.cursor()
        cursor.execute(f"""
SELECT id_saves, nome, data FROM  tabelaSaves;
""")
        save = cursor.fetchall()
        for i in save:
            id_personagem = i[0]
            nome = i[1]
            data = i[2]
            print(f'SAVE: {id_personagem} | PERSONAGEM: {nome} | DATA: {data}')
        escolha = input('Escolha teu save')
        conn.commit()

        cursor.execute(f"""    
SELECT nome,arma,dano,vida,vidaMaxima,especial,nivel,experiencia 
FROM tabelaSaves 
WHERE id_saves = {escolha};
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
            print('Save carregado')
            conn.commit()
            
        cursor.execute(f"""
SELECT nomeItem,quantidade 
FROM tabelaInventario WHERE saves = {id_personagem};
""")    

        inventario = cursor.fetchall()
        for i in inventario:
            h.inventario.extend([i[0]] * (i[1]))
        conn.commit()
        conn.close()

    def luta(self):
            luta = Luta()

            save = int(input('''
    ┌──────────────┐   ┌───────────────┐
    │ [1] NEW GAME │   │ [2] CONTINUE  │
    └──────────────┘   └───────────────┘
    ''')) 
            os.system('cls')
            if save == 1:
                luta.escolher_personagem()
            elif save == 2:
                luta.carregar_save()
                

            luta.escolher_inimigo()
            contador_kills = []
            
            while True:
                opcoes = int(input('''
    ┌────────────┐   ┌──────────┐    
    │ [1] ATACAR │   │ [2] ITEM │   
    └────────────┘   └──────────┘    
    '''))
                if opcoes == 1:
                    os.system('cls')
                    critico = random.randint(1,20) 
                    especial = random.randint(1,20)          
                    time.sleep(0.5)
                    if especial > 15:
                        luta.especial()
                    luta.ataque_inimigo()
                    luta.log_batalha(luta.ataque_heroi())
                if self.inimigo_escolhido.vida <= 0:
                    os.system('cls')
                    print(f'''
{Cores.AZUL_CLARO}____________________________________________________{Cores.RESET}
{Cores.VERDE}Você Ganhou! 👌{Cores.RESET}
{Cores.AZUL_CLARO}____________________________________________________{Cores.RESET}
''')
                    contador_kills.append(Herois.contador_kills(self.inimigo_escolhido.tipo))
                    
                    Luta.drop(Luta)
                    Herois.ganhar_experiencia(self.personagem_escolhido,self.inimigo_escolhido.nivel,self.inimigo_escolhido.tipo)
                    Herois.subir_level(self.personagem_escolhido)
                    Herois.exibir_status(self.personagem_escolhido)

                    opcoes_save = int(input('''
    ┌───────────────┐   ┌────────────┐    
    │ [1] CONTINUAR │   │ [2] SALVAR │   
    └───────────────┘   └────────────┘    
    '''))
                    os.system('cls')
                    if opcoes_save == 1:
                        pass
                    elif opcoes_save == 2:
                        Luta.save(self)
                        pass

                    luta.escolher_inimigo()           
                if self.personagem_escolhido.vida <= 0:
                    Herois.tela_de_morte(self.personagem_escolhido,contador_kills)          
                    luta.escolher_personagem()
                elif opcoes == 2:
                    luta.usar_consumivel()  
        #except Exception as e: print(f'Esse é o Erro: {e}')
        


    nemesis = Inimigo('Nemesis','Lança míssil', 25,150 , 150 ,'boss', 0)
    mr_x = Inimigo('Mister X','Soco', 30,140, 140,'boss' , 0)
    #-
    personagem_escolhido = Herois('a','a',0,0,0,'a', 0, 0)
    inimigo_escolhido = Inimigo('a','a',0,0, 0,'a',0)

def main():
    luta = Luta()
    luta.luta()
if __name__ == '__main__':
    main()