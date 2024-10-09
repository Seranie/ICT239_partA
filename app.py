from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/about')
def index():
    return render_template("about.html")

@app.route('/tours')
def tours():
    return render_template('tours.html', totalNumberOfTours=10)

if __name__ == '__main__':
    app.run(debug=True)