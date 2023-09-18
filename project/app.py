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
    if request == "POST":
        car_brand = request.form.get('Car Brand: ')
        car_type = request.form.get('Car Type: ')
        miles_driven = float(request.form.get('miles_driven'))
        fuel_per_gallon = float(request.form.get('fuel_per_gallon'))
        return render_template("carbon.html", car_brand=car_brand, car_type = car_type)


    else:
        return render_template("carbon.html")

if __name__ == "__main__":
    app.run(debug=True)
    
