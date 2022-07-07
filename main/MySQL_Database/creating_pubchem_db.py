from CreateDB import CreateDB
from main.config import configuration_dict

if __name__ == "__main__":

    user = configuration_dict['user']

    password = configuration_dict['password']

    db_name = configuration_dict['db_name']

    db = CreateDB(user, password)

    db.create_db(db_name)

    db.see_dbs()

