from flask import Flask, render_template, request
from models.Tour import Tour

app = Flask(__name__)

@app.template_filter('formatdate')
def formatdate(date, formatString="%a, %d %b %Y"):
    return date.strftime(formatString)

@app.route('/')
@app.route('/about')
def index():
    return render_template("about.html")

@app.route('/tours')
def tours():
    Tour.createTours()
    return render_template('tours.html', tours=Tour.tours)

if __name__ == '__main__':
    app.run(debug=True)