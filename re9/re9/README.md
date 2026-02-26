# ⚔️ Resident Evil - Game de Luta em Turnos

Um jogo interativo de luta em turnos imersivo, baseado no universo de Resident Evil, desenvolvido para treinar conceitos de Lógica de Programação e Orientação a Objeto com Python.

## 🎮 Características Principais

### Personagens Jogáveis
O jogo oferece 7 personagens únicos do universo de Resident Evil, cada um com habilidades e características distintas:
- **Leon Kennedy** - Agente equilibrado com habilidade de esquiva
- **Chris Redfield** - Soldado com alta taxa de crítico
- **Ethan Winters** - Sobrevivente resistente com regeneração de vida
- **Ada Wong** - Agente versátil
- **Hunk** - Soldado mercenário
- **Jill Valentine** - Agente especializada
- **Wesker** - Antagonista com poderes especiais

### Sistema de Combate Dinâmico
- **Ataques com críticos**: Cada ataque possui chance de causar dano crítico (1.5x de dano)
- **Sistema de vida progressivo**: Vida máxima aumenta com nivelamento
- **Dano baseado em probabilidade**: Variação de dano entre ataques
- **Habilidades especiais por personagem**: Cada herói tem uma habilidade única

### Sistema de Itemização
- **Erva Verde**: Recupera 30 de vida
- **Erva Amarela**: Recupera 35 de vida e aumenta vida máxima em 35
- **Spray Médico**: Recupera 60 de vida
- **Granada de Mão**: Causa 70 de dano ao inimigo
- **Granada de Luz**: Atordoa o inimigo, permitindo fuga ou novo ataque

### Sistema de Personagem
- **Experiência e Nivelamento**: Ganhe XP ao derrotar inimigos (100 XP para normais, 200 para bosses)
- **Progressão**: Aumente seu nível até 10 e melhore atributos
- **Inventário**: Colete e utilize itens durante as lutas
- **Salvamento**: Salve seu progresso em banco de dados SQLite

### Interface
- **Sistema de cores ANSI**: Feedback visual com cores diferentes para ações
- **Navegação intuitiva**: Uso de teclado (W/S e ENTER) para seleções
- **Efeitos visuais**: Animações e efeitos sonoros (em Windows)
- **Mensagens contextualizadas**: Descrições detalhadas de cada ação

## 📁 Estrutura do Projeto

```
├── personagem.py           # Classe abstrata Personagem (classe mãe)
├── herois.py               # Classe Herois (herda de Personagem) com sistema de XP
├── inimigo.py              # Classe Inimigo (herda de Personagem)
├── luta.py                 # Lógica principal do sistema de combate
├── inventario.py           # Sistema de itens e consumíveis
├── cores.py                # Definições de cores ANSI
├── comentarios.py          # Mensagens e diálogos
├── tabelas.py              # Dados dos personagens e inimigos
├── personagem_save.py      # Sistema de salvamento em banco de dados
├── teste.py                # Testes e utilitários
├── sons/                   # Arquivos de áudio
├── __pycache__/            # Cache de compilação Python
└── README.md               # Este arquivo
```

## 🎯 Mecânicas de Jogo

### Sistema de Ataque
- Cada ataque tem percentual de chance de ser crítico
- Ataque normal: 1x de dano
- Ataque crítico: 1.5x de dano
- Dano varia aleatoriamente entre ataques

### Habilidades Especiais por Personagem
- **Leon Kennedy**: Pode esquivar de ataques
- **Chris Redfield**: Chance de crítico aumentada (32%)
- **Ethan Winters**: Regenera vida aleatoriamente durante combates
- Outros personagens possuem habilidades únicas específicas

### Sistema de Experiência
- **Derrota inimigos normais**: +100 XP × nível do inimigo
- **Derrota bosses**: +200 XP × nível do inimigo
- **Progressão de nível**: Aumente atributos a cada novo nível
  - Dano aumenta 30% por nível
  - Vida máxima aumenta 50% por nível
- **Nível máximo**: 10

### Vitória e Derrota
- ✅ **Vitória**: Reduza a vida do inimigo a 0 ou menos
- ❌ **Derrota**: Sua vida for reduzida a 0 ou menos
- **Fuga**: Use itens especiais para escapar de lutas

## 🎮 Como Jogar

1. **Iniciar o jogo**: Execute o arquivo principal
2. **Escolher personagem**: Navegue com W/S e selecione com ENTER
3. **Escolher inimigo**: Selecione qual inimigo enfrentar
4. **Combater**: 
   - Ataque normal
   - Use itens do inventário
   - Utilize habilidades especiais
5. **Ganhar experiência**: Derrote inimigos para evoluir seu personagem
6. **Salvar progresso**: Guarde seu avanço no banco de dados

## 💡 Dicas de Gameplay

1. **Ethan** é o personagem mais resistente (170 vida inicial) - ideal para iniciantes
2. **Chris** possui o maior dano base (17 de dano) - melhor para ataque agressivo
3. **Leon** é o mais equilibrado e pode esquivar - bom para jogadores experientes
4. **Gerencie itens**: Use recuperadores de vida estrategicamente
5. **Nível importa**: Personagens de nível maior ganham estatísticas significativas

## 🛠️ Requisitos

- **Python 3.7+**
- **SQLite3** (geralmente incluído com Python)
- **Windows** (recomendado, para efeitos sonoros e entrada de teclado)

## 🚀 Como Executar

```bash
python luta.py
```

## 📚 Conceitos de Programação Aplicados

- **Herança**: Hierarquia de classes com Personagem, Herois e Inimigo
- **Polimorfismo**: Implementação de `tela_de_morte()` em diferentes classes
- **Abstrações**: Classe abstrata `Personagem` com métodos abstratos
- **Encapsulamento**: Atributos privados e métodos de acesso
- **Persistência**: Salvamento de dados em SQLite
- **Lógica de Probabilidade**: Sistema de críticos e chance
- **Manipulação de Strings e I/O**: Interface interativa com o usuário

## 🤝 Melhorias Futuras

- [ ] Adicionar mais personagens e inimigos bosses
- [ ] Criar sistema de múltiplas fases/campanha
- [ ] Implementar modo multiplayer local
- [ ] Melhorar gráficos com biblioteca de UI
- [ ] Adicionar efeitos sonoros mais elaborados
- [ ] Criar ranking de jogadores
- [ ] Sistema de achievements/conquistas
- [ ] Modo survival com ondas de inimigos

---

**Desenvolvido como projeto educacional de Python e Orientação a Objeto**
