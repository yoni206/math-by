# from cvc5.pythonic import *
from z3 import *
import sys
from pprint import pprint

def print_model(model,n,k,x):
    for i in range(k):
        for j in range(n):
            print("x[" + str(i) + "][" + str(j) + "]: " + str(model[x[i][j]]))
assert(len(sys.argv)) == 3
n = int(sys.argv[1])
k = int(sys.argv[2])

x = {}

for i in range(k):
    if i not in x:
        x[i] = {}
    for j in range(n):
        # x[i][j] is the jth coordinate of the ith sphere
        x[i][j] = Real("x" + str(i) + "," + str(j))

s = Solver()

# s.set("nl-cov", "true")

s.add(x[0][0] == 1)
for j in range(1,n):
    s.add(x[0][j] == 0)

s.add(x[1][0] == 1/2)
s.add(x[1][1] == Sqrt(3)/2)
for j in range(2,n):
    s.add(x[1][j] == 0)

for i in range(k):
    dist = 0
    for j in range(n):
        dist += x[i][j]**2
    s.add(dist == 1)

for i in range(k):
    for j in range(i+1, k):
        dot_product = 0
        for l in range(n):
            dot_product += x[i][l]*x[j][l]
        s.add(dot_product <= 1/2)

if s.check() == sat:
    print_model(s.model(),n,k,x)
else:
    print(s.check())
