from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/route", methods=['GET'])
def route():
    return render_template("routes.html")

@app.route("/carbon", methods=['GET', 'POST'])
def carbon():
    if request.method == "POST":
        carbrand = request.form['brand']
        cartype = request.form['type']
        miles = float(request.form["miles"])
        fuel = request.form["fuel"]
        distance = float(request.form["mileage"])

        if fuel == "Diesel":
            emissions_factor = 10.16  
        elif fuel == "Gasoline":
            emissions_factor = 8.89  
        else:
            return "Invalid fuel type"

        carbon_emissions = (miles / distance) * emissions_factor
        carbon_emissions = round(carbon_emissions, 2)
        
        return render_template("success.html", carbrand=carbrand, cartype=cartype, miles=miles, fuel=fuel, carbon_emissions=carbon_emissions)

    return render_template('carbon.html')

@app.route('/electric', methods=['GET', 'POST'])
def electric():
    ACCESS_TOKEN = "sk.eyJ1IjoicmF1bmFrbWFoZXNod2FyaSIsImEiOiJjbG1xdGduc2EwMHVjMm5teTU2cXAzdW43In0.oB7SXDSODRHUM556Yhy9VQ"
    return render_template('electric.html')


if __name__ == "__main__":
    app.run(debug=True)
    
