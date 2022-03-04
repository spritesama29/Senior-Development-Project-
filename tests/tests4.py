import main
import windowsData
def test_orderedDataTest():
    conn, cursor = main.open_db("otherTestData.sqlite")
    main.setup_db(cursor)

    q = "INSERT INTO popularTV(show_id,rank,rankUpDown,title,full_title,year,crew,imdb_rating,rating_count) " \
        "VALUES (?,?,?,?,?,?,?,?,?)"

    cursor.execute(q, ("i", 3,23,"one1","one","2022","Obama","100.4","12345"))
    cursor.execute(q, ("i", 2, 34, "one1","one", "2022", "Obama", "100.4", "12345"))
    cursor.execute(q, ("i", 4, 1, "one1", "one","2022", "Obama", "100.4", "12345"))
    cursor.execute(q, ("i", 5, -1, "one1", "one","2022", "Obama", "100.4", "12345"))
    tv = main.orderBy(cursor, "tv")
    tv2 = main.rankBy(cursor,"tv")

    # This test shows that the data is ordered by biggest rankUpDown to lowest by asserting that 34 is at the top
    # This test shows that the data is ordered by rank by asserting that the highest rank, 2, is at the top
    assert tv[0][1] == 2
    assert tv[0][2] == 34

def test_posAndNegMovers():
    testData = [["random","rank",1],["random","rank",2],["random","rank",-1]]
    posPull = main.posAndNegSort(testData,testData,"posMOV")
    negPull = main.posAndNegSort(testData, testData,"negMOV")
    # This test takes in data and sorts it by a positive or negative ranking.
    # This then checks that there are 2 pos numbs and 1 neg num in their respective lists based on rank up down

    assert len(posPull)==2
    assert len(negPull)==1