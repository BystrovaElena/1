
import networkx as nx
# Создаем граф
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 1), (1, 4), (3, 5)])
# Вычисляем меру центральности в собственных векторах
eigenvector_centrality = nx.eigenvector_centrality(G)
# Выводим центральность для семи узлов с точностью до 2 знаков после запятой
for n in G.nodes:
    print("Узел " + str(n) + ": {:.2f}".format(eigenvector_centrality[n]))