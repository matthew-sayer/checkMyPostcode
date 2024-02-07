import pandas
class retrieveDataByPostcode:
    def getPostcodeDataFromMap(postcode, postcodeMap):
        decileData = postcodeMap.loc[postcodeMap['PCD'] == postcode]
        return decileData