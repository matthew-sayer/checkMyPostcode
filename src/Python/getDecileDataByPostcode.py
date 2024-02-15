import pandas as pd
import json
#Here, I am creating a class to pull in the postcode map. Then, I take the postcode input and check it against the map.
#After that, I check if it matches and if it does not then I reformat it.
#If it still doesn't match, I state that the postcode was not found.
#The checkDecileData function will recursively call itself to reformat the postcode
#It will do this until it finds a match, or it still can't find one due to no valid postcode being entered

class getDecileData: 
    def __init__(self, postcodeMapRef):
        self.postcodeMap = postcodeMapRef
class takePostcodeInput(getDecileData):
    def __init__(self, postcodeMapRef):
        getDecileData.__init__(self, postcodeMapRef)

    def getInput(self):
        postcode = input('Enter a postcode: ')
        postcode = postcode.replace(' ', '')
        postcode = postcode.upper()
        return postcode

class getDecileDataForPostcode(getDecileData):
    def __init__(self, postcodeMapRef):
        getDecileData.__init__(self, postcodeMapRef)
    def getPostcodeDataFromMap(self, postcode):
        decileData = self.postcodeMap.loc[self.postcodeMap['Postcode'] == postcode]
        return decileData
    
    def checkDecileData(self, postcode):
        decileData = self.getPostcodeDataFromMap(postcode)
        if decileData.empty:
            if len(postcode) == 7:
                postcode = postcode[:4] + ' ' + postcode[4:]
                postcode = postcode.upper()
            elif len(postcode) == 6:
                postcode = postcode[:3] + ' ' + postcode[3:]
                postcode = postcode.upper()
            return self.checkDecileData(postcode)
        else:
             return decileData

    def outputDecileData(self, decileData):
            if not decileData.empty:
                return decileData
            else: 
                print('Postcode not found')