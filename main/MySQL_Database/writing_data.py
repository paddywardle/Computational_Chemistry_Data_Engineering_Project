from CreateDB import CreateDB
from main.config import configuration_dict
import pandas as pd

if __name__ == "__main__":

    user = configuration_dict['user']

    password = configuration_dict['password']

    db_name = configuration_dict['db_name']

    table_name = input("Enter Table Name: ")

    json_path = "../../raw_data/pubchem_raw_data.json"

    df = pd.read_json(json_path)

    df.drop(['index'], axis=1, inplace=True)

    db = CreateDB(user, password)

    db.write_df(table_name, db_name, df)



    