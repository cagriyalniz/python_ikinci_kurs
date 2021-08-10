
#%%
def Hastaekleme():
    try:
        fHastaAp = open("hasta.txt", "a") # "w" ile yapildigi zaman uzerine yaziyor, "a" ile yapildigi zaman ekleme yapiyor append
    
        hastalist = ["veli", "tolgay", "serdar", "gökhan", "ali", "olga"]

        for i in hastalist:
            fHastaAp.write("\n")
            fHastaAp.writelines(i)
        
           
    finally:
        fHastaAp.close()

def Hastaokuma():
    try:
        fHastaRe = open("hasta.txt", "r")
        print(fHastaRe.read(1))

        for i in fHastaRe:
            print(i)
        
        
    
    finally:
        fHastaRe.close()

#Hastaekleme()
Hastaokuma()


#%%
# print("deneme")
# listem = ["ali", "veli", "ayşe"]
# for i in listem:
#     print(i)

# %%
