import pandas as pd


class AnalyseData:
    def __init__(self, postcodeMapRef):
        self.postcodeMapRef = postcodeMapRef

    def exploratoryAnalysis(self):
        descriptions = self.postcodeMapRef.describe().round(2)
        #include numeric columns only
        correlations = self.postcodeMapRef.corr(numeric_only=True)
        return descriptions, correlations