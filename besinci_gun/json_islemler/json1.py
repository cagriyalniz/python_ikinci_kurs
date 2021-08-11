import json

data = '{"name" : "cagri" , "surname" : "yalniz"}'

y = json.loads(data)

print(y["name"])
print(y["surname"])

musteri = {
            "firstname" : "cagri",
            "email" : "cagri@python.com"
        }

musteriJson = json.dumps(musteri)
print(musteriJson)
print(type(musteriJson))

print(json.dumps("cagri"))
