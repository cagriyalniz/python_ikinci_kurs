sayilar1 = [1 , 2, 3, 4, 4, 5, 54, 42, 73, 65]
sayilar2 = list(filter(lambda s: s%2 == 0, sayilar1))
print("ilk listedeki cift sayilar: " + str(sayilar2))
