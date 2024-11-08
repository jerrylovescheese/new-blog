from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

# Route for the home page


@app.route('/')
def home():
    return render_template('index.html')

# Route for other static pages


@app.route('/page/<path:path>')
def page(path):
    return render_template('page.html', path=path)


if __name__ == '__main__':
    app.run(debug=True)
