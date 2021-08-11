import sqlite3 
# https://www.sqlitetutorial.net/sqlite-sample-database verileri buradan aldik

cnn = sqlite3.connect("chinook.db")

cursor = cnn.execute("select FirstName from customers where city ='London' ")

for row in cursor:
    print("First Name: " + row[0])


komut2 = cnn.execute("""select  
                    FirstName, City from customers where city = 'Paris'""")

for row in komut2:
    print(row[0] + " from " + row[1])


komut3 = cnn.execute("""Select city , count(*) from Customers 
                    group by city order by city desc""")

for row in komut3:
    print("City: " + row[0])
    print("Count: " + str(row[1]))
    print("***********")

komut4 = cnn.execute("""Select city, count(*) from Customers
                        group by city order by count(*) desc""")

for row in komut4:
    print("City: " + row[0])
    print("count: " + str(row[1]))
    print("----------")

komut5 = cnn.execute("""Select city, count(*) from Customers
                        group by city having count(*)>1 
                        """)

for row in komut5:
    print("city: " + row[0])
    print("count: " + str(row[1]))
    print("*-*-*-*-*-*-*-*-*")

komut6 = cnn.execute("""select Firstname, email from Customers
                        where email like '%apple%' """) #hem basinda hem sonunda % isareti istedi, normalde sadece basina ekleniyordu


for row in komut6:
    print("ismi: " + row[0] + " applefan boy maili: " + row[1])
    print("apple apple apple")


komut7 = cnn.execute("""select firstname, country, email from Customers
                        where email like '%yahoo%' order by country""")

for row in komut7:
    print(row[1] + " memleketli " + row[0] + " oldboy mail hesabi: " + row[2])
    print(":) :) :) :) :) :) :) :) :) :)")
    
cnn.close()

