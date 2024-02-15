import pandas as pd

class getPostcodeData:
    def __init__(self, centroidsDF, iodDF):
        self.centroidsDF = centroidsDF
        self.iodDF = iodDF

    #manual mapping of postcode to LSOA code (unused currently)
    def getPostcodeData(self, postcode):
        #retrieve the LSOA code for the postcode entered
        lsoaCode = self.centroidsDF.loc[self.centroidsDF['PCD'] == postcode, 'LSOA01'].values[0]
        #get the decile data for the LSOA code
        decileData = self.iodDF.loc[self.iodDF['LSOA code (2011)'] == lsoaCode].copy()
        decileData['Postcode'] = postcode
        return decileData
    def createPostcodeMap(self):
        #rename column to match
        self.centroidsDF = self.centroidsDF.rename(columns={'LSOA01': 'LSOA'})
        self.iodDF = self.iodDF.rename(columns={'LSOA code (2011)': 'LSOA'})
        postcodeMap = pd.merge(self.iodDF, self.centroidsDF, on='LSOA', how='left')
        #drop the LSOA column
        postcodeMap = postcodeMap.drop(columns=['LSOA'])
        postcodeMap = postcodeMap.rename(columns={'PCD': 'Postcode'})
        postcodeMap = postcodeMap[['Postcode'] + [col for col in postcodeMap.columns if col != 'Postcode']]
        return postcodeMap