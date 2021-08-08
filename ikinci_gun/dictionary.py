my_dict = {"isim": "cagri",
            "soyisim": "yalniz",
            "numara": 345}

print(my_dict)
my_dict["isim"] = "akif"
my_dict["soyisim"] = "şakir"
print(my_dict)

my_dict2 = dict(a = "apple", b = "samsung")
print(my_dict2)
del(my_dict2["a"])
print(my_dict2)