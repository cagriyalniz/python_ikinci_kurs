# https://jsonplaceholder.typicode.com/

import json

with open("kisiler.js") as kisiler:
    data = json.load(kisiler)
    print(data[0])
    print(data[0]["address"]["street"])

    k =0
    for i in data[k]:
        print(i)

    print("*************")
    i = 0
    while i < 6:
        print(str(data[i]["id"]) + " " + str(data[i]["name"])) #bu yazim sekli ne kadar dogru bilmiyorum fakat istedigim sonucu aldim
        i = i + 1

    print("---------------")

    for i in range(len(data)):
        print(data[i]["name"])



    

    