from flask import Flask, render_template, request
import main

homepage = 'checkMyPostcode.html'

#create a Flask instance
app = Flask(__name__, template_folder='C:\\Users\\matth\\MyScripts\\Data\\checkMyPostcode\\src\\templates')

#define a route to show as the root of the web server
def loadPostcodeMap():
    postcodeMapRef = main.main('C:\\Users\\matth\\MyScripts\\temp\\ONSPD_Centroids.csv.gz', 'C:\\Users\\matth\\MyScripts\\temp\\IoD2019.csv.gz')
    return postcodeMapRef

postcodeMapRef = loadPostcodeMap()

@app.route('/', methods=['GET', 'POST', 'PUT', 'PATCH']) #this shows that the site will be e.g. localhost:5000/
def start():
    if request.method == 'POST':
        postcode = request.form['postcode']
        decileDataInstance = main.getDecileData.getDecileDataForPostcode(postcodeMapRef)
        decileData = decileDataInstance.checkDecileData(postcode)
        result = decileDataInstance.outputDecileData(decileData).to_html()
        return render_template(homepage, result=result)
    else:
        return render_template(homepage) #renders the HTML file

if __name__ == '__main__':
    app.run()
    


