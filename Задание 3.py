
import networkx as nx
# Создаем граф
G = nx.Graph()
G.add_edges_from([(1, 3), (2, 3), (1, 4), (4, 6), (5, 6), (5, 7)])  # Пример графа с "ямой" и "горбиком"
# Вычисляем меру центральности в собственных векторах
eigenvector_centrality = nx.eigenvector_centrality(G)
# Выводим центральность для семи узлов
for node in G.nodes:
    print(f"Узел {node}: {eigenvector_centrality[node]:.4f}")