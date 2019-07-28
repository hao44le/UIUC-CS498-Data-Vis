# Insert code here to
# set the first six rows
# of A to the first six
# rows of an identity
# matrix
for x in range(6):
  for y in range(6):
    if x == y: A[x][y] = 1
    else: A[x][y] = 0


bx = np.array(np.zeros(n))

# set the first six
# elements of bx to the
# desired x coordinates
# of the first six vertices


bx[0] = -1
bx[1] = 1
bx[2] = -1
bx[3] = 1
bx[4] = -1
bx[5] = 1

for x in range(6,n): bx[x] = 0

x = np.linalg.solve(A,bx)

by = np.array(np.zeros(n))

# set the first six
# elements of by to the
# desired y coordinates
# of the first six vertices

by[0] = -1
by[1] = -1
by[2] = 0
by[3] = 0
by[4] = 1
by[5] = 1

for a in range(6,n): by[a] = 0

y = np.linalg.solve(A,by)

drawgraph(x,y,edges)