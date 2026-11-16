""" Helper file to harvest API data """
import requests
import json

def Get(url):
    #craft filename
    segments = url.split("/")
    out = segments[-1]

    #make request
    resp = requests.get(url)
    data = resp.json()

    #dump data
    with open(out, "w") as f:
        json.dump(data, f, indent=4)

    #return json
    return data

if __name__ == "__main__":
    endpoint = "https://data.ct.gov/resource/anen-a5ei.json"
    Get(endpoint)
