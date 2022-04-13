import imp
from flask import Flask, jsonify, render_template, request
import csv

app = Flask(__name__)

@app.route('/data1')
def home():
    data = [
        ("01-03-2017",0.7443)
        ("01-04-2017",0.751)
        ("01-05-2017",0.7551)
        ("01-06-2017",0.7568)
        ("01-07-2017",0.7553)
        
    ]
    labels = [Row[0] for row in data]
    Values = [Row[1] for row in data]

    return render_template("graph.html", labels=labels, Values=Values)

@app.route('/test', methods=['GET', 'POST'])
def root(): 
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        results = []
        
        user_csv = request.form.get('FXCADUSD').split('\n')
        reader = csv.DictReader(user_csv)
        
        for row in reader:
            results.append(dict(row))

        fieldnames = [key for key in results[0].keys()]

        return render_template('home.html', results=results, fieldnames=fieldnames, len=len)


@app.route('/')
def index():
    return render_template("index.html")
    

@app.route('/google-charts/pie-chart')
def google_pie_chart():
    data = {'Task' : 'Hours per Day', 'Work':11, 'Eat' :2, 'Commute':2, 'Watching TV':2, 'Sleeping':7}
    return render_template('pie-chart.html', data=data)



if __name__ == "__main__":
    app.run()