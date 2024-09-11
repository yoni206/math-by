# from cvc5.pythonic import *
from z3 import *

from pprint import pprint

def abs(x):
  return If(x<0, -x, x)

k = 10

x = {}
y = {}

for i in range(k):
    x[i] = Real("x" + str(i))
    y[i] = Real("y" + str(i))

s = Solver()

#s.add(x[0] ** 2 == 2)
#if s.check() == sat:
#  print(s.model())
#exit()


# s.set("nl-cov", "true")

for i in range(k):
  # s.add(x[i]**2 + y[i]**2 == 2)
  s.add(x[i]**2 + y[i]**2 == 1)


for i in range(k):
  for j in range(i+1, k):
    # s.add((x[i] - x[j])**2 + (y[i]-y[j])**2 >= 2)
    s.add(x[i]*x[j] + y[i]*y[j] <= 1/2)


if s.check() == sat:
  for k in s.model():
    print(str(k) + ": " + str(s.model()[k]))
else:
  print("unsat")
