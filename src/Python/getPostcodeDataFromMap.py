import pandas
class retrieveDataByPostcode:
    def __init__(self, postcodeMap):
        self.postcodeMap = postcodeMap
    def getPostcodeDataFromMap(self, postcode):
        decileData = self.postcodeMap.loc[self.postcodeMap['PCD'] == postcode]
        return decileData