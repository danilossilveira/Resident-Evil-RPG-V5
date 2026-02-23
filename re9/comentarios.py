import random
from cores import Cores
class Comentarios():
    def mensagem_inimigo_proximo(self, inimigo,arma, nivel):
        falas = [
            f"O {inimigo} (nivel {nivel}) está se aproximando com um(a) {arma}.",
            f"Você avistou o {inimigo} (nivel {nivel}) à sua frente.",
            f"O {inimigo} (nivel {nivel}) surge empunhando um(a) {arma}.",
            f"Um {inimigo} (nivel {nivel}) bloqueia seu caminho.",
            f"O {inimigo} (nivel {nivel}) corre em sua direção com um(a) {arma}."
        ]
        return (random.choice(falas))

    def mensage_ataque_inimigo(self, inimigo,):
        falas = [
            f"O {inimigo} avançou contra você.",
            f"O {inimigo} tenta te acertar.",
            f"O {inimigo} desfere um golpe em você.",
            f"O {inimigo} inicia um ataque feroz.",
            f"O {inimigo} investe rapidamente contra você.",
            f"O {inimigo} te acerta com um golpe violento.",
            f"O {inimigo} te atinge de surpresa.",
            f"O {inimigo} lança um ataque direto contra você.",
            f"O {inimigo} tenta te derrubar com um golpe."

        ]
        return (random.choice(falas))
    def mensagem_ataque_heroi(self, inimigo, arma):
        falas = [
            f"Você acerta um golpe no {inimigo}.",
            f"Você golpeou o {inimigo}.",
            f"Seu ataque atinge o {inimigo}."
            f"Você atacou o {inimigo} com seu(sua) {arma}.",
            f"Seu(sua) {arma} acerta o {inimigo}.",
            f"Você golpeia o {inimigo} usando o(a) {arma}.",
            f"Você desfere um ataque com o(a) {arma} no {inimigo}."
    ]
        return (random.choice(falas)) 
    
    def mensagem_dano_critico(self,dano, inimigo):
        falas = [            
        f"{Cores.VERMELHO}CRÍTICO! Você causou {dano} de dano no {inimigo}!{Cores.RESET}",
        f"{Cores.VERMELHO}CRÍTICO! {inimigo} recebeu {dano} de dano!{Cores.RESET}",
        f"{Cores.VERMELHO}CRÍTICO! Seu golpe causa {dano} de dano — o {inimigo} cambaleia!{Cores.RESET}",
        f"{Cores.VERMELHO}CRÍTICO! {dano} de dano! O {inimigo} é atingido brutalmente!{Cores.RESET}",
        f"{Cores.VERMELHO}CRÍTICO! Você acerta em cheio e causa {dano} de dano no {inimigo}!{Cores.RESET}",
        ]
        return (random.choice(falas))


