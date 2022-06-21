from CreateDB import CreateDB
from getpass import getpass

if __name__ == "__main__":

    user = input("Enter Database Username: ")

    password = getpass("Enter Database Password: ")

    db_name = input("Enter Database Name: ")

    create_query = f"""
    CREATE TABLE properties(
        id INT AUTO_INCREMENT PRIMARY KEY,
        cid INT,
        MolecularFormula TEXT,
        MolecularWeight FLOAT,
        CanonicalSMILES TEXT,
        IsomericSMILES TEXT,
        InChI TEXT,
        InChIKey TEXT,
        IUPACName TEXT,
        XLogP FLOAT,
        ExactMass FLOAT,
        MonoisotopicMass FLOAT,
        TPSA FLOAT,
        Complexity FLOAT,
        Charge FLOAT,
        HBondDonorCount FLOAT,
        HBondAcceptorCount FLOAT,
        RotatableBondCount FLOAT,
        HeavyAtomCount FLOAT,
        IsotopeAtomCount FLOAT,
        AtomStereoCount INT,
        DefinedAtomStereoCount FLOAT,
        UndefinedAtomStereoCount FLOAT,
        BondStereoCount INT,
        DefinedBondStereoCount FLOAT,
        UndefinedBondStereoCount FLOAT,
        CovalentUnitCount FLOAT,
        Volume3D FLOAT,
        XStericQuadrupole3D FLOAT,
        YStericQuadrupole3D FLOAT,
        ZStericQuadrupole3D FLOAT,
        FeatureCount3D FLOAT,
        FeatureAcceptorCount3D FLOAT,
        FeatureDonorCount3D FLOAT,
        FeatureAnionCount3D FLOAT,
        FeatureCationCount3D FLOAT,
        FeatureRingCount3D FLOAT,
        FeatureHydrophobeCount3D FLOAT,
        ConformerModelRMSD3D FLOAT,
        EffectiveRotorCount3D FLOAT,
        ConformerCount3D INT,
        Fingerprint2D TEXT,
        Title TEXT
    )
    """

    db = CreateDB(user, password)

    db.commit_query(db_name, create_query)
