# edges[] has already been defined to the edge list as before
# n already set to 22, the number of vertices
# deg[i] already set to the degree of vertex i
import numpy as np
edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 5],
         [0, 6], [1, 9], [2, 10], [2, 14], [3, 13], [3, 17], [4, 18], [5, 21],
         [6, 7], [6, 10], [7, 8], [8, 9], [9, 13],
         [10, 11], [11, 12], [11, 15], [12, 13], [12, 16],
         [14, 15], [14, 18], [15, 16], [16, 17], [17, 21],
         [18, 19], [19, 20], [20, 21]]

n = 22

deg = np.array(np.zeros(n, dtype=int))

# insert code here to compute
# the degree of vertex i and
# store it in deg[i]

for edge in edges:
    deg[edge[0]] += 1
    deg[edge[1]] += 1
A = np.array(np.zeros((n, n)))

# Insert code here to fill
# the nxn matrix A with
# the Laplacian matrix for
# the graph represented by
# the edge-list in array edges
fast_edge_lookup = dict()
for row in edges:
    (ver_1, ver_2) = row[0], row[1]
    if ver_1 in fast_edge_lookup:
        fast_edge_lookup[ver_1].add(ver_2)
    else:
        fast_edge_lookup[ver_1] = set()
        fast_edge_lookup[ver_1].add(ver_2)

    if ver_2 in fast_edge_lookup:
        fast_edge_lookup[ver_2].add(ver_1)
    else:
        fast_edge_lookup[ver_2] = set()
        fast_edge_lookup[ver_2].add(ver_1)

for x_index in range(n):
    for y_index in range(n):
        value = 1
        if x_index == y_index:
            value = 1
        elif y_index in fast_edge_lookup[x_index]:
            value = -1 / deg[x_index]
        else:
            value = 0
        A[x_index][y_index] = value

print(A)

