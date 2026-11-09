""" Program to convert CSV to json """
import sys
import pandas as pd

def CSVToJSON(path, out="./out.json"):
    """ Convert CSV file to JSON preprocessing """
    #create pandas dataframe from csv
    df = pd.read_csv(path)

    outJson = (df.groupby("Municipality or Borough", as_index=False)
               .apply(lamda x: x.to_dict(orient="records"))
               .reset_index()
               .rename(columns={0: "names"})
               .to_json(orient="records"))
    
    print(outJson)

    return out

if __name__ == "__main__":
    if (len(sys.argv) >= 2):
        path = sys.argv[1]
    else:
        sys.exit("Error: must provide csv path")

    CSVToJSON(path)
