""" Helper file to harvest API data """
import requests
import json
import sys

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
    #get path
    if (len(sys.argv) >= 2):
        path = sys.argv[1]
    else:
        sys.exit("Error: require path to text file of endpoints to request")

    #enumerate paths
    with open(path, "r") as f:
        for l in f:
            Get(l.strip())
