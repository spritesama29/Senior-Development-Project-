import sqlite3
import main
from typing import Tuple


def check250():
    result = main.check250(cursor) - 1

    assert result == 250


def checkTable():
    q2 = "SELECT * FROM table250 WHERE show_id=(?)"
    check = cursor.execute(q2, ("abcdefg",))
    if len(check.fetchall()) == 0:
        q = "INSERT INTO table250(show_id,title,full_title,year,crew,imdb_rating,rating_count) VALUES (?,?,?,?,?,?,?)"
        cursor.execute(q, ("abcdefg", "Sea of these", "Sea of these 2022", "2022",
                           "Kyle Stearns, Teddy Barnes, Micheal Foley,", "100.4", "12345"))

        q1 = "SELECT COUNT(*) FROM table250"
        cursor.execute(q1)
        result = cursor.fetchall()[0][0]

        assert result == 1
    else:
        print("already there")


conn, cursor = main.open_db("testdata")
main.setup_db(cursor)
tv = main.get250Shows()
checkTable()

main.add250(cursor, tv)

check250()
main.close_db(conn)
