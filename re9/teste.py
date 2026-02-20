
itens = ["a", "b", "a", "c", "b", "a"]
contagens = {}

for item in itens:
    contagens[item] = contagens.get(item, 0) + 1

print(contagens)  # {'a': 3, 'b': 2, 'c': 1}
