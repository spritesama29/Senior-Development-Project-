import main


def test_orderedDataTest():
    conn, cursor = main.open_db("otherTestData.sqlite")
    main.setup_db(cursor)

    q = "INSERT INTO popularTV(show_id,rank,rankUpDown,title,full_title,year,crew,imdb_rating,rating_count) " \
        "VALUES (?,?,?,?,?,?,?,?,?)"

    cursor.execute(q, ("i", 3, 23, "one1", "one", "2022", "Obama", "100.4", "12345"))
    cursor.execute(q, ("3", 2, 34, "one1", "one", "2022", "Obama", "100.4", "12345"))
    cursor.execute(q, ("5", 4, 1, "one1", "one", "2022", "Obama", "100.4", "12345"))
    cursor.execute(q, ("7", 5, -1, "one1", "one", "2022", "Obama", "100.4", "12345"))
    tv = main.orderBy(cursor, "tv")
    tv2 = main.rankBy(cursor, "tv")

    # This test shows that the data is ordered by biggest rankUpDown to lowest by asserting that 34 is at the top
    # This test shows that the data is ordered by rank by asserting that the highest rank, 2, is at the top
    assert tv2[0][1] == 2
    assert tv[0][2] == 34


def test_posAndNegMovers():
    testData = [["random", "rank", 1], ["random", "rank", 2], ["random", "rank", -1]]
    posPull = main.posAndNegSort(testData,testData, "posMOV")
    negPull = main.posAndNegSort(testData, testData, "negMOV")
    # This test takes in data and sorts it by a positive or negative ranking.
    # This then checks that there are 2 pos numbs and 1 neg num in their respective lists based on rank up down

    assert len(posPull) == 2
    assert len(negPull) == 1


def test_crossOvers():
    conn, cursor = main.open_db("otherTestData.sqlite")
    main.setup_db(cursor)

    q = "INSERT INTO popularTV(show_id,rank,rankUpDown,title,full_title,year,crew,imdb_rating,rating_count) " \
        "VALUES (?,?,?,?,?,?,?,?,?)"

    cursor.execute(q, ("i", 3, 23, "one1", "one", "2022", "Obama", "100.4", "12345"))
    conn.commit()
    q2 = "INSERT INTO table250(show_id,rank,title,full_title,year,crew,imdb_rating,rating_count) " \
        "VALUES (?,?,?,?,?,?,?,?)"
    cursor.execute(q2, ("i", 3, "one1", "one", "2022", "Obama", "100.4", "12345"))
    conn.commit()
    crossOverTV = main.getTVjoin(cursor)

    q3 = "INSERT INTO popularMOV(show_id,rank,rankUpDown,title,full_title,year,crew,imdb_rating,rating_count) " \
        "VALUES (?,?,?,?,?,?,?,?,?)"

    cursor.execute(q3, ("i", 3, 23, "one1", "one", "2022", "Obama", "100.4", "12345"))
    conn.commit()
    q4 = "INSERT INTO table250MOV(show_id,rank,title,full_title,year,crew,imdb_rating,rating_count) " \
         "VALUES (?,?,?,?,?,?,?,?)"
    cursor.execute(q4, ("i", 3, "one1", "one", "2022", "Obama", "100.4", "12345"))
    conn.commit()
    crossOverMOV = main.getMOVjoin(cursor)
    # This adds a pieces of dummy data to the popularTV and 250TV table and checks that the inner join returns 1
    # This adds a pieces of dummy data to the popularMOV and table250 table and checks that the inner join returns 1

    assert len(crossOverTV) == 1
    assert len(crossOverMOV) == 1
