import plotly.express as px

class visualiseData:
    def __init__(self, postcodeMap):
        self.postcodeMap = postcodeMap
    def choroplethMap(self):
        geojson = 'C:\\Users\\matth\\Documents\\combined_postcodes_swindon.geojson'
        fig = px.choropleth(self.postcodeMap,
                            featureidkey='properties.postcodes',
                            locations='PCD',
                            geojson=geojson)
        fig.show()
        html = fig.write_html('C:\\Users\\matth\\Documents\\choroplethMap.html')
        return html
    