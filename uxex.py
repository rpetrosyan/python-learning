uxex = {}

for i in range(5):
    uxex[i] = [0.0, 0.0]

print(uxex)
def netrl(g):
    if g[0] > g[1]:
        return 0
    else:
        return 1

print(netrl(uxex[0]))
import random
def voroshel(g):
    if random.random() < 0.3:
        return random.randint(0, 1)
    else:
        return netrl(g)

print(voroshel(uxex[0]))
