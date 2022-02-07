import requests
import secrets
import sqlite3
from typing import Tuple


f = open("data.txt", "w")


def setup_db(cursor:sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS table250(
    show_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    full_title TEXT NOT NULL,
    year TEXT NOT NULL,
    crew TEXT NOT NULL,
    imdb_rating TEXT NOT NULL,
    rating_count TEXT NOT NULL
    );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS ratings(
    show_id TEXT NOT NULL,
    total_rating TEXT NOT NULL,
    total_rating_votes TEXT NOT NULL,
    rating10percentage TEXT NOT NULL,
    ratingVotes10 TEXT NOT NULL,
    rating9percentage TEXT NOT NULL,
    ratingVotes9 TEXT NOT NULL,
    rating8percentage TEXT NOT NULL,
    ratingVotes8 TEXT NOT NULL,
    rating7percentage TEXT NOT NULL,
    ratingVotes7 TEXT NOT NULL,
    rating6percentage TEXT NOT NULL,
    ratingVotes6 TEXT NOT NULL,
    rating5percentage TEXT NOT NULL,
    ratingVotes5 TEXT NOT NULL,
    rating4percentage TEXT NOT NULL,
    ratingVotes4 TEXT NOT NULL,
    rating3percentage TEXT NOT NULL,
    ratingVotes3 TEXT NOT NULL,
    rating2percentage TEXT NOT NULL,
    ratingVotes2 TEXT NOT NULL,
    rating1percentage TEXT NOT NULL,
    ratingVotes1 TEXT NOT NULL,
    FOREIGN KEY (show_id) REFERENCES table250(show_id)
    );''')
def open_db(filename:str)->Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)#connect to existing DB or create new one
    cursor = db_connection.cursor()#get ready to read/write data
    return db_connection, cursor

def close_db(connection:sqlite3.Connection):
    connection.commit()#make sure any changes get saved
    connection.close()
def getUserRatings(showId):
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/{showId}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    return results.json()


def get250Shows():
    loc = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    return results.json()


def writeToFile250(tvDic):
    for i in range(250):
        f.write("rank:" + ((tvDic.get("items"))[i]).get("rank") + "\n")
        f.write(((tvDic.get("items"))[i]).get("title") + "\n")
        f.write("year:" + ((tvDic.get("items"))[i]).get("year") + "\n")
        f.write("id:" + ((tvDic.get("items"))[i]).get("id") + "\n\n")


def searchByTitle(title, tv):
    for j in range(250):
        if ((tv.get("items"))[j]).get("title") == title:
            return ((tv.get("items"))[j]).get("rank")


def searchByRank(rank, tv):
    for k in range(250):
        if ((tv.get("items"))[k]).get("rank") == rank:
            return ((tv.get("items"))[k]).get("title")


def findIdByTitle(title, tv):

    for w in range(250):
        if ((tv.get("items"))[w]).get("title") == title:
            return ((tv.get("items"))[w]).get("id")


def findIdbyRank(rank, tv):

    for n in range(250):
        if ((tv.get("items"))[n]).get("rank") == rank:
            return ((tv.get("items"))[n]).get("id")


def writeRatings(dic):

    f.write(dic.get("title") + "\n")
    if len(dic.get("ratings")) == 0:
        f.write("No ratings found!" + "\n\n")

    else:

        for m in range(len(dic.get("ratings"))):
            f.write("rating " + ((dic.get("ratings")[m]).get("rating")) + "\n")
            f.write("percent " + ((dic.get("ratings")[m]).get("percent")) + "\n")
            f.write("votes " + ((dic.get("ratings")[m]).get("votes")) + "\n\n")

def add250(cursor:sqlite3.Cursor,tv):
    q = "INSERT INTO table250(show_id,title,full_title,year,crew,imdb_rating,rating_count) VALUES (?,?,?,?,?,?,?)"
    for i in range(250):
        cursor.execute(q, (((tv.get("items"))[i]).get("id"),((tv.get("items"))[i]).get("title"),((tv.get("items"))[i]).get("fullTitle"),((tv.get("items"))[i]).get("year"),((tv.get("items"))[i]).get("crew"),((tv.get("items"))[i]).get("imDbRating"),((tv.get("items"))[i]).get("imDbRatingCount")))

def addRatings(cursor:sqlite3.Cursor,data):
    q = "INSERT INTO ratings(show_id,total_rating,total_rating_votes,rating10percentage,ratingVotes10,rating9percentage,ratingVotes9,rating8percentage,ratingVotes8,rating7percentage,ratingVotes7,rating6percentage,ratingVotes6,rating5percentage,ratingVotes5,rating4percentage,ratingVotes4,rating3percentage,ratingVotes3,rating2percentage,ratingVotes2,rating1percentage,ratingVotes1) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    cursor.execute(q, (data.get("imDbId"),data.get("totalRating"),data.get("totalRatingVotes"),(data.get("ratings")[0].get("percent")),(data.get("ratings")[0].get("votes")),(data.get("ratings")[1].get("percent")),(data.get("ratings")[1].get("votes")),(data.get("ratings")[2].get("percent")),(data.get("ratings")[2].get("votes")),(data.get("ratings")[3].get("percent")),(data.get("ratings")[3].get("votes")),(data.get("ratings")[4].get("percent")),(data.get("ratings")[4].get("votes")),(data.get("ratings")[5].get("percent")),(data.get("ratings")[5].get("votes")),(data.get("ratings")[6].get("percent")),(data.get("ratings")[6].get("votes")),(data.get("ratings")[7].get("percent")),(data.get("ratings")[7].get("votes")),(data.get("ratings")[8].get("percent")),(data.get("ratings")[8].get("votes")),(data.get("ratings")[9].get("percent")),(data.get("ratings")[9].get("votes"))))

def main():

    tv = get250Shows()
    data1 = getUserRatings(findIdbyRank("1", tv))
    data50 = getUserRatings(findIdbyRank("50", tv))
    data100 = getUserRatings(findIdbyRank("100", tv))
    data200 = getUserRatings(findIdbyRank("200",  tv))
    dataWheel = getUserRatings("tt7462410")

#    writeRatings(data1)
#    writeRatings(data50)
#    writeRatings(data100)
#    writeRatings(data200)
#    writeRatings(dataWheel)
#    writeToFile250(tv)
    conn, cursor = open_db("demo_db.sqlite")
    setup_db(cursor)
    add250(cursor,tv)
    addRatings(cursor, data1)
    addRatings(cursor, data50)
    addRatings(cursor, data100)
    addRatings(cursor, data200)
    addRatings(cursor, dataWheel)
# show_simple_select(cursor)
# show_select_with_join(cursor)
    close_db(conn)
    print(data1)


f.close()
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()
