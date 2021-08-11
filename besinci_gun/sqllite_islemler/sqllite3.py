import sqlite3

cnn = sqlite3.connect("chinook.db")

komut1 = cnn.execute("select AlbumId, Title, ArtistId from albums")

list1 = list()
list2 = list()
list3 = list()
list4 = list()

for row in komut1:
    print(row[0], row[1], row[2])
    list1.append(row[0])
    list2.append(row[1])
    list3.append(row[2])

k = 0
for k in range(len(list1)):
    list4.append(str(list1[k]) + " " + list2[k] + " " + str(list3[k]))
    k = k + 1

print("**************")
t = 0
for t in range(len(list4)):
    print(list4[t])
    t = t + 1

albumTextAppe3 = open("Album.txt", "a")
x = "AlbumId".ljust(5)
y = "Title".center(5)
z = "ArtistId".rjust(5)
albumTextAppe3.write("{0} {1} {2} \n".format(x, y, z))
a = 0
for a in range(len(list4)):
    albumTextAppe3.write(str(list4[a]).ljust(5))
    albumTextAppe3.write("\n")
    a = a + 1


albumTextAppe3.close()
    

