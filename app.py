from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/tours')
def tours():
    return render_template('tours.html')

if __name__ == '__main__':
    app.run(debug=True)