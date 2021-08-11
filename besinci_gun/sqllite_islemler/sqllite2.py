import sqlite3

cnn = sqlite3.connect("chinook.db")

komut1 = cnn.execute("select firstname from customers where firstname like '%i%' ")
my_list = list()

for row in komut1:
    print(row[0])
    
    my_list.append(row[0])

print(my_list)

komut2 = cnn.execute("""select firstname, city from customers 
                        where city like '%london%' """)

sayac = 0
londonNameList = list()
londonCityList = list()
for row in komut2:
    #print(str(row[0]) + " " + str(row[1]))
    londonNameList.append(row[0])
    londonCityList.append(row[1])

# londonTxtAppe = open("FromLondon1.txt", "a")
# londonTxtAppe.write(str(londonNameList))
# londonTxtAppe.write(str(londonCityList))
# londonTxtAppe.close()

komut3 = cnn.execute("""select firstname, city from customers 
                        where city like '%paris%' """)
londonTxtAppe2 = open("FromLondon2.txt", "a")
londonNameList2 = list()
londonCityList2 = list()

for row in komut3:
    print(row[0] + row[1])
    londonNameList2.append(row[0])
    londonCityList2.append(row[1])

print(londonCityList2)
print(len(londonCityList2))

listlistlistlistbzzzzzweneedanotherthing = list()
l = len(londonCityList2)
k = 0
for row in range(len(londonNameList2)):
    listlistlistlistbzzzzzweneedanotherthing.append(londonNameList2[k] + " " + londonCityList2[k])
    k = k + 1

print(listlistlistlistbzzzzzweneedanotherthing[0])

londonTxtAppe2.write(str(listlistlistlistbzzzzzweneedanotherthing))

londonTxtAppe2.close()


cnn.close()