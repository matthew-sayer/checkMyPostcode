import pandas as pd

class getPostcodeData:
    #manual mapping of postcode to LSOA code (unused currently)
    def getPostcodeData(postcode, centroidsDF, iodDF):
        #retrieve the LSOA code for the postcode entered
        lsoaCode = centroidsDF.loc[centroidsDF['PCD'] == postcode, 'LSOA01'].values[0]
        #get the decile data for the LSOA code
        decileData = iodDF.loc[iodDF['LSOA code (2011)'] == lsoaCode].copy()
        decileData['Postcode'] = postcode
        return decileData
    def createPostcodeMap(centroidsDF, iodDF):
        #rename column to match
        centroidsDF = centroidsDF.rename(columns={'LSOA01': 'LSOA'})
        iodDF = iodDF.rename(columns={'LSOA code (2011)': 'LSOA'})
        postcodeMap = pd.merge(iodDF, centroidsDF, on='LSOA', how='left')
        return postcodeMap