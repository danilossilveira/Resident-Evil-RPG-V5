import sqlite3
import traceback
class Save():
    
    def criar_conexao():
        conn = sqlite3.connect('personagens_save.db')
        return conn
    
    def criar_tabela_herois():
        try:
        
            conn = Save.criar_conexao()
            cursor = conn.cursor()
            cursor.execute("""
    CREATE TABLE IF NOT EXISTS tabelaHerois (
    id VARCHAR(2) PRIMARY KEY NOT NULL,
    nome VARCHAR(20) NOT NULL,
    arma VARCHAR(20)NOT NULL,
    dano FLOAT NOT NULL,
    vidaMaxima INTEGER NOT NULL,
    vida FLOAT NOT NULL,
    especial VARCHAR(50) NOT NULL,
    nivel INTEGER NOT NULL,
    experiencia INTEGER NOT NULL
    );""")
            conn.commit()
            cursor.execute(       
    """INSERT INTO tabelaHerois (id, nome, arma, dano, vidaMaxima, vida, especial, nivel, experiencia)
    VALUES(1,'Leon', 'Pistola',15,150,150, 'Desvia de ataques', 0, 0),
        (2,'Chirs', 'Sub-metralhadora',17 ,135,135, 'Chance de crítico aumenta', 0, 0),
        (3,'Ethan', 'Shotgun',12,170, 170,'Regenera vida', 0, 0),
        (4,'Ada Wong', 'Balestra' ,14 ,145 ,145,'Dano multiplicado', 0, 0),
        (5,'Hunk', 'Metralhadora', 16,150, 150, 'Chance de dar um hit kill', 0, 0),
        (6,'Jill Valentine', 'Assalto', 14,150, 150, 'Quanto menos vida, mais dano', 0, 0),
        (7,'Wesker', 'Katana', 19, 180,180, 'Ataque triplicado', 0, 0);
    """)
            conn.commit()
            conn.close()
        except Exception:
            traceback.print_exc()

    def criar_tabela_inventario():
        conn = Save.criar_conexao()
        cursor = conn.cursor()
        try:
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS tabelaInventario (
        nomeItem VARCHAR(30) NOT NULL
        );""")
            conn.commit()
            conn.close()
        except Exception:
            traceback.print_exc()
    def drop_item(self, item):
        conn = Save.criar_conexao()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
        INSERT INTO tabelaInventario(nomeItem)
        VALUES('{item}')
        """)
            conn.commit()
            conn.close()
        except Exception:
            traceback.print_exc()
                
    def remover_item(self,item):
        conn = Save.criar_conexao()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
        DELETE FROM tabelaInventario WHERE nomeItem = ?
        """,(item,))
            conn.commit()
            conn.close()
        except Exception:
            traceback.print_exc()            

    def criar_tabela_saves():
        conn = Save.criar_conexao()
        cursor = conn.cursor()
        try:
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS tabelaSaves (
        id_saves INTEGER PRIMARY KEY NOT NULL,
        nome VARCHAR(20) NOT NULL ,
        arma VARCHAR(20) NOT NULL,
        dano FLOAT NOT NULL,
        vidaMaxima INTEGER NOT NULL,
        vida FLOAT NOT NULL,
        especial VARCHAR(50) NOT NULL,
        nivel INTEGER NOT NULL,
        experiencia INTEGER NOT NULL,
        data VARCHAR(50) NOT NULL
        );""")
            conn.commit()
            conn.close()
        except Exception:
            traceback.print_exc()



    def salvar_progresso(self,nome, arma,dano,vida,vidaMaxima,especial,nivel,experiencia,data ):
        conn = Save.criar_conexao()
        cursor = conn.cursor()
        try:    
            cursor.execute(f"""
    INSERT INTO tabelaSaves(
        nome,
        arma,
        dano,
        vidaMaxima,
        vida,
        especial,
        nivel,
        experiencia,
        data)
    VALUES(?,?,?,?,?,?,?,?,?);
    """,(nome, arma,dano,vidaMaxima,vida,especial,nivel,experiencia,data))
            conn.commit()
            conn.close()
        except Exception:
            conn = Save.criar_conexao()
            traceback.print_exc()
            pass
            
    def salvar_personagem(self, nome,vida, nivel,dano,xp):
        try:
            conn = Save.criar_conexao()
            cursor = conn.cursor()
            cursor.execute(f"""
    UPDATE tabelaPersonagem SET vida = '{vida}', nivel = '{nivel}', dano = '{dano}', xp = '{xp}' 
    WHERE nome = '{nome}';
    """)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception:
            traceback.print_exc()
    






















































    def criar_tabela_inventario000():
        conn = Save.criar_conexao()
        cursor = conn.cursor()
        try:
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS tabelaInventario (
        id_inventario INTEGER PRIMARY KEY NOT NULL,
        nomeItem VARCHAR(30) NOT NULL,
        quantidade INTEGER NOT NULL, 
        saves INTEGER NOT NULL,
        FOREIGN KEY (saves) REFERENCES tabelaPersonagem (id_saves)                      
        );""")
            conn.commit()
            conn.close()
        except Exception:
            traceback.print_exc()