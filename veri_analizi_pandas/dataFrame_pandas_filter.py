import pandas as pd

# filter/group
filmler = pd.read_csv("imdb-1000.csv")
#print(filmler)
print(filmler["title"].head(8))
print(filmler[["title", "star_rating"]].head(8))

print(filmler[['title', 'star_rating']][filmler['star_rating'] > 9])
print(filmler[(filmler['star_rating'] > 8) & (filmler['star_rating'] < 8.5)])
print(filmler[['title', 'star_rating']] [(filmler['star_rating'] > 8.7) & (filmler['star_rating'] < 9)])

print(filmler[(filmler['star_rating'] > 8) & (filmler['star_rating'] < 8.2)][['title', 'star_rating']])

print(filmler.query('star_rating > 8.4')[['title', 'genre', 'star_rating']]) #query adamdır

print("tum filmlerin ort derecesi: " + str(filmler.star_rating.mean()))
print(filmler.groupby('genre').star_rating.mean())

print("***********************-------**********")



def CsvToTxt(): #txt dosyasi içine cok intizamli yazdi
    mTxtA =open ("movies.txt", "a")
    moviesCvs = pd.read_csv("imdb-1000.csv")
    moviesQuery = moviesCvs.query('star_rating >8.7')[['title', 'star_rating']]
    moviesCvsDf = pd.DataFrame(moviesQuery)    
    mTxtA.write(str(moviesCvsDf))
    
    mTxtA.close()

#CsvToTxt()