from abc import ABC,abstractmethod

class Personagem(ABC):
    def __init__(self,nome,equipamento,dano,vida,nivel):
        self.nome = nome
        self.equipamento = equipamento
        self.dano = dano
        self.vida = int(vida)
        self.nivel = nivel

    @abstractmethod
    def tela_de_morte(self):
        pass
    
