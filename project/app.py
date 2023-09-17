from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/route", methods=['GET'])
def route():
    return render_template("routes.html")

@app.route("/carbon", methods=['GET'])
def carbon():
    return render_template("carbon.html")

if __name__ == "__main__":
    app.run(debug=True)
    
