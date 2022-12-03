import requests


if __name__=="__main__":
    headers = {
        'x-rapidapi-key': "ce19d0164fmsh3d383efc0e85ce5p16dcb1jsnb1a4a3c79541",
        'x-rapidapi-host': "airport-info.p.rapidapi.com"
        }
    url = "https://airport-info.p.rapidapi.com/airport?icao=KJFK"
    x = requests.get(url, headers=headers)
    print(x.status_code)
    print(x.content)