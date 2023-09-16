from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def open_map():
    pass

if __name__ == "__main__":
    app.run(debug=True)
    
