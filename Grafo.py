import numpy as np
import json
import matplotlib.pyplot as mtplot

class Grafo:
  def __init__(self, direcionado:bool, ponderado: bool):
    self.ordem = 0
    self.tamanho = 0
    self.lista_adjacencia = {}
    self.direcionado = direcionado
    self.ponderado = ponderado
    self.time = 0

  def adiciona_vertice(self, label: str):
    if self.existe_vertice(label) is None:
      self.lista_adjacencia[label] = []
      self.ordem += 1
    # else:
    #   print("Vértica já existente!")

  def adiciona_aresta(self, u, v, peso=1):
      # Adiciona os vértices não existentes
      if self.existe_vertice(u) is None:
          self.adiciona_vertice(u)
      if self.existe_vertice(v) is None:
          self.adiciona_vertice(v)

      # Verifica se a aresta já existe
      if self.tem_aresta(u, v):
          for i in range(len(self.lista_adjacencia[u])):
              if self.lista_adjacencia[u][i][0] == v:
                  self.lista_adjacencia[u][i] = (v, self.lista_adjacencia[u][i][1] + peso)
                  break

          if not self.direcionado:
              for j in range(len(self.lista_adjacencia[v])):
                  if self.lista_adjacencia[v][j][0] == u:
                      self.lista_adjacencia[v][j] = (u, self.lista_adjacencia[v][j][1] + peso)
                      break
      else:
          # Se a aresta não existir, adiciona a aresta
          self.tamanho += 1
          self.lista_adjacencia[u].append((v, peso))

          if not self.direcionado:
              self.lista_adjacencia[v].append((u, peso))

  def existe_vertice(self, label):
    return self.lista_adjacencia.get(label)

  def remove_aresta(self,u,v):
    # Primeiramente, buscar a chave do 'u' no dicionário
    # Depois, buscar o índice vértice ao qual ele está ligado dentro da lista de tuplas
    # Finalmente, remover a tupla indicada da lista de acordo com o índice encontrado
    # Complexidade O(n) -> tem como fazer mais rápido aqui ou somente em outra estrutura?

    if self.direcionado is True:
      for i in range(len(self.lista_adjacencia[u])):
        if self.lista_adjacencia[u][i][0] == v:
          self.lista_adjacencia[u].pop(i)
          break

    else:

      for i in range(len(self.lista_adjacencia[u])):
        if self.lista_adjacencia[u][i][0] == v:
          self.lista_adjacencia[u].pop(i)
          break

      for i in range(len(self.lista_adjacencia[v])):
        if self.lista_adjacencia[v][i][0] == u:
          self.lista_adjacencia[v].pop(i)
          break

  def remove_vertice(self, u):

    self.lista_adjacencia.pop(u)

  def remove_vertice_completo(self, u):
    # Primeiramente, remove o vértice da lista de adjacência
    # Depois, itera sobre todos os outros vértices na lista de adjacência
    # Cria uma nova lista sem nenhuma aresta que vá em direção à u

      if u in self.lista_adjacencia:
          self.lista_adjacencia.pop(u)

      for key in list(self.lista_adjacencia.keys()):
          self.lista_adjacencia[key] = [edge for edge in self.lista_adjacencia[key] if edge[0] != u]

  def tem_aresta(self,u,v):

    for i in range(len(self.lista_adjacencia[u])):
      if self.lista_adjacencia[u][i][0] == v:
        return True

    return False

  def grau_entrada(self, u):

    if self.direcionado is False:
      return None

    count = 0
    key_list = list(self.lista_adjacencia.keys())
    key_list.remove(u)

    for key in key_list:
      for i in range(len(self.lista_adjacencia[key])):
        if self.lista_adjacencia[key][i][0]==u:
          count += 1

    return count

  def grau_saida(self, u):

    if self.direcionado is False:
      return None

    return len(self.lista_adjacencia[u])

  def grau(self,u):

    if self.direcionado is False:
      return len(self.lista_adjacencia[u])
    else:
      return self.grau_entrada(u) + self.grau_saida(u)

  def get_peso(self,u,v):

    if self.tem_aresta(u,v):

      for i in range(len(self.lista_adjacencia[u])):
        if self.lista_adjacencia[u][i][0] == v:
          return self.lista_adjacencia[u][i][1]


  def desenha_grafo(self):
    for label in self.lista_adjacencia:
      print(label, "->", self.lista_adjacencia[label])

  def get_prox_node(self, custo, visited):
      custo_min = np.inf
      prox_node = None
      for node in custo:
          if node not in visited and custo[node][0] < custo_min:
              custo_min = custo[node][0]
              prox_node = node
      return prox_node

  def dijkstra(self, source_node, destination_node):
    visited = []  
    custo = {node: [np.inf, None] for node in self.lista_adjacencia}  
    custo[source_node][0] = 0
    node_atual = source_node

    while destination_node not in visited:
        nodes_adjacentes = self.lista_adjacencia[node_atual]
        for adj, peso_aresta in nodes_adjacentes:
            if adj not in visited:
                new_custo = custo[node_atual][0] + peso_aresta
                if new_custo < custo[adj][0]:
                    custo[adj][0] = new_custo
                    custo[adj][1] = node_atual

        visited.append(node_atual)
        node_atual = self.get_prox_node(custo, visited)

        if node_atual is None:
            break  

    # Reconstruir o caminho mais curto a partir do nó de destino
    shortest_path = []
    step = destination_node
    while step is not None:
        shortest_path.append(step)
        step = custo[step][1]
    shortest_path.reverse() 

    return (custo[destination_node][0], shortest_path)
  
  def dijkstra_distancia_maxima(self, source_node, dist_maxima):
    # Dijkstra modificado para parar quando a distância máxima for atingida, e registrar todos os nodes que foram atingidos até aquela distância
    visited = []
    custo = {node: [np.inf, None] for node in self.lista_adjacencia}
    custo[source_node][0] = 0
    node_atual = source_node
    accumulated_custos = {source_node: 0}

    while node_atual is not None and accumulated_custos[node_atual] <= dist_maxima:
        adjacent_nodes = self.lista_adjacencia[node_atual]
        for adj, peso_aresta in adjacent_nodes:
            new_custo = custo[node_atual][0] + peso_aresta
            if new_custo < custo[adj][0]:
                custo[adj][0] = new_custo
                custo[adj][1] = node_atual
                accumulated_custos[adj] = new_custo

        visited.append(node_atual)
        node_atual = self.get_prox_node(custo, visited)

    # percorre a lista dos custos acumulados para encontrar os vértices que estão dentro da distância máxima
    vertices_limite_distancia = []
    for node in accumulated_custos:
        if node != source_node and accumulated_custos[node] <= dist_maxima:
            vertices_limite_distancia.append(node)

    return vertices_limite_distancia
  
  def top_20_saida(self):
    # cRIAR uma lista de tuplas com list comprehension (vertice, grau de saída)
    graus_saida = [(vertice, self.grau_saida(vertice)) for vertice in self.lista_adjacencia.keys()]
    graus_saida.sort(key=lambda x: x[1], reverse=True)
    return graus_saida[:20]

  def top_20_entrada(self):
    graus_entrada = [(vertice, self.grau_entrada(vertice)) for vertice in self.lista_adjacencia.keys()]
    graus_entrada.sort(key=lambda x: x[1], reverse=True)
    return graus_entrada[:20]
  
  def get_ordem(self):
    return self.ordem
  
  def get_tamanho(self):
    return self.tamanho
  
  def save_to_file(self, filename):
    with open(filename, 'w') as f:
        json.dump(self.lista_adjacencia, f)

  def dfs(self, node, visited):
      visited.add(node)
      for adjacente in self.lista_adjacencia[node]:
          if adjacente[0] not in visited:
              self.dfs(adjacente[0], visited)

  def conexo(self):
      # verifica se o grafo é conectado usando DFS
      visited = set()
      start = next(iter(self.lista_adjacencia))
      self.dfs(start, visited)
      return len(visited) == len(self.lista_adjacencia)

  def fortemente_conectado(self):
      # Verifica se o grafo direcionado é fortemente conectado
      for u in self.lista_adjacencia:
          for v in self.lista_adjacencia:
              if not self.existe_caminho(u, v) or not self.existe_caminho(v, u):
                  return False

      return True
  
  def bfs(self, start_node, target_node):
      # bfs para encontrar um caminho entre dois vértices, retorna se é possível ou não chegar de um node ao outro
      visited = set()
      queue = [start_node]
      visited.add(start_node)

      while queue:
          node_atual = queue.pop(0)

          if node_atual == target_node:
              return True, visited 

          for adjacente, peso in self.lista_adjacencia[node_atual]:
              if adjacente not in visited:
                  visited.add(adjacente)
                  queue.append(adjacente)

      return False, visited 
  

# ----------------------------------------------------------------------------------------------------------

# EXERCÍCIO NÚMERO 2

# Aqui está a implementação do algoritmo de Kosaraju para encontrar componentes fortemente conectados em um grafo direcionado
# Caso o grafo não seja direcionado, o algoritmo de Kosaraju não pode ser aplicado, e a função count_strongly_connected_components() lança um erro
# A função count_connected_components() é usada para encontrar componentes conectados em grafos não direcionados

  def dfs_time(self, node, visited, tempos):
      """ DFS que armazena os tempos de início e término de visitação. """
      visited.add(node)
      # incrementa o tempo de visitação
      self.time += 1
      # marca o tempo inicial de visitação de cada vértice
      tempos[node]['start_time'] = self.time

      for adjacente, _ in self.lista_adjacencia[node]:
          if adjacente not in visited:
              self.dfs_time(adjacente, visited, tempos)  # Chamada correta da função dfs_time

      self.time += 1
      # marca o tempo de término de visitação de cada vértice
      tempos[node]['finish_time'] = self.time


  def executa_dfs(self):
      visited = set()
      tempos = {node: {'start_time': None, 'finish_time': None} for node in self.lista_adjacencia}

      # Executa DFS para todos os vértices não visitados (para garantir que todos os componentes sejam cobertos)
      for node in self.lista_adjacencia:
          if node not in visited:
              self.dfs_time(node, visited, tempos)

      return tempos  # Retorna o dicionário com tempos de início e término
  
  def grafo_transposto(self):
      transposto = Grafo(direcionado=True, ponderado=self.ponderado)
      
      for vertice in self.lista_adjacencia:
          transposto.adiciona_vertice(vertice)
      for u in self.lista_adjacencia:
          for (v, peso) in self.lista_adjacencia[u]:
              transposto.adiciona_aresta(v, u, peso)
      
      return transposto
  
  def kosaraju(self):
      if not self.direcionado:
          raise("O algoritmo de Kosaraju só pode ser aplicado em grafos direcionados. Redirecionando para a função de contagem de elementos conectados.")

      # Passo 1: Executa DFS no grafo original e coleta tempos de término
      tempos = self.executa_dfs()

      # Ordena os nós pelos tempos de término em ordem decrescente
      ordem = sorted(self.lista_adjacencia, key=lambda node: tempos[node]['finish_time'], reverse=True)

      # Passo 2: Cria o grafo transposto
      transposto = self.grafo_transposto()

      # Passo 3: Executa DFS no grafo transposto na ordem decrescente dos tempos de término
      visited = set()
      componentes = []

      for node in ordem:
          if node not in visited:
              componente = []
              self.dfs_transposto(transposto, node, visited, componente)
              componentes.append(componente)

      return componentes

  
  def dfs_transposto(self, grafo, node, visited, componente):
    # Função auxiliar para DFS no grafo transposto
    visited.add(node)
    componente.append(node)
    for adjacente, _ in grafo.lista_adjacencia[node]:
        if adjacente not in visited:
            self.dfs_transposto(grafo, adjacente, visited, componente)

  # As duas funções abaixos são chamadas para grafos não direcionados que não podem usar o algoritmo de Kosaraju

  def find_connected_components(self):
      visited = set()
      componentes = []

      for node in self.lista_adjacencia:
          if node not in visited:
              componente = []
              self.dfs_collect(node, visited, componente)
              componentes.append(componente)

      return componentes

  def dfs_collect(self, node, visited, componente):
      """ DFS modificada para coletar os vértices do componente conectado. """
      visited.add(node)
      componente.append(node)
      for adjacente in self.lista_adjacencia[node]:
          if adjacente[0] not in visited:
              self.dfs_collect(adjacente[0], visited, componente)

  # Salvar componentes em um .txt para verificação
  def salva_componentes_em_arquivo(self, nome_arquivo, componentes):
    with open(nome_arquivo, 'w') as arquivo:
        for componente in componentes:
            arquivo.write("Componentes fortemente conectados:\n")
            arquivo.write(", ".join(map(str, componente)) + "\n")
            arquivo.write("-----------\n")

###################################################################################

# EXERCÍCIO 3: Algoritmo de Primm

  def dijkstra_primm(self, source_node, destination_node):
    visited = []  
    custo = {node: [np.inf, None] for node in self.lista_adjacencia}  
    custo[source_node][0] = 0
    node_atual = source_node

    while destination_node not in visited:
        nodes_adjacentes = self.lista_adjacencia[node_atual]
        for adj, peso_aresta in nodes_adjacentes:
            if adj not in visited:
                new_custo = custo[node_atual][0] + peso_aresta
                if new_custo < custo[adj][0]:
                    custo[adj][0] = new_custo
                    custo[adj][1] = node_atual

        visited.append(node_atual)
        node_atual = self.get_prox_node(custo, visited)

        if node_atual is None:
            break  

    # Reconstruir o caminho mais curto a partir do nó de destino
    shortest_path = []
    step = destination_node
    while step is not None:
        shortest_path.append(step)
        step = custo[step][1]
    shortest_path.reverse() 

    return (custo[destination_node][0], shortest_path)
  

  # Acho que por ter implementado o algoritmo de Dijkstra anteriormente, o desenvolvimento dessa função foi relativamente simples
  # As diferenças entre as funções de dijkstra e do algoritmo de Primm é que ao invés de fazer um while até o destination node o while é feito até que todos os vértices sejam visitados
  # E a construção do caminho mais curto é feita de forma diferente, pois ao invés de considerar o custo acumulado dos nodes visitados, utilizamos apenas os custos das arestas locais
  # Movi o algoritmo de dijkstra em cima desse para fins de comparação
  def prim_algorithm(self, start_node):
      visited = []  
      custo = {node: [np.inf, None] for node in self.lista_adjacencia}  
      custo[start_node][0] = 0
      node_atual = start_node

      while len(visited) < len(self.lista_adjacencia): 
          nodes_adjacentes = self.lista_adjacencia[node_atual]
          for adj, peso_aresta in nodes_adjacentes:
              if adj not in visited:
                  if peso_aresta < custo[adj][0]:  # Aqui ao invés de comparar o custo acumulado comparamos o custo da aresta
                      custo[adj][0] = peso_aresta
                      custo[adj][1] = node_atual

          visited.append(node_atual)
          node_atual = self.get_prox_node(custo, visited)

          if node_atual is None:
              break  

      # Para construir a árvore geradora mínima também é mais simples do que Dijkstra
      # Precisamos apenas percorrermos o dicionário de custos e adicionar as arestas que possuem custo mínimo
      mst_edges = []
      for node in custo:
          if custo[node][1] is not None:
              mst_edges.append((custo[node][1], node, custo[node][0]))

      return mst_edges

# ----------------------------------------------------------------------------------------------------------
      
# EXERCÍCIO NÚMERO 4

  def centralidade_grau(self):
    centralidade = {}

    # usar para não ficar uma grande quantia de tempo
    # vertices = list(self.lista_adjacencia.keys())[:1000]
    # for vertice in vertices:
      
    for vertice in self.lista_adjacencia:
        if self.direcionado:
            grau_entrada = self.grau_entrada(vertice)
            grau_saida = self.grau_saida(vertice)
            centralidade[vertice] = grau_saida + grau_entrada
        else:
            centralidade[vertice] = self.grau(vertice)

    return centralidade

  def plot_histograma_graus(self, maxNum):
    graus = [self.grau(vertice) for idx, vertice in enumerate(self.lista_adjacencia) if idx < maxNum]
    mtplot.hist(graus, bins=range(min(graus), max(graus) + 4), edgecolor='black', align='left', color='red')
    mtplot.title('Distribuição de Graus dos Vértices')
    mtplot.xlabel('Grau')
    mtplot.ylabel('Número de Vértices')
    mtplot.show()
    
# EXERCÍCIO NÚMERO 5
  def plot_top_10_centralidade_grau(self):
    centralidade = self.centralidade_grau()
    
    # x[1] pois queremos o valor e não a key, [:10] pega os 10 primeiros pois está em ordem decrescente
    top_10 = sorted(centralidade.items(), key=lambda x: x[1], reverse=True)[:10]
    vertices, graus = zip(*top_10)

    mtplot.figure(figsize=(10, 6))
    mtplot.bar(vertices, graus, color='red')
    mtplot.title('Top-10 Vértices por Centralidade de Grau')
    mtplot.xlabel('Vértices')
    mtplot.ylabel('Centralidade de Grau')
    mtplot.show()


# ----------------------------------------------------------------------------------------------------------

# EXERCÍCIO NÚMERO 6
  
  def centralidade_intermediacao(self):
    centralidade = dict.fromkeys(self.lista_adjacencia.keys(), 0.0)
    for s in self.lista_adjacencia:
        pilha = []
        predecessores = {w: [] for w in self.lista_adjacencia}
        sigma = dict.fromkeys(self.lista_adjacencia, 0.0)
        sigma[s] = 1.0
        distancia = dict.fromkeys(self.lista_adjacencia, -1)
        distancia[s] = 0
        fila = [s]
        while fila:
            v = fila.pop(0)
            pilha.append(v)
            for w, peso in self.lista_adjacencia[v]:
                if distancia[w] < 0:
                    fila.append(w)
                    distancia[w] = distancia[v] + 1
                if distancia[w] == distancia[v] + 1:
                    sigma[w] += sigma[v]
                    predecessores[w].append(v)
        delta = dict.fromkeys(self.lista_adjacencia, 0)
        while pilha:
            w = pilha.pop()
            for v in predecessores[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1 + delta[w])
            if w != s:
                centralidade[w] += delta[w]
    return centralidade

  def plot_top_10_centralidade_intermediacao(self):
          centralidade = self.centralidade_intermediacao()
          top_10 = sorted(centralidade.items(), key=lambda x: x[1], reverse=True)[:10]
          vertices, valores = zip(*top_10)
          mtplot.figure(figsize=(10, 6))
          mtplot.bar(vertices, valores, color='blue')
          mtplot.title('Top-10 Vértices por Centralidade de Intermediação')
          mtplot.xlabel('Vértices')
          mtplot.ylabel('Centralidade de Intermediação')
          mtplot.xticks(rotation=45, ha='right')
          mtplot.show()
    
# ----------------------------------------------------------------------------------------------------------

# EXERCÍCIO NÚMERO 7
  def centralidade_proximidade(self, vertice):
        distancias, _ = self.bfs_distancias(vertice)
        soma_distancias = 0
        alcancaveis = 0

        for dist in distancias.values():
            if dist != np.inf and dist != 0:
                soma_distancias += dist
                alcancaveis += 1

        if alcancaveis > 0:
            if self.direcionado:
                N = len(distancias)
                soma_inversa_distancias = 0
                for dist in distancias.values():
                    if dist != np.inf and dist != 0:
                        soma_inversa_distancias += 1 / dist
                return soma_inversa_distancias / (N - 1)
            else:
                return (alcancaveis-1) / soma_distancias
        else:
            return 0

  def top_10_centralidade_proximidade(self):
    centralidades = {}
    maiores_valores = []
    for vertice in self.lista_adjacencia.keys():
      centralidade = self.centralidade_proximidade(vertice)
      centralidades[vertice] = centralidade
    for vertice, centralidade in centralidades.items():
      if len(maiores_valores) < 10:
        maiores_valores.append((vertice, centralidade))
      else:
        menor_valor = min(maiores_valores, key=lambda x: x[1])
        if centralidade > menor_valor[1]:
          maiores_valores.remove(menor_valor)
          maiores_valores.append((vertice, centralidade))

        maiores_valores = sorted(centralidades.items(), key=lambda x: x[1], reverse=True)[:10]
        return maiores_valores
  
  def plotar_top_10_centralidade(self, top_10=None):
        if top_10 is None:
            top_10 = self.top_10_centralidade_proximidade()
        
        # Extrair nomes e centralidades
        nomes = [x[0] for x in top_10]
        centralidades = [x[1] for x in top_10]
        
        # Criar o gráfico de barras invertido
        plt.figure(figsize=(8, 10))  # Ajuste o tamanho conforme necessário
        bars = plt.bar(nomes, centralidades, color='skyblue')
        
        # Ajustar o layout e rótulos
        plt.ylabel('Centralidade de Proximidade')
        plt.title('Top 10 Centralidade de Proximidade')
        plt.xticks(rotation=90)  # Rotacionar os nomes dos vértices para melhor visualização
        
        
        # Adicionar rótulos individuais para cada barra
        for bar in bars:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), round(bar.get_height(), 2), 
                     ha='center', va='bottom', fontsize=8)
        
        plt.tight_layout()  # Ajustar layout para evitar cortes de rótulos
        plt.show()

  def tipo_vertice(self, vertice):
        """
        Identifica se o vértice é um diretor ou um ator.
        Retorna "diretor" se o vértice é um diretor,
        "ator" se é um ator, ou "indefinido" se não é possível determinar.
        """
        if self.direcionado:
            tem_entrada = any(vertice in [adj[0] for adj in self.lista_adjacencia[node]] for node in self.lista_adjacencia)
            tem_saida = len(self.lista_adjacencia[vertice]) > 0

            if tem_entrada and not tem_saida:
                return "diretor"
            elif not tem_entrada and tem_saida:
                return "ator"
            elif tem_entrada and tem_saida:
                return "indefinido"
            else:
                return "indefinido"
        else:
            return "indefinido"
        
  def top_10_centralidade_diretores(self):
        centralidades = {}
        maiores_valores = []
        for vertice in self.lista_adjacencia.keys():
            if self.tipo_vertice(vertice) == "diretor":
                centralidade = self.centralidade_proximidade(vertice)
                centralidades[vertice] = centralidade
        for vertice, centralidade in centralidades.items():
              if len(maiores_valores) < 10:
                maiores_valores.append((vertice, centralidade))
              else:
                menor_valor = min(maiores_valores, key=lambda x: x[1])
                if centralidade > menor_valor[1]:
                  maiores_valores.remove(menor_valor)
                  maiores_valores.append((vertice, centralidade))

                maiores_valores = sorted(centralidades.items(), key=lambda x: x[1], reverse=True)[:10]
                return maiores_valores







