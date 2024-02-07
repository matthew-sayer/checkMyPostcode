import ingestData as ingest
import createPostcodeMap as map
import getPostcodeDataFromMap as getData

def main(centroidsFile, iodFile):
        centroidsDF = ingest.IngestData.readCentroidsMap(centroidsFile)
        iodDF = ingest.IngestData.readIndicesOfDeprivation(iodFile)
        postcodeMap = map.getPostcodeData.createPostcodeMap(centroidsDF, iodDF)
        decileData = getData.retrieveDataByPostcode.getPostcodeDataFromMap('SN251RL', postcodeMap)
        print(decileData)
if __name__ == "__main__":
    main('C:\\Users\\matth\\MyScripts\\Data\\checkMyPostcode\\data\\ONSPD_Centroids.csv.gz', 'C:\\Users\\matth\\MyScripts\\Data\\checkMyPostcode\\data\\IoD2019.csv.gz')