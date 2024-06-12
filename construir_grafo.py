import csv
import sys
from string import capwords
from Grafo import Grafo

sys.setrecursionlimit(100000)

filename = 'netflix_amazon_disney_titles.csv'

grafo_atores_diretores = Grafo(direcionado=True, ponderado=True)
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
                grafo_atores_diretores.adiciona_aresta(diretor, ator)

        # Construir grafo número 2 (atores -> atores) evitando duplicações
        for i, ator in enumerate(atores_formatados):
            grafo_atores.adiciona_vertice(ator)
            for j in range(i + 1, len(atores_formatados)):
                outro_ator = atores_formatados[j]
                grafo_atores.adiciona_vertice(outro_ator)
                grafo_atores.adiciona_aresta(ator, outro_ator)

print("Número de vértices do grafo 1:", grafo_atores.get_ordem())
print("Número de arestas do grafo 1:", grafo_atores.get_tamanho())

# print("Número de vértices do grafo 2:", grafo_atores.get_ordem())
# print("Número de arestas do grafo 2:", grafo_atores.get_tamanho())

print("Joan Cusack:", grafo_atores.lista_adjacencia["Joan Cusack"])

componentes_conectados = grafo_atores.count_strongly_connected_components()
print("Número de componentes fortemente conectados:", componentes_conectados)
# dfs_2 = grafo_atores.executa_dfs()

# grafo_atores_diretores.salva_componentes_em_arquivo("componentes_fortemente_conectados.txt", componentes_conectados)