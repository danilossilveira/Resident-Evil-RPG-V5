
import sqlite3
from personagem_save import Save as s


class Teste():
    
    def escolher_personagem(self): 
        conn = sqlite3.connect('personagens_save.db')
        cursor = conn.cursor()
        print(cursor.fetchall())
        for i in cursor:
            print(i)


        #for i in
        #if escolha not in personagens:








def main():
    Teste.escolher_personagem(Teste)
if __name__ == '__main__':
    main()
