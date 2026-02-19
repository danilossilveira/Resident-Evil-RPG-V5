import sqlite3
import traceback
class Save():
    
    def criar_conexao():
        conn = sqlite3.connect('personagens_save.db')
        return conn
    
    def criar_tabela():
        try:
        
            conn = Save.criar_conexao()
            cursor = conn.cursor()
            cursor.execute("""
    CREATE TABLE IF NOT EXISTS tabelaHerois (
    id VARCHAR(2) PRIMARY KEY,
    nome VARCHAR(20) ,
    arma VARCHAR(20),
    dano FLOAT,
    vidaMaxima INTEGER,
    vida FLOAT,
    especial VARCHAR(50),
    nivel INTEGER,
    experiencia INTEGER
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



    def criar_tabelas():
        conn = Save.criar_conexao()
        cursor = conn.cursor()
        try:
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS tabelaSaves (
        id_saves INTEGER PRIMARY KEY,
        nome VARCHAR(20) ,
        arma VARCHAR(20),
        dano FLOAT,
        vidaMaxima INTEGER,
        vida FLOAT,
        especial VARCHAR(50),
        nivel INTEGER,
        experiencia INTEGER,
        data DATE
        );""")
            conn.commit()
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS tabelaInventario (
        id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeItem VARCHAR(30),
        quantidade INTEGER, 
        saves INTEGER,
        FOREIGN KEY (saves) REFERENCES tabelaPersonagem (id_saves)                      
        );""")
        
            conn.commit()
            cursor.close()
            conn.close()
            
        except Exception:
            traceback.print_exc()

    def salvar_progresso(self,nome, arma,dano,vidaMaxima,vida,especial,nivel,experiencia,data ):
        try:    
            conn = Save.criar_conexao()
            cursor = conn.cursor()

            cursor.execute(f"""
    INSERT INTO tabelaSaves(nome,
        arma,
        dano,
        vidaMaxima,
        vida,
        especial,
        nivel,
        experiencia,
        data)
    VALUES('{nome}','{arma}',{dano},{vidaMaxima},{vida},'{especial}',{nivel},{experiencia},'{data}')
    """)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception:
            traceback.print_exc()
            
    def salvar_personagem(self, nome,vida, nivel,dano,xp):
        try:
            conn = Save.criar_conexao()
            cursor = conn.cursor()
            cursor.execute(f"""
    UPDATE tabelaPersonagem SET vida = '{vida}', nivel = '{nivel}', dano = '{dano}', xp = '{xp}' 
    WHERE nome = '{nome}'
    """)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception:
            traceback.print_exc()
    
        