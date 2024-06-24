import itertools

def gerar_combinacoes_fechadas(numeros_impares, numeros_pares, max_combinacoes=100):
    todas_combinacoes = []
    count = 0
    for comb_impares in itertools.combinations(numeros_impares, 4):
        for comb_pares in itertools.combinations(numeros_pares, 4):
            todas_combinacoes.append(list(comb_impares) + list(comb_pares))
            count += 1
            if count >= max_combinacoes:
                return todas_combinacoes
    return todas_combinacoes

# Números disponíveis para o sorteio
numeros_impares = [1, 3, 5, 11, 13, 15, 21, 23, 25]
numeros_pares = [2, 4, 12, 14, 22, 24]

# Gerar combinações fechadas
comb_fechadas = gerar_combinacoes_fechadas(numeros_impares, numeros_pares)

# Mostrar as combinações geradas
print("Total de combinações fechadas:", len(comb_fechadas))
for i, comb in enumerate(comb_fechadas, 1):
    print(f"Combinação {i}: {comb}")
