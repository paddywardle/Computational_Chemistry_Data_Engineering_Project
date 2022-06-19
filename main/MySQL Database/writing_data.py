from CreateDB import CreateDB
from getpass import getpass
import pandas as pd

if __name__ == "__main__":

    user = input("Enter Database Username: ")

    password = getpass("Enter Database Password: ")

    db_name = input("Enter Database Name: ")

    json_path = "../../raw_data/pubchem_raw_data.json"

    df = pd.read_json(json_path)

    df.drop(['index'], axis=1, inplace=True)

    db = CreateDB(user, password)

    db.write_df(db_name, df)



    