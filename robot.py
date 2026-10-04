import random

texy=0

while True:
    qayl = random.randint(0,1)
    if qayl == 0:
        texy = texy - 1
    else:
        texy = texy + 1
    if texy < 0:
        texy = 0
    print(texy)
    if texy == 4:
        print("Gandzy gtav!")
        break


