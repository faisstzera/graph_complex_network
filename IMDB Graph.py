import csv
import sys
from string import capwords
from Grafo import Grafo

sys.setrecursionlimit(100000)

filename = 'netflix_amazon_disney_titles.csv'

# Grafo 1: Direcionado de Diretores para Atores
grafo_atores_diretores = Grafo(direcionado=True, ponderado=True)
# Grafo 2: Não direcionado entre Atores
grafo_atores = Grafo(direcionado=False, ponderado=True)

with open(filename, 'r') as csv_file:
    datareader = csv.reader(csv_file)
    next(datareader)
    count = 1
    for row in datareader:
        print('Row number', count)
        count += 1

        diretores = row[3].split(",")
        atores = row[4].split(",")

        if not diretores[0] or not atores[0]:
            print("Diretor ou ator não encontrado")
            continue

        diretores_formatados = [capwords(diretor.strip()) for diretor in diretores]
        atores_formatados = [capwords(ator.strip()) for ator in atores]

        # Construir grafo número 1 (atores -> diretores)
        for diretor in diretores_formatados:
            grafo_atores_diretores.adiciona_vertice(diretor)
            for ator in atores_formatados:
                grafo_atores_diretores.adiciona_vertice(ator)
                grafo_atores_diretores.adiciona_aresta(ator, diretor, 1)

        # Construir grafo número 2 (atores -> atores) evitando duplicações
        for i, ator in enumerate(atores_formatados):
            grafo_atores.adiciona_vertice(ator)
            for j in range(i + 1, len(atores_formatados)):
                outro_ator = atores_formatados[j]
                grafo_atores.adiciona_vertice(outro_ator)
                grafo_atores.adiciona_aresta(ator, outro_ator, 1)

# ----------------------------------------------------------------------------------------
# EXERCÍCIO 1: Informações sobre os grafos
print("Número de vértices do grafo 1 (atores -> diretores):", grafo_atores_diretores.get_ordem())
print("Número de arestas do grafo 1 (atores -> diretores):", grafo_atores_diretores.get_tamanho())
print("Número de vértices do grafo 2 (atores -> atores):", grafo_atores.get_ordem())
print("Número de arestas do grafo 2 (atores -> atores):", grafo_atores.get_tamanho())

# ----------------------------------------------------------------------------------------
# EXERCÍCIO 2: Encontrar componentes conectados e fortemente conectados

# Encontrar componentes conectados no grafo de atores
componentes_conectados_atores = grafo_atores.find_connected_components()
print("Número de componentes conectados no grafo de atores:", len(componentes_conectados_atores))

# Encontrar componentes fortemente conectados no grafo de diretores usando algoritmo de Kosaraju
componentes_conectados_diretores = grafo_atores_diretores.kosaraju()
print("Número de componentes fortemente conectados no grafo de diretores:", len(componentes_conectados_diretores))

# Opcional: salvar componentes fortemente conectados em um arquivo
grafo_atores_diretores.salva_componentes_em_arquivo("componentes_fortemente_conectados_diretores.txt", componentes_conectados_diretores)
grafo_atores.salva_componentes_em_arquivo("componentes_conectados_atores.txt", componentes_conectados_atores)


# ----------------------------------------------------------------------------------------
# Exercício 3: Gerar a Minimum Spanning Tree a partir de um vértice específico
minimum_spanning_tree = grafo_atores_diretores.prim_algorithm("Tom Hanks")

print("Árvore geradora mínima:", minimum_spanning_tree)