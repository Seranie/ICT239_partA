from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", pageTitle="About")

@app.route('/tours')
def tours():
    return render_template('tours.html', pageTitle="Tours", totalNumberOfTours=10)

if __name__ == '__main__':
    app.run(debug=True)