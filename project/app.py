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
        car_brand = request.form.get('carBrand')
        car_type = request.form.get('car_type')
        miles = request.form.get('miles')
        fuel = request.form.get('fuel')
        
        return render_template("success.html", car_brand=car_brand, car_type=car_type, miles=miles, fuel=fuel)

    return render_template('carbon.html')

if __name__ == "__main__":
    app.run(debug=True)
    
