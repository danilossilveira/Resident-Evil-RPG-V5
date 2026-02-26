# ⚔️ Game de Luta - Resident Evil

Um jogo interativo de luta em turnos baseado no universo de Resident Evil, para trenar lógica e orientação a objeto

## 🎮 Características

- **3 Personagens Jogáveis:**
  - **Leon Kennedy** - Equipado com Pistola (Dano: 15, Vida: 140)
    - Habilidade especial: Desvia de ataques
  - **Chris Redfield** - Equipado com Sub-metralhadora (Dano: 17, Vida: 135)
    - Habilidade especial: Chance de crítico aumentada
  - **Ethan** - Equipado com Shotgun (Dano: 12, Vida: 170)
    - Habilidade especial: Regenera vida

- **Sistema de Combate Dinâmico:**
  - Ataques normais e críticos
  - Sistema de vida com regeneração/dano
  - Chance de crítico baseada no personagem

- **Inimigos:**
  - **Nemesis** - Equipado com Lança míssil (Dano: 25, Vida: 150)

- **Interface Colorida:**
  - Mensagens de ataque em cores diferentes
  - Feedback visual para ações (crítico, vitória, derrota)
  - Sistema de cores ANSI para melhor experiência

## 📁 Estrutura do Projeto

```
├── personagem.py      # Classe Personagem (classe mãe)
├── herois.py          # Classe Herois (herda de Personagem)
├── inimigo.py         # Classe Inimigo (herda de Personagem)
├── luta.py            # Classe Luta e lógica do jogo
├── cores.py           # Definição de cores ANSI
└── README.md          # Este arquivo
```

## 🎯 Mecânicas do Jogo

### Sistema de Ataque
- Cada ataque tem chance de ser crítico
- Ataque crítico causa 1.5x de dano
- Leon tem 25% de chance de crítico (e pode esquivar)
- Chris tem 32% de chance de crítico (maior chance que os outros)
- Ethan tem 25% de chance de crítico (mas regenera vida)

### Habilidades Especiais
- **Leon**: A cada turno, pode desviar de ataques
- **Chris**: Chance aumentada de crítico
- **Ethan**: Regenera 5 de vida aleatoriamente durante os combates

### Vitória e Derrota
- ✅ **Vitória**: Reduza a vida do inimigo a 0 ou menos
- ❌ **Derrota**: Sua vida cair para 0 ou menos


## 💡 Dicas de Gameplay

1. **Ethan** é o personagem mais resistente (170 vida)
2. **Chris** tem o maior dano base (17)
3. **Leon** é equilibrado e pode esquivar ataques


## 🤝 Contribuições

Sinta-se livre para melhorar o projeto! Alguns melhoramentos possíveis:
- Adicionar mais personagens e inimigos
- Criar múltiplas fases/níveis
- Sistema de itens e powerups
- Salvar pontuação
- Melhorar a interface gráfica

---

