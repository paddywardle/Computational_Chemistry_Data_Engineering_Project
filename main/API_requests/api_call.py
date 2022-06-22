from HTTPRequests import HTTPRequests
from PIL import Image
from io import BytesIO
import pandas as pd
import numpy as np
import sys
import os
from getpass import getpass
from tqdm import tqdm
sys.path.append(os.path.dirname(os.getcwd())+"\\MySQL Database")
from CreateDB import CreateDB


def pubchem_compound_properties_query(num_records, start_cid=1):

    # initialise HTTPRequests class
    api_class = HTTPRequests()

    # api properties
    properties = ['MolecularFormula','MolecularWeight','CanonicalSMILES','IsomericSMILES','InChI','InChIKey','IUPACName','Title','XLogP','ExactMass','MonoisotopicMass','TPSA','Complexity','Charge','HBondDonorCount','HBondAcceptorCount',
                  'RotatableBondCount','HeavyAtomCount','IsotopeAtomCount','AtomStereoCount','DefinedAtomStereoCount','UndefinedAtomStereoCount','BondStereoCount','DefinedBondStereoCount','UndefinedBondStereoCount','CovalentUnitCount','Volume3D',
                  'XStericQuadrupole3D','YStericQuadrupole3D','ZStericQuadrupole3D','FeatureCount3D','FeatureAcceptorCount3D','FeatureDonorCount3D','FeatureAnionCount3D','FeatureCationCount3D','FeatureRingCount3D','FeatureHydrophobeCount3D',
                  'ConformerModelRMSD3D','EffectiveRotorCount3D','ConformerCount3D','Fingerprint2D']
    
    # joining them into a comma-separated string
    properties_string = ','.join(properties)

    columns = [f'pixel_{x}' for x in range(1, 10001)]

    images_array = np.empty((0,0))

    # api url with values that can be formatted later
    for i in tqdm(range(start_cid, num_records+1)):

        properties_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{it}/property/{properties}/JSON'.format(it=i, properties=properties_string)

        images_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{it}/PNG?record_type=2d&image_size=small'.format(it=i)

        properties_response = api_class.get(properties_url)

        images_response = api_class.get(images_url)

        properties_json = properties_response.json()

        image = BytesIO(images_response.content)

        images_array = np.append(images_array, image)

        if i == start_cid:
            properties_df = pd.DataFrame(properties_json['PropertyTable']['Properties'])

        else:
            properties_df_other = pd.DataFrame(properties_json['PropertyTable']['Properties'])

            properties_df = pd.concat([properties_df, properties_df_other])
    
    images_df = pd.DataFrame(images_array, columns=['image'])

    user = input("Input Database User: ")
    password = getpass("Input Database Password: ")
    database = input("Input Database Name: ")

    # writing to MySQL database
    db_instance = CreateDB(user, password)

    db_instance.write_df('properties', database, properties_df)

    db_instance.write_df('images', database, images_df)

    return 0

if __name__ == "__main__":

    # number of records user wants
    num_records = int(input("Input the number of records you want: "))

    # calling function
    pubchem_compound_properties_query(num_records)