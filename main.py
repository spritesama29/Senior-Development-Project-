import requests
import secrets


def main():

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
    # print(data)
    # 1 tt5491994
    # 50 tt2297757
    # 100 tt0286486
    # 200 tt1492966

    f = open("data.txt", "w")

    def writeToFile250(tvDic):
        for i in range(250):
            f.write("rank:" + ((tvDic.get("items"))[i]).get("rank") + "\n")
            f.write(((tvDic.get("items"))[i]).get("title") + "\n")
            f.write("year:" + ((tvDic.get("items"))[i]).get("year") + "\n")
            f.write("id:" + ((tvDic.get("items"))[i]).get("id") + "\n\n")

    def searchByTitle(title):
        for j in range(250):
            if ((tv.get("items"))[j]).get("title") == title:
                return ((tv.get("items"))[j]).get("rank")

    def searchByRank(rank):
        for k in range(250):
            if ((tv.get("items"))[k]).get("rank") == rank:
                return ((tv.get("items"))[k]).get("title")

    def findIdByTitle(title):

        for w in range(250):
            if ((tv.get("items"))[w]).get("title") == title:
                return ((tv.get("items"))[w]).get("id")

    def findIdbyRank(rank):

        for n in range(250):
            if ((tv.get("items"))[n]).get("rank") == rank:
                return ((tv.get("items"))[n]).get("id")

    def writeRatings(dic):

        f.write(dic.get("title") + "\n")
        for m in range(10):
            f.write("rating " + ((dic.get("ratings")[m]).get("rating")) + "\n")
            f.write("percent " + ((dic.get("ratings")[m]).get("percent")) + "\n")
            f.write("votes " + ((dic.get("ratings")[m]).get("votes")) + "\n\n")

    data1 = getUserRatings("tt5491994")
    data50 = getUserRatings("tt2297757")
    data100 = getUserRatings("tt0286486")
    data200 = getUserRatings("tt1492966")

    # dataWheel = getUserRatings()

    tv = get250Shows()
    writeRatings(data1)
    writeRatings(data50)
    writeRatings(data100)
    writeRatings(data200)

    writeToFile250(tv)

    f.close()
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()
