# thx https://www.youtube.com/watch?v=rxMKCvqBRys

with open("notlar.txt", "r") as f:
    with open("gecenler.txt", "w") as g: #dosya olmadigi zaman kendisi oto olusacak
        with open("kalanlar.txt", "w") as k:
            icerik = f.readlines() 
            m = 0 
            for satir in icerik:
                if m == 0: #ilk satiri okumayip atlamak iciin
                    m+=1
                    continue
                satir = satir.replace("\n", "") #\n leri kaldirmak icin
                bosluk_sayisi = 0
                bosluk_indexleri = []
                index = 0
                for karakter in satir: #satirdaki bosluklarin sayisini ve bosluklarin kacinci indexte oldugunu bulmak icin
                    if karakter == " ":
                        bosluk_sayisi += 1
                        bosluk_indexleri.append(index)
                    index +=1
                
                ad_soyad = satir[:bosluk_indexleri[0]] #en bastan ilk bosluga kadar olan kismi al
                soyad = ad_soyad.split("-")[-1] #ad soyadı - lara gore bol ve en sonrakini al. soyadlari almak icin
                ad = ad_soyad[:ad_soyad.index(soyad)-1].replace("-", " ") #ad ı alırken - yi almamak icin -1 yazıldı. iki isimliler icin replace yapildi

                notlar = satir.split(" ")[-1]
                notlar2 = notlar.split("/")
                birinci_vize = int(notlar2[0])
                ikinci_vize = int(notlar2[1])
                final = int(notlar2[2])
                ort = birinci_vize*0.3 + ikinci_vize*0.3 + final*0.4

                bolum = satir[bosluk_indexleri[0] + 1: bosluk_indexleri[len(bosluk_indexleri)-1]] # +1 bosluğu eklemesin diye, -1 out of range olmamak icin

                if ort >= 70:
                    g.write(ad)
                    g.write(" " *(25 - len(ad))) #ad yazdırıldıktan sonra 25 e tamamlayacak kadar bosluk birakilacak
                    g.write(soyad)
                    g.write(" "*(25 - len(soyad)))
                    g.write(bolum)
                    g.write(" "*(25 - len(bolum)))
                    g.write(str(round(ort, 1))) # ortalamaları virgulden sonra 1 basamak yazdırmak icin
                    g.write(" "*21)
                    g.write("GECTI")
                    g.write("\n")
                else:
                    k.write(ad)
                    k.write(" "*(25 - len(ad))) #ad yazdırıldıktan sonra 25 e tamamlayacak kadar bosluk birakilacak
                    k.write(soyad)
                    k.write(" "*(25 - len(soyad)))
                    k.write(bolum)
                    k.write(" "*(25 - len(bolum)))
                    k.write(str(round(ort, 1))) # ortalamaları virgulden sonra 1 basamak yazdırmak icin
                    k.write(" "*21)
                    k.write("KALDI")
                    k.write("\n")
