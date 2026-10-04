import random

uxex = {}
for i in range(5):
    uxex[i] = [0.0, 0.0]

def voroshel(g):
    if random.random() < 0.3:
        return random.randint(0, 1)
    elif g[0] > g[1]:
        return 0
    else:
        return 1

for porc in range(100):
    texy = 0
    qayler = 0
    while texy < 4:
        hin = texy
        gorc = voroshel(uxex[hin])
        if gorc == 0:
            texy = texy - 1
        else:
            texy = texy + 1
        if texy < 0:
            texy = 0
        qayler = qayler + 1
        if texy == 4:
            varj = 1.0
        else:
            varj = max(uxex[texy]) * 0.9
        uxex[hin][gorc] = uxex[hin][gorc] + 0.5 * (varj - uxex[hin][gorc])
    if porc % 10 == 0:
        print(porc, qayler)

print(uxex)
