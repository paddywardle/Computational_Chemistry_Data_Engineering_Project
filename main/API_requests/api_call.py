from HTTPRequests import HTTPRequests
from PIL import Image
from io import BytesIO
import pandas as pd
import numpy as np
import sys
import os
from getpass import getpass
from tqdm import tqdm
from bs4 import BeautifulSoup
import lxml
sys.path.append(os.path.dirname(os.getcwd())+"\\MySQL Database")
from CreateDB import CreateDB

def pubchem_compound_properties_query(num_records, start_cid=1, write_to_db='yes'):

    if write_to_db.upper() == "YES":
    
        user = input("Input Database User: ")
        password = getpass("Input Database Password: ")
        database = input("Input Database Name: ")

        # writing to MySQL database
        db_instance = CreateDB(user, password)

    # initialise HTTPRequests class
    api_class = HTTPRequests()

    # api properties
    properties = ['MolecularFormula','MolecularWeight','CanonicalSMILES','IsomericSMILES','InChI','InChIKey','IUPACName','Title','XLogP','ExactMass','MonoisotopicMass','TPSA','Complexity','Charge','HBondDonorCount','HBondAcceptorCount',
                'RotatableBondCount','HeavyAtomCount','IsotopeAtomCount','AtomStereoCount','DefinedAtomStereoCount','UndefinedAtomStereoCount','BondStereoCount','DefinedBondStereoCount','UndefinedBondStereoCount','CovalentUnitCount','Volume3D',
                'XStericQuadrupole3D','YStericQuadrupole3D','ZStericQuadrupole3D','FeatureCount3D','FeatureAcceptorCount3D','FeatureDonorCount3D','FeatureAnionCount3D','FeatureCationCount3D','FeatureRingCount3D','FeatureHydrophobeCount3D',
                'ConformerModelRMSD3D','EffectiveRotorCount3D','ConformerCount3D','Fingerprint2D']
    
    # joining them into a comma-separated string
    properties_string = ','.join(properties)

    # api url with values that can be formatted later <- iterating from starting cid to starting cid + num_records
    # because 0 isn't a record in the pubchem database
    for i in tqdm(range(start_cid, num_records+start_cid)):

        try:

            # url for properties database
            properties_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{it}/property/{properties}/XML'.format(it=i, properties=properties_string)

            # response for properties database
            properties_response = api_class.get(properties_url)

            # beautiful soup object for XML property data
            properties_bs = BeautifulSoup(properties_response.content, 'xml')

            # list to store xml tag values
            properties_data = {}

            # iterating through xml tags
            for prop in properties:
                # getting all values for each tag
                for text in properties_bs.find_all(prop):
                    b = text
                    # appending xml tag value to properties_data
                    properties_data[prop] = [b.get_text()]

            # creating dataframe from properties data (have to reshape as it is a column list)
            properties_df = pd.DataFrame(properties_data)

            # url for images database
            images_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{it}/PNG?record_type=2d&image_size=small'.format(it=i)

            # response for image database
            images_response = api_class.get(images_url)

            # image bytes object from response
            image = BytesIO(images_response.content)

            # array with image bytes object
            images_array = np.array([image])

            # images dataframe with single record
            images_df = pd.DataFrame(images_array, columns=['image'])

            if write_to_db.upper() == "YES":

                # writing properties dataframe to properties table in database
                db_instance.write_df('properties', database, properties_df)

                # writing image dataframe to images table in database
                db_instance.write_df('images', database, images_df)
        
        except AttributeError:

            pass

    return 0

if __name__ == "__main__":

    # record to start at in requests
    starting_record = int(input("Input record to start at: "))

    # number of records user wants
    num_records = int(input("Input the number of records you want: "))

    # write_to_db?
    write_to_db = input("Would you like to write data to the database?: ")

    # calling function
    pubchem_compound_properties_query(num_records, starting_record, write_to_db)