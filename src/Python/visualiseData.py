import plotly.express as px

class visualiseData:
    def __init__(self, postcodeMap):
        self.postcodeMap = postcodeMap
    def choroplethMap(self):
        geojson = 'C:\\Users\\matth\\MyScripts\\Data\\checkMyPostcode\\data\\lsoa.geojson'
        fig = px.choropleth(self.postcodeMap,
                            featureidkey='properties.LSOA11CD',
                            locations='LSOA',
                            geojson=geojson)
        fig.show()