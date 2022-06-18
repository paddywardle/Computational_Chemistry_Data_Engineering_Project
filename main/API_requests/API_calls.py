from HTTPRequests import HTTPRequests
import pandas as pd

def pubchem_compound_query(url, num_records, properties_string):

    # initialise HTTPRequests class
    api_class = HTTPRequests()

    if num_records > 865:
        num_calls = int(num_records/865)
        count = 0

        for i in range(num_calls):
            records_list = [str(x) for x in range(count+1,count+865)]
            records_string = ','.join(records_list)
            url_with_records = url.format(records_string, properties_string)
            response = api_class.get(url_with_records)
            response_json = response.json()
            count += 865
            
            if i == 0:
                df = pd.DataFrame(response_json['PropertyTable']['Properties'])
            else:
                df_other = pd.DataFrame(response_json['PropertyTable']['Properties'])
                df = pd.concat([df, df_other])

        if count < num_records:
            records_list = [str(x) for x in range(count,num_records)]
            records_string = ','.join(records_list)
            url_with_records = url.format(records_string, properties_string)
            response = api_class.get(url_with_records)
            response_json = response.json()
            df_other = pd.DataFrame(response_json['PropertyTable']['Properties'])
            df = pd.concat([df, df_other])
        
        return df.reset_index()

    records_list = [str(x) for x in range(1,num_records)]
    records_string = ','.join(records_list)
    url_with_records = url.format(records_string, properties_string)
    response = api_class.get(url_with_records)
    response_json = response.json()
    df = pd.DataFrame(response_json['PropertyTable']['Properties'])

    return df

if __name__ == "__main__":

    properties = ['MolecularFormula','MolecularWeight','CanonicalSMILES','IsomericSMILES','InChI','InChIKey','IUPACName','Title','XLogP','ExactMass','MonoisotopicMass','TPSA','Complexity','Charge','HBondDonorCount','HBondAcceptorCount',
                  'RotatableBondCount','HeavyAtomCount','IsotopeAtomCount','AtomStereoCount','DefinedAtomStereoCount','UndefinedAtomStereoCount','BondStereoCount','DefinedBondStereoCount','UndefinedBondStereoCount','CovalentUnitCount','Volume3D',
                  'XStericQuadrupole3D','YStericQuadrupole3D','ZStericQuadrupole3D','FeatureCount3D','FeatureAcceptorCount3D','FeatureDonorCount3D','FeatureAnionCount3D','FeatureCationCount3D','FeatureRingCount3D','FeatureHydrophobeCount3D',
                  'ConformerModelRMSD3D','EffectiveRotorCount3D','ConformerCount3D','Fingerprint2D']
    
    properties_string = ','.join(properties)

    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{0}/property/{1}/JSON'

    num_records = int(input("Input the number of records you want: "))

    df = pubchem_compound_query(url, num_records, properties_string)

    df.to_json("../../raw_data/pubchem_raw_data.json")