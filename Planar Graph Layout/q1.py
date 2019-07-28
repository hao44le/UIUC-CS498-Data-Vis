import numpy as np
edges = [[0,1],[0,2],[1,3],[2,4],[3,5],[4,5],
         [0,6],[1,9],[2,10],[2,14],[3,13],[3,17],[4,18],[5,21],
         [6,7],[6,10],[7,8],[8,9],[9,13],
         [10,11],[11,12],[11,15],[12,13],[12,16],
         [14,15],[14,18],[15,16],[16,17],[17,21],
         [18,19],[19,20],[20,21]]

n = 22

x = np.array(np.zeros(n))
y = np.array(np.zeros(n))

# https://math.stackexchange.com/questions/206659/dividing-circle-into-six-equal-parts-and-know-the-coordinates-of-each-diving-poi/270816

for x_index in range(n):
    # x = 1 * cos(2 * x_index * pi / k) + 1 - 1
    x[x_index] = np.cos(2 * x_index * np.pi / n)
for y_index in range(n):
    # y = 1 * sin(2 * y_index * pi / k) + 0
    y[y_index] = np.sin(2 * y_index * np.pi / n)
print(x)
print(y)