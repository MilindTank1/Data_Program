from flask import Flask, jsonify, request, render_template 
app = Flask(__name__)

@app.route('/')
def index():
    return  render_template("index.html")


@app.route('/charts')
def charts():
    return render_template("pie-chart.html")

if __name__ == "__main__":
    app.run()