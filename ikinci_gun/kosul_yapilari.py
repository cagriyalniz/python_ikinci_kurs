
light = ["red", "yellow", "green"]

i = int(input("0-2 arasi bir sayi secin"))
print(i)
print(light[i])

def traffic_lamb(light, i):
    if i == 0:
        print("yanan isik " + light[i] + " bekleyiniz")
    elif i == 1:
        print("yanan isik " + light[i] + " hazirlanin")
    else:
        print("yanan isik " + light[i] + " geciniz")

traffic_lamb(light, i)