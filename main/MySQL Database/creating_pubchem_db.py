from CreateDB import CreateDB
from getpass import getpass

if __name__ == "__main__":

    user = input("Enter Database Username: ")

    password = getpass("Enter Database Password: ")

    db_name = input("Enter Database Name: ")

    db = CreateDB(user, password)

    db.create_db(db_name)

    db.see_dbs()

