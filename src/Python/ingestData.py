import pandas as pd

class IngestData:
    def __init__(self, centroidsFile, iodFile):
        self.centroidsFile = centroidsFile
        self.iodFile = iodFile

    def readCentroidsMap(self):
        #read csv file but only certain columns
        columnsToLoad = ['PCD', 'LSOA01']
        centroidsDF = pd.read_csv(self.centroidsFile, usecols=columnsToLoad, compression='gzip')
        return centroidsDF
    
    def readIndicesOfDeprivation(self):
        columnsToLoad = ['LSOA code (2011)',
                        'Index of Multiple Deprivation (IMD) Decile (where 1 is most deprived 10% of LSOAs)',
                        'Income Decile (where 1 is most deprived 10% of LSOAs)',
                        'Employment Decile (where 1 is most deprived 10% of LSOAs)',
                        'Education, Skills and Training Decile (where 1 is most deprived 10% of LSOAs)',
                        'Health Deprivation and Disability Decile (where 1 is most deprived 10% of LSOAs)',
                        'Crime Decile (where 1 is most deprived 10% of LSOAs)',
                        'Barriers to Housing and Services Decile (where 1 is most deprived 10% of LSOAs)',
                        'Living Environment Decile (where 1 is most deprived 10% of LSOAs)',
                        'Income Deprivation Affecting Children Index (IDACI) Decile (where 1 is most deprived 10% of LSOAs)',
                        'Income Deprivation Affecting Older People (IDAOPI) Decile (where 1 is most deprived 10% of LSOAs)',
                        'Children and Young People Sub-domain Decile (where 1 is most deprived 10% of LSOAs)',
                        'Adult Skills Sub-domain Decile (where 1 is most deprived 10% of LSOAs)',
                        'Geographical Barriers Sub-domain Decile (where 1 is most deprived 10% of LSOAs)',
                        'Wider Barriers Sub-domain Decile (where 1 is most deprived 10% of LSOAs)',
                        'Indoors Sub-domain Decile (where 1 is most deprived 10% of LSOAs)',
                        'Outdoors Sub-domain Decile (where 1 is most deprived 10% of LSOAs)']
        
        iodDF = pd.read_csv(self.iodFile, usecols=columnsToLoad, compression='gzip')
        return iodDF