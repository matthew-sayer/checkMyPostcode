import ingestData as ingest
import createPostcodeMap as map
import getPostcodeDataFromMap as getData
import visualiseData as vis

def main(centroidsFile, iodFile):
        print("Application loading...")
        ingestData = ingest.IngestData(centroidsFile, iodFile)
        centroidsDF = ingestData.readCentroidsMap()
        iodDF = ingestData.readIndicesOfDeprivation()
        map_data = map.getPostcodeData(centroidsDF, iodDF)
        postcodeMap = map_data.createPostcodeMap()
        vis_data = vis.visualiseData(postcodeMap)
        vis_data.choroplethMap()
        get_data = getData.retrieveDataByPostcode(postcodeMap)

        while True:
       #get postcode input 
                postcode = input('Enter a postcode (or type "quit" to exit): ')
                #remove postcode spaces
                postcode = postcode.replace(' ', '')
                postcode = postcode.upper()
                if postcode.lower() == 'quit':
                        break
                decileData = get_data.getPostcodeDataFromMap(postcode)
                if decileData.empty:
                        if postcode.__len__() == 7:
                              #add space after 4th character
                                postcode = postcode[:4] + ' ' + postcode[4:]
                                postcode = postcode.upper()
                        elif postcode.__len__() == 6:
                                postcode = postcode[:3] + ' ' + postcode[3:]
                                postcode = postcode.upper()
                decileData = get_data.getPostcodeDataFromMap(postcode)
                if not decileData.empty:
                        print(decileData)
                else: 
                        print('Postcode not found')

if __name__ == "__main__":
    main('C:\\Users\\matth\\MyScripts\\temp\\ONSPD_Centroids.csv.gz', 'C:\\Users\\matth\\MyScripts\\temp\\IoD2019.csv.gz')