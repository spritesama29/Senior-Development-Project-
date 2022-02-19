import requests
import secrets
import sqlite3
from typing import Tuple

# Kyle Stearns

f = open("data.txt", "w")


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute("""DROP TABLE IF EXISTS TABLE250""")
    cursor.execute('''CREATE TABLE IF NOT EXISTS table250(
    show_id TEXT PRIMARY KEY,
    rank TEXT NOT NULL,
    title TEXT NOT NULL,
    full_title TEXT NOT NULL,
    year TEXT NOT NULL,
    crew TEXT NOT NULL,
    imdb_rating TEXT NOT NULL,
    rating_count TEXT NOT NULL
    );''')
    cursor.execute("""DROP TABLE IF EXISTS TABLE250MOV""")
    cursor.execute('''CREATE TABLE IF NOT EXISTS table250MOV(
        show_id TEXT PRIMARY KEY,
        rank TEXT NOT NULL,
        title TEXT NOT NULL,
        full_title TEXT NOT NULL,
        year TEXT NOT NULL,
        crew TEXT NOT NULL,
        imdb_rating TEXT NOT NULL,
        rating_count TEXT NOT NULL
        );''')
    cursor.execute("""DROP TABLE IF EXISTS PopularTV""")
    cursor.execute('''CREATE TABLE IF NOT EXISTS popularTV(
        show_id TEXT NOT NULL,
        rank TEXT NOT NULL,
        rankUpDown TEXT NOT NULL,
        title TEXT NOT NULL,
        full_title TEXT NOT NULL,
        year TEXT NOT NULL,
        crew TEXT NOT NULL,
        imdb_rating TEXT NOT NULL,
        rating_count TEXT NOT NULL,
        FOREIGN KEY (show_id) REFERENCES table250(show_id)
        );''')
    cursor.execute("""DROP TABLE IF EXISTS popularMOV""")
    cursor.execute('''CREATE TABLE IF NOT EXISTS popularMOV(
            show_id TEXT NOT NULL,
            rank TEXT NOT NULL,
            rankUpDown TEXT NOT NULL,
            title TEXT NOT NULL,
            full_title TEXT NOT NULL,
            year TEXT NOT NULL,
            crew TEXT NOT NULL,
            imdb_rating TEXT NOT NULL,
            rating_count TEXT NOT NULL,
            FOREIGN KEY (show_id) REFERENCES table250MOV(show_id)
            );''')
    cursor.execute("""DROP TABLE IF EXISTS ratings""")
    cursor.execute('''CREATE TABLE IF NOT EXISTS ratings(
    show_id TEXT NOT NULL,
    total_rating TEXT DEFAULT "none",
    total_rating_votes TEXT DEFAULT "none",
    rating10percentage TEXT DEFAULT "none",
    ratingVotes10 TEXT DEFAULT "none",
    rating9percentage TEXT DEFAULT "none",
    ratingVotes9 TEXT DEFAULT "none",
    rating8percentage TEXT DEFAULT "none",
    ratingVotes8 TEXT DEFAULT "none",
    rating7percentage TEXT DEFAULT "none",
    ratingVotes7 TEXT DEFAULT "none",
    rating6percentage TEXT DEFAULT "none",
    ratingVotes6 TEXT DEFAULT "none",
    rating5percentage TEXT DEFAULT "none",
    ratingVotes5 TEXT DEFAULT "none",
    rating4percentage TEXT DEFAULT "none",
    ratingVotes4 TEXT DEFAULT "none",
    rating3percentage TEXT DEFAULT "none",
    ratingVotes3 TEXT DEFAULT "none",
    rating2percentage TEXT DEFAULT "none",
    ratingVotes2 TEXT DEFAULT "none",
    rating1percentage TEXT DEFAULT "none",
    ratingVotes1 TEXT DEFAULT "none",
    FOREIGN KEY (show_id) REFERENCES table250(show_id)
    );''')
    cursor.execute("""DROP TABLE IF EXISTS ratingsMOV""")
    cursor.execute('''CREATE TABLE IF NOT EXISTS ratingsMOV(
        show_id TEXT PRIMARY KEY ,
        total_rating TEXT DEFAULT "none",
        total_rating_votes TEXT DEFAULT "none",
        rating10percentage TEXT DEFAULT "none",
        ratingVotes10 TEXT DEFAULT "none",
        rating9percentage TEXT DEFAULT "none",
        ratingVotes9 TEXT DEFAULT "none",
        rating8percentage TEXT DEFAULT "none",
        ratingVotes8 TEXT DEFAULT "none",
        rating7percentage TEXT DEFAULT "none",
        ratingVotes7 TEXT DEFAULT "none",
        rating6percentage TEXT DEFAULT "none",
        ratingVotes6 TEXT DEFAULT "none",
        rating5percentage TEXT DEFAULT "none",
        ratingVotes5 TEXT DEFAULT "none",
        rating4percentage TEXT DEFAULT "none",
        ratingVotes4 TEXT DEFAULT "none",
        rating3percentage TEXT DEFAULT "none",
        ratingVotes3 TEXT DEFAULT "none",
        rating2percentage TEXT DEFAULT "none",
        ratingVotes2 TEXT DEFAULT "none",
        rating1percentage TEXT DEFAULT "none",
        ratingVotes1 TEXT DEFAULT "none",
        FOREIGN KEY (show_id) REFERENCES popularMOV(show_id)
        );''')


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
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


def getMostPopularTVs():
    loc = f"https://imdb-api.com/en/API/MostPopularMovies/{secrets.secret_key}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    return results.json()


def getMostPopularMovies():
    loc = f"https://imdb-api.com/en/API/MostPopularTVs/{secrets.secret_key}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    return results.json()


def get250movies():
    loc = f"https://imdb-api.com/en/API/Top250Movies/{secrets.secret_key}"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    return results.json()


def addWheel(cursor: sqlite3.Cursor):
    q = "INSERT INTO table250(show_id,rank,title,full_title,year,crew,imdb_rating,rating_count)" \
        "VALUES (?,?,?,?,?,?,?,?)"
    cursor.execute(q, ("tt7462410", "The Wheel of Time", "0", "0", "0", "0", "0", "0"))


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


def orderRankUpDownMOV(num, tv):
    rankList = {}
    sortedList = {}
    for i in range(num):
        num = ((tv.get("items"))[i]).get("rankUpDown")
        newNum = ""
        if num=="":
            rankList[((tv.get("items"))[i]).get("id")] = 0
        else:
            for char in num:
                if char == " ":
                    newNum = newNum + "0"
                elif char == "-":
                    newNum = newNum + char
                elif char.isdigit():
                    if char != ",":
                        newNum = newNum + char
            rankList[((tv.get("items"))[i]).get("id")] = int(newNum)

    sortedList = sorted(rankList.items(), key=lambda t: t[1])

    return sortedList


def writeRatings(dic):
    f.write(dic.get("title") + "\n")
    if len(dic.get("ratings")) == 0:
        f.write("No ratings found!" + "\n\n")

    else:

        for m in range(len(dic.get("ratings"))):
            f.write("rating " + ((dic.get("ratings")[m]).get("rating")) + "\n")
            f.write("percent " + ((dic.get("ratings")[m]).get("percent")) + "\n")
            f.write("votes " + ((dic.get("ratings")[m]).get("votes")) + "\n\n")


def add250TV(cursor: sqlite3.Cursor, tv):
    q1 = "SELECT * FROM table250 WHERE show_id=(?)"
    check = cursor.execute(q1, ("tt5491994",))
    if len(check.fetchall()) == 0:
        q = "INSERT INTO table250(show_id, rank, title,full_title,year,crew,imdb_rating,rating_count)" \
            " VALUES (?,?,?,?,?,?,?,?)"

        for i in range(250):
            cursor.execute(q, (((tv.get("items"))[i]).get("id"), ((tv.get("items"))[i]).get("rank"),
                               ((tv.get("items"))[i]).get("title"),
                               ((tv.get("items"))[i]).get("fullTitle"), ((tv.get("items"))[i]).get("year"),
                               ((tv.get("items"))[i]).get("crew"), ((tv.get("items"))[i]).get("imDbRating"),
                               ((tv.get("items"))[i]).get("imDbRatingCount")))
    else:
        print("already in there")


def add250MOV(cursor: sqlite3.Cursor, tv):
    q = "INSERT INTO table250MOV(show_id, rank, title,full_title,year,crew,imdb_rating,rating_count) " \
        "VALUES (?,?,?,?,?,?,?,?)"
    for i in range(250):
        cursor.execute(q, (((tv.get("items"))[i]).get("id"), ((tv.get("items"))[i]).get("rank"),
                           ((tv.get("items"))[i]).get("title"),
                           ((tv.get("items"))[i]).get("fullTitle"), ((tv.get("items"))[i]).get("year"),
                           ((tv.get("items"))[i]).get("crew"), ((tv.get("items"))[i]).get("imDbRating"),
                           ((tv.get("items"))[i]).get("imDbRatingCount")))


def addPopTV(cursor: sqlite3.Cursor, tv):
    q = "INSERT INTO popularTV(show_id,rank,rankUpDown,title,full_title,year,crew,imdb_rating,rating_count) " \
        "VALUES (?,?,?,?,?,?,?,?,?)"
    for i in range(100):
        cursor.execute(q, (((tv.get("items"))[i]).get("id"), ((tv.get("items"))[i]).get("rank"),
                           ((tv.get("items"))[i]).get("rankUpDown"), ((tv.get("items"))[i]).get("title"),
                           ((tv.get("items"))[i]).get("fullTitle"), ((tv.get("items"))[i]).get("year"),
                           ((tv.get("items"))[i]).get("crew"), ((tv.get("items"))[i]).get("imDbRating"),
                           ((tv.get("items"))[i]).get("imDbRatingCount")))


def addPopMOV(cursor: sqlite3.Cursor, tv):
    q = "INSERT INTO popularMOV(show_id,rank,rankUpDown,title,full_title,year,crew,imdb_rating,rating_count) " \
        "VALUES (?,?,?,?,?,?,?,?,?)"
    for i in range(100):
        cursor.execute(q, (((tv.get("items"))[i]).get("id"), ((tv.get("items"))[i]).get("rank"),
                           ((tv.get("items"))[i]).get("rankUpDown"), ((tv.get("items"))[i]).get("title"),
                           ((tv.get("items"))[i]).get("fullTitle"), ((tv.get("items"))[i]).get("year"),
                           ((tv.get("items"))[i]).get("crew"), ((tv.get("items"))[i]).get("imDbRating"),
                           ((tv.get("items"))[i]).get("imDbRatingCount")))


def addRatings(cursor: sqlite3.Cursor, data):
    if len(data.get("ratings")) == 0:
        q = "INSERT INTO ratings(show_id,total_rating,total_rating_votes,rating10percentage," \
            "ratingVotes10,rating9percentage,ratingVotes9," \
            "rating8percentage,ratingVotes8,rating7percentage,ratingVotes7,rating6percentage,ratingVotes6," \
            "rating5percentage,ratingVotes5,rating4percentage,ratingVotes4,rating3percentage,ratingVotes3," \
            "rating2percentage,ratingVotes2,rating1percentage,ratingVotes1) " \
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(q, (data.get("imDbId"), data.get("totalRating"),
                           data.get("totalRatingVotes"), "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                           "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",))
    else:
        q = "INSERT INTO ratings(show_id,total_rating,total_rating_votes,rating10percentage," \
            "ratingVotes10,rating9percentage,ratingVotes9," \
            "rating8percentage,ratingVotes8,rating7percentage,ratingVotes7,rating6percentage,ratingVotes6," \
            "rating5percentage,ratingVotes5,rating4percentage,ratingVotes4,rating3percentage,ratingVotes3," \
            "rating2percentage,ratingVotes2,rating1percentage,ratingVotes1) " \
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(q, (data.get("imDbId"), data.get("totalRating"), data.get("totalRatingVotes"),
                           (data.get("ratings")[0].get("percent")), (data.get("ratings")[0].get("votes")),
                           (data.get("ratings")[1].get("percent")), (data.get("ratings")[1].get("votes")),
                           (data.get("ratings")[2].get("percent")), (data.get("ratings")[2].get("votes")),
                           (data.get("ratings")[3].get("percent")),
                           (data.get("ratings")[3].get("votes")), (data.get("ratings")[4].get("percent")),
                           (data.get("ratings")[4].get("votes")), (data.get("ratings")[5].get("percent")),
                           (data.get("ratings")[5].get("votes")), (data.get("ratings")[6].get("percent")),
                           (data.get("ratings")[6].get("votes")), (data.get("ratings")[7].get("percent")),
                           (data.get("ratings")[7].get("votes")), (data.get("ratings")[8].get("percent")),
                           (data.get("ratings")[8].get("votes")), (data.get("ratings")[9].get("percent")),
                           (data.get("ratings")[9].get("votes"))))


def addRatingsMOV(cursor: sqlite3.Cursor, data):
    try:
        q = "INSERT INTO ratingsMOV(show_id,total_rating,total_rating_votes,rating10percentage," \
            "ratingVotes10,rating9percentage,ratingVotes9," \
            "rating8percentage,ratingVotes8,rating7percentage,ratingVotes7,rating6percentage,ratingVotes6," \
            "rating5percentage,ratingVotes5,rating4percentage,ratingVotes4,rating3percentage,ratingVotes3," \
            "rating2percentage,ratingVotes2,rating1percentage,ratingVotes1) " \
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(q, (data.get("imDbId"), data.get("totalRating"), data.get("totalRatingVotes"),
                           (data.get("ratings")[0].get("percent")), (data.get("ratings")[0].get("votes")),
                           (data.get("ratings")[1].get("percent")), (data.get("ratings")[1].get("votes")),
                           (data.get("ratings")[2].get("percent")), (data.get("ratings")[2].get("votes")),
                           (data.get("ratings")[3].get("percent")),
                           (data.get("ratings")[3].get("votes")), (data.get("ratings")[4].get("percent")),
                           (data.get("ratings")[4].get("votes")), (data.get("ratings")[5].get("percent")),
                           (data.get("ratings")[5].get("votes")), (data.get("ratings")[6].get("percent")),
                           (data.get("ratings")[6].get("votes")), (data.get("ratings")[7].get("percent")),
                           (data.get("ratings")[7].get("votes")), (data.get("ratings")[8].get("percent")),
                           (data.get("ratings")[8].get("votes")), (data.get("ratings")[9].get("percent")),
                           (data.get("ratings")[9].get("votes"))))
    except Exception:
        q = "INSERT INTO ratingsMOV(show_id,total_rating,total_rating_votes,rating10percentage," \
            "ratingVotes10,rating9percentage,ratingVotes9," \
            "rating8percentage,ratingVotes8,rating7percentage,ratingVotes7,rating6percentage,ratingVotes6," \
            "rating5percentage,ratingVotes5,rating4percentage,ratingVotes4,rating3percentage,ratingVotes3," \
            "rating2percentage,ratingVotes2,rating1percentage,ratingVotes1) " \
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(q, (data.get("imDbId"), data.get("totalRating"),
                           data.get("totalRatingVotes"), "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                           "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",))


def check250TV(cursor: sqlite3.Cursor):
    q = "SELECT COUNT(*) FROM table250"
    cursor.execute(q)
    return cursor.fetchall()[0][0]


def check250MOV(cursor: sqlite3.Cursor):
    q = "SELECT COUNT(*) FROM table250MOV"
    cursor.execute(q)
    return cursor.fetchall()[0][0]


def checkPOPTV(cursor: sqlite3.Cursor):
    q = "SELECT COUNT(*) FROM popularTV"
    cursor.execute(q)
    return cursor.fetchall()[0][0]


def checkPOPMOV(cursor: sqlite3.Cursor):
    q = "SELECT COUNT(*) FROM popularMOV"
    cursor.execute(q)
    return cursor.fetchall()[0][0]


def checkRatingMOV(cursor: sqlite3.Cursor):
    q = "SELECT COUNT(*) FROM ratingsMOV"
    cursor.execute(q)
    return cursor.fetchall()[0][0]


def foreignKeyTest(cursor: sqlite3.Cursor):
    q = "SELECT * FROM sqlite_master WHERE name='ratingsMOV'"
    a = cursor.execute(q)
    b = a.fetchall()[0][4]

    return b.split()


def main():
    tv = get250Shows()

    data1 = getUserRatings(findIdbyRank("1", tv))
    data50 = getUserRatings(findIdbyRank("50", tv))
    data100 = getUserRatings(findIdbyRank("100", tv))
    data200 = getUserRatings(findIdbyRank("200", tv))
    dataWheel = getUserRatings("tt7462410")

    conn, cursor = open_db("demo_db.sqlite")

    setup_db(cursor)

    mov = get250movies()

    add250MOV(cursor, mov)

    poptv = getMostPopularTVs()

    addPopTV(cursor, poptv)

    popMov = getMostPopularMovies()

    addPopMOV(cursor, popMov)

    dic = orderRankUpDownMOV(100, mov)
    negChange = getUserRatings(dic[0][0])
    posChange3 = getUserRatings(dic[97][0])
    posChange2 = getUserRatings(dic[98][0])
    posChange1 = getUserRatings(dic[99][0])
    addRatingsMOV(cursor, negChange)
    addRatingsMOV(cursor, posChange3)
    addRatingsMOV(cursor, posChange2)
    addRatingsMOV(cursor, posChange1)

    add250TV(cursor, tv)

    addRatings(cursor, data1)
    addRatings(cursor, data50)
    addRatings(cursor, data100)
    addRatings(cursor, data200)
    addRatings(cursor, dataWheel)
    addWheel(cursor)

    close_db(conn)


f.close()
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()
