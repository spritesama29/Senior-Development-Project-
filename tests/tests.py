
import main


def test_checkTables():
    conn, cursor = main.open_db("testdata.sqlite")
    main.setup_db(cursor)
    tv = main.get250Shows()
    mov250 = main.get250movies()
    poptv = main.getMostPopularTVs()
    popMov = main.getMostPopularMovies()

    orderedTV = main.orderRankUpDownMOV(100, poptv)
    negChange = main.getUserRatings(orderedTV[0][0])
    posChange3 = main.getUserRatings(orderedTV[97][0])
    posChange2 = main.getUserRatings(orderedTV[98][0])
    posChange1 = main.getUserRatings(orderedTV[99][0])
    main.addRatingsMOV(cursor, negChange)
    main.addRatingsMOV(cursor, posChange3)
    main.addRatingsMOV(cursor, posChange2)
    main.addRatingsMOV(cursor, posChange1)
    main.add250TV(cursor, tv)
    main.add250MOV(cursor,mov250)
    main.addPopTV(cursor,poptv)
    main.addPopMOV(cursor,popMov)

    tv250Count = main.check250TV(cursor)
    mov250Count = main.check250MOV(cursor)
    popTVCount = main.checkPOPTV(cursor)
    popMOVCount = main.checkPOPMOV(cursor)
    ratingsMOVCount = main.checkRatingMOV(cursor)
    main.close_db(conn)
    assert tv250Count == 250
    assert mov250Count == 250
    assert popTVCount == 100
    assert popMOVCount == 100
    assert  ratingsMOVCount == 4


def test_foreignKeyMOV():
    conn, cursor = main.open_db("testdata.sqlite")
    sqlQuery = main.foreignKeyTest(cursor)
    queryCheck = 0
    sqlQueryLen = len(sqlQuery)
    # This test takes in the split sql query gotten from sql master. It then looks for the word foreign and
    # then once it finds it, in then looks for references. Once we find references, we then know directly after it
    # Will be the statement of the table so we iterate through the index afte reference till we get the correct
    # Table name
    for i in range(sqlQueryLen):
        if sqlQuery[i] == "FOREIGN":
            for j in range(sqlQueryLen):
                if sqlQuery[j] == "REFERENCES":
                    testString = ""
                    for k in range(sqlQueryLen):
                        testString = testString + sqlQuery[j+1][k]
                        if testString == "popularMOV":
                            queryCheck = 1
                            break
                        else:
                            k += 1
        else:
            i += 1
    main.close_db(conn)
    assert queryCheck == 1
