def ntrel(g):
    if g[0] > g[1] and g[0] > g[2]:
        return 0
    elif g[1] > g[2]:
        return 1
    else:
        return 2
print(ntrel([0.42, 0.51, 0.87]))
print(ntrel([0.90, 0.30, 0.10]))
print(ntrel([0.20, 0.70, 0.40]))
