
import main


def test_check250():
    conn, cursor = main.open_db("testdata.sqlite")
    main.setup_db(cursor)
    tv = main.get250Shows()


    main.add250(cursor, tv)
    #main.close_db(conn)
    result = main.check250(cursor)


    assert result == 250


def test_checkTable():
    conn, cursor = main.open_db("testdata.sqlite")
    main.setup_db(cursor)


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


