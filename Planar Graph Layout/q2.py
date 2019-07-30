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

print(deg)