from main.secrets import db_secrets
configuration_dict = {
    "db_name": "pubchem_database",
    "host": "localhost",
    "user": "root",
    "password": db_secrets["password"]
}