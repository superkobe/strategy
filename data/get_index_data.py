import os
import sys
import json
import requests

import pandas as pd
from tqdm import tqdm


def get_index_code(save_path):
    if os.path.exists(save_path):
        return pd.read_csv(save_path)
    else:
        try:
            r = requests.get("https://danjuanapp.com/djapi/index_eva/dj", headers={"user-agent":"Mozilla/5.0"})
            r.raise_for_status()
        except Exception as e:
            print(e)
            sys.exit(1)
        
        r.encoding = r.apparent_encoding
        data = json.loads(r.text)
        index_code_data = [[d["id"], d["name"], d["index_code"]] for d in data["data"]["items"]]
        df = pd.DataFrame(index_code_data, columns=["id", "name", "index_code"])
        df.to_csv(save_path, index=None)
        return df


def get_index_data(index_codes, save_path):
    if os.path.exists(save_path):
        return json.load(open(save_path, "r"))
    else:
        DATA_TYPES = ["pe", "pb", "roe"]
        URL = " https://danjuanapp.com/djapi/index_eva/{}_history/{}?day=all"

        def get_index_data(index_code, data_type):
            try:
                r = requests.get(URL.format(data_type, index_code), headers={"user-agent": "Mozilla/5.0"})
                r.raise_for_status()
            except Exception as e:
                print(e)
                sys.exit(1)
            
            r.encoding = r.apparent_encoding
            data = json.loads(r.text)
            return data["data"][f"index_eva_{data_type}_growths"]

        data = {}
        for index_code in tqdm(index_codes, desc="Get index data"):
            for dt in DATA_TYPES:
                data[index_code] = get_index_data(index_code, dt)
        
        with open(save_path, "w") as f:
            json.dump(data, f)
    

if __name__ == "__main__":
    df = get_index_code(save_path="index_name_code.csv")
    get_index_data(df["index_code"].tolist(), save_path="index_data.json")
