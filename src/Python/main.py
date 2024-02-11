import ingestData as ingest
import createPostcodeMap as map
import getDecileDataByPostcode as getDecileData
import visualiseData as vis

def main(centroidsFile, iodFile):
        print("Application loading...")
        print("Loading data...")
        ingestData = ingest.IngestData(centroidsFile, iodFile)
        centroidsDF = ingestData.readCentroidsMap()
        iodDF = ingestData.readIndicesOfDeprivation()
        print("Mapping LSOA data to postcodes...")
        map_data = map.getPostcodeData(centroidsDF, iodDF)
        postcodeMapRef = map_data.createPostcodeMap()
       #print("Visualising data...")
        #vis_data = vis.visualiseData(postcodeMap)
        #vis_data.choroplethMap()
        #initialise getDecileData class
        postcodeInput = getDecileData.takePostcodeInput(postcodeMapRef)
        postcode = postcodeInput.getInput()
        decileDataInstance = getDecileData.getDecileDataForPostcode(postcodeMapRef)
        decileData = decileDataInstance.checkDecileData(postcode)
        decileDataInstance.outputDecileData(decileData)

if __name__ == "__main__":
    main('C:\\Users\\matth\\MyScripts\\temp\\ONSPD_Centroids.csv.gz', 'C:\\Users\\matth\\MyScripts\\temp\\IoD2019.csv.gz')