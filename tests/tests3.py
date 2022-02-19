import main


def test_RankUpDownHappy():
    testDic = {'items': [{'id': '1', 'rank': '1', 'rankUpDown': '-1000', 'title': 'a'},
               {'id': '2', 'rank': '1', 'rankUpDown': '3', 'title': 'b'},
               {'id': '3', 'rank': '1', 'rankUpDown': '1', 'title': 'c'},
               {'id': '4', 'rank': '1', 'rankUpDown': '-100', 'title': 'd'}]}
    testList1 = main.orderRankUpDownMOV(4, testDic)

    # This test shows that the orderRankUpDown function put the numbs in the correct
    # order from biggest neg change to pos
    assert int(testList1[0][1]) == -1000
    assert int(testList1[1][1]) == -100
    assert int(testList1[2][1]) == 1
    assert int(testList1[3][1]) == 3


def test_RankUpDownBad():
    testDic = {'items': [{'id': '1', 'rank': '1', 'rankUpDown': '-10034rf 0', 'title': 'a'},
               {'id': '2', 'rank': '1', 'rankUpDown': '', 'title': 'b'},
               {'id': '3', 'rank': '1', 'rankUpDown': ' ', 'title': 'c'},
               {'id': '4', 'rank': '1', 'rankUpDown': '-1asd00', 'title': 'd'}]}
    testList2 = main.orderRankUpDownMOV(4, testDic)
    # This test has bad data with an empty list, spaces in between, and letters. This checks that all the data go
    # into the list even with that bad data
    assert len(testList2) == 4

