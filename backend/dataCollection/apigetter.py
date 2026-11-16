""" Helper file to harvest API data """
import requests
import json
import sys

def Get(url, out):
    #make request
    resp = requests.get(url)
    data = resp.json()

    #dump data
    with open(out, "w") as f:
        json.dump(data, f, indent=4)

    #return json
    return data

if __name__ == "__main__":
    """ Requires txt file with [outputname],[url] as format """
    #get path
    if (len(sys.argv) >= 2):
        path = sys.argv[1]
    else:
        sys.exit("Error: require path to text file of endpoints to request")

    #enumerate paths
    with open(path, "r") as f:
        for l in f:
            split = l.strip().split(",")
            Get(split[1], split[0])
