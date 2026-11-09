""" Program to convert CSV to json """
import sys
import json
import datetime
import pandas as pd

#TODO
#reformat hierarchy for better nesting
#align to Ryan's format
#ingest more sources
#translate from json to Sam's pug format

def CSVToJSON(path, out="./out.json"):
    """ Convert CSV file to JSON preprocessing """
    #create pandas dataframe from csv
    df = pd.read_csv(path)

    #group by municipality/borough name and nest officials
    outDF = (df.groupby(["Municipality or Borough","Jurisdiction Type"])
               .apply(lambda x: x[["Name","Title","Phone","Email Address"]].to_dict("records"))
               .reset_index()
               .rename(columns={0:"Officials"}))
    #separate outjson and outdf for granularity
    outDF["Timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #get text and convert to json
    outTxt = outDF.to_json(orient="records")
    outJson = json.loads(outTxt)

    #write to path
    with open(out, "w") as f:
        json.dump(outJson, f, indent=4)
    
    #return json object
    return outJson

if __name__ == "__main__":
    if (len(sys.argv) >= 2):
        path = sys.argv[1]
    else:
        sys.exit("Error: must provide csv path")

    CSVToJSON(path)
