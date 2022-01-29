import requests
import secrets


def main():
    loc = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/tt7462410"
    results = requests.get(loc)
    if results.status_code != 200:
        print("help!")
        return
    data = results.json()
    print(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()