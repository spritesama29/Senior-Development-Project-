
import main


def test_check250():
    conn, cursor = main.open_db("testdata.sqlite")
    main.setup_db(cursor)
    tv = main.get250Shows()
    main.add250(cursor, tv)

    result = main.check250TV(cursor)
    main.close_db(conn)
    assert result == 250
