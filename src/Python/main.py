import ingestData as ingest
import createPostcodeMap as map
import getPostcodeDataFromMap as getData

def main(centroidsFile, iodFile):
        print("Application loading...")
        centroidsDF = ingest.IngestData.readCentroidsMap(centroidsFile)
        iodDF = ingest.IngestData.readIndicesOfDeprivation(iodFile)
        postcodeMap = map.getPostcodeData.createPostcodeMap(centroidsDF, iodDF)

        while True:
       #get postcode input 
                postcode = input('Enter a postcode (or type "quit" to exit): ')
                #remove postcode spaces
                postcode = postcode.replace(' ', '')
                postcode = postcode.upper()
                if postcode.lower() == 'quit':
                        break
                decileData = getData.retrieveDataByPostcode.getPostcodeDataFromMap(postcode, postcodeMap)
                if decileData.empty:
                        if postcode.__len__() == 7:
                              #add space after 4th character
                                postcode = postcode[:4] + ' ' + postcode[4:]
                                postcode = postcode.upper()
                        elif postcode.__len__() == 6:
                                postcode = postcode[:3] + ' ' + postcode[3:]
                                postcode = postcode.upper()
                        if decileData.empty:
                                print('Postcode not found')
                decileData = getData.retrieveDataByPostcode.getPostcodeDataFromMap(postcode, postcodeMap)
                if not decileData.empty:
                        print(decileData)

if __name__ == "__main__":
    main('https://github.com/matthew-sayer/checkMyPostcode-/raw/master/data/ONSPD_Centroids.csv.gz', 'https://github.com/matthew-sayer/checkMyPostcode-/raw/master/data/IoD2019.csv.gz')