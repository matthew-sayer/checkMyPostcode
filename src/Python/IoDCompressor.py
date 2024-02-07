import pandas as pd 
#Used in preparation before git commit due to file size limitations
class compress:
    def compress_data(file_path):
        df = pd.read_csv(file_path)j
        df.to_csv(file_path + '.gz', compression='gzip')
        return df
        
compress.compress_data('C:\\Users\\matth\\MyScripts\\Data\\checkMyPostcode\\data\\IoD2019.csv')
print('IoD2019.csv compressed')
compress.compress_data('C:\\Users\\matth\\MyScripts\\Data\\checkMyPostcode\\data\\ONSPD_Centroids.csv')
print('ONSPD_Centroids.csv compressed')


