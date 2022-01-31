import requests
import secrets


f = open("data.txt", "w")


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
    for m in range(10):
        f.write("rating " + ((dic.get("ratings")[m]).get("rating")) + "\n")
        f.write("percent " + ((dic.get("ratings")[m]).get("percent")) + "\n")
        f.write("votes " + ((dic.get("ratings")[m]).get("votes")) + "\n\n")


def main():

    tv = get250Shows()
    data1 = getUserRatings(findIdbyRank("1", tv))
    data50 = getUserRatings(findIdbyRank("50", tv))
    data100 = getUserRatings(findIdbyRank("100", tv))
    data200 = getUserRatings(findIdbyRank("200",  tv))
    dataWheel = getUserRatings("tt7462410")

    writeRatings(data1)
    writeRatings(data50)
    writeRatings(data100)
    writeRatings(data200)
    writeRatings(dataWheel)
    writeToFile250(tv)

    f.close()
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()
