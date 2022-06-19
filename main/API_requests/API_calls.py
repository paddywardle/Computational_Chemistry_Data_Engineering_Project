from HTTPRequests import HTTPRequests
import pandas as pd

def pubchem_compound_query(url, num_records, properties_string):

    # initialise HTTPRequests class
    api_class = HTTPRequests()

    # requesting 500 records at a time
    if num_records > 500:
        # getting the number of times 500 records will be requeste (any additional requests will be processed later)
        num_calls = int(num_records/500)

        # initialising record count
        count = 0

        for i in range(num_calls):
            # comma separated string of record numbers
            records_list = [str(x) for x in range(count+1,count+501)]
            records_string = ','.join(records_list)

            # formatting url with records and properties string
            url_with_records = url.format(records_string, properties_string)

            # requesting url
            response = api_class.get(url_with_records)

            # getting json from response
            response_json = response.json()
            count += 501
            
            #if the first iteration the create the dataframe, else concat to the dataframe
            if i == 0:
                df = pd.DataFrame(response_json['PropertyTable']['Properties'])
            else:
                df_other = pd.DataFrame(response_json['PropertyTable']['Properties'])
                df = pd.concat([df, df_other])

        # requesting any remaining records that don't make up a batch of 500
        if count < num_records:
            records_list = [str(x) for x in range(count,num_records)]
            records_string = ','.join(records_list)
            url_with_records = url.format(records_string, properties_string)
            response = api_class.get(url_with_records)
            response_json = response.json()
            df_other = pd.DataFrame(response_json['PropertyTable']['Properties'])
            df = pd.concat([df, df_other])
        
        return df.reset_index()

    # requesting a batch if the user requests a batch less than 500
    records_list = [str(x) for x in range(1,num_records)]
    records_string = ','.join(records_list)
    url_with_records = url.format(records_string, properties_string)
    response = api_class.get(url_with_records)
    response_json = response.json()
    df = pd.DataFrame(response_json['PropertyTable']['Properties'])

    return df

if __name__ == "__main__":

    # api properties
    properties = ['MolecularFormula','MolecularWeight','CanonicalSMILES','IsomericSMILES','InChI','InChIKey','IUPACName','Title','XLogP','ExactMass','MonoisotopicMass','TPSA','Complexity','Charge','HBondDonorCount','HBondAcceptorCount',
                  'RotatableBondCount','HeavyAtomCount','IsotopeAtomCount','AtomStereoCount','DefinedAtomStereoCount','UndefinedAtomStereoCount','BondStereoCount','DefinedBondStereoCount','UndefinedBondStereoCount','CovalentUnitCount','Volume3D',
                  'XStericQuadrupole3D','YStericQuadrupole3D','ZStericQuadrupole3D','FeatureCount3D','FeatureAcceptorCount3D','FeatureDonorCount3D','FeatureAnionCount3D','FeatureCationCount3D','FeatureRingCount3D','FeatureHydrophobeCount3D',
                  'ConformerModelRMSD3D','EffectiveRotorCount3D','ConformerCount3D','Fingerprint2D']
    
    # joining them into a comma-separated string
    properties_string = ','.join(properties)

    # api url with values that can be formatted later
    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{0}/property/{1}/JSON'

    # number of records user wants
    num_records = int(input("Input the number of records you want: "))

    # calling function
    df = pubchem_compound_query(url, num_records, properties_string)

    # saving json
    df.to_json("../../raw_data/pubchem_raw_data.json")