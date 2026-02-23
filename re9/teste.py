import msvcrt
import os

def menu_inventario():
    itens = ["Faca de Combate", "Pistola 9mm", "Erva Verde", "Munição", "Sair"]
    index = 0

    while True:
        # O segredo para não piscar: usar o código ANSI para voltar ao topo
        print("\033[H", end="") 
        
        print("╔════════════════════════════════════╗")
        print("║      MALETA DE EQUIPAMENTOS        ║")
        print("╠════════════════════════════════════╣")
        
        for i, item in enumerate(itens):
            if i == index:
                # Usamos cores ANSI (opcional) para dar o destaque "Premium"
                print(f"║  \033[1;33m▶ [ {item.ljust(20)} ]\033[0m      ║") 
            else:
                print(f"║    {item.ljust(24)}        ║")
                
        print("╚════════════════════════════════════╝")
        print(" [W/S] Navegar  |  [ENTER] Selecionar")

        # Captura a tecla sem precisar de Enter
        tecla = msvcrt.getch().lower()

        # O msvcrt retorna 'bytes', por isso usamos b'w'
        if tecla == b'w':
            index = (index - 1) % len(itens)
        elif tecla == b's':
            index = (index + 1) % len(itens)
        elif tecla == b'\r':  # \r é o código para a tecla ENTER
            if itens[index] == "Sair":
                break
            print(f"\n Selecionado: {itens[index]} ".center(40, "-"))
            msvcrt.getch() # Pausa para ver o resultado
if __name__ == '__main__':
    menu_inventario()            