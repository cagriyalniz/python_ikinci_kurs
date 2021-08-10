#

def krktrBul(cumle1):
    x = 0
    syc_tr = 0
    list1 = cumle1
    for i in list1:
        if i == "ç":
            syc_tr = syc_tr + 1
        if i == "ğ":
            syc_tr = syc_tr + 1
        if i == "I":
            syc_tr = syc_tr + 1
        if i == "ö":
            syc_tr = syc_tr + 1
        if i == "ü":
            syc_tr = syc_tr + 1
        if i == "ş":
            syc_tr = syc_tr + 1        
        x = x + 1    
    donus = print(cumle1 + "\n bu cumlede {} adet turkce karakter mevcut".center(60).format(syc_tr))
    return donus

krktrBul("Sabahın sesi kulaklarımda Biri pencereyi açmış yine Ekşi, yorgun bir tat ağzımda")





    