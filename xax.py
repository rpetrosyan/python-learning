import random

gaxtni = random.randint(1,100)

porcer=0
while True:
    tiv = int(input("gri tiv 1-100"))
    porcer = porcer + 1
    if tiv == gaxtni:
        print("Gushakecir!")
        print(porcer)
        break
    elif gaxtni - tiv > 10:
        print("shat qich e")
    elif gaxtni > tiv:
        print("qich e")
    elif tiv - gaxtni <=10:
        print("shat e")
    else:
        print("shat shat e")

