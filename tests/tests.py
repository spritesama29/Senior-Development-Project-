
import main


def test_check250():
    conn, cursor = main.open_db("testdata.sqlite")
    main.setup_db(cursor)
    tv = main.get250Shows()
    main.add250(cursor, tv)
    main.close_db(conn)
    result = main.check250(cursor)

    assert result == 250
