i = 0
tplm = 0
while i<=10:
    tplm = tplm + i
    i = i + 1
    if i == 4:
        continue
    print(i)    #i leri yaz fakat 4 olursa 4u gecip yazmaya devam et
    if tplm > 30:
        break   #tplm 30dan buyuk olursa donguyu kir

print(tplm)


