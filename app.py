from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1> This is a sample File, Welcome!</h1>"
@app.route('/about')
def about():
    return "<p>This is built locally and pushed through git.</p>"

if __name__ == '__main__':
    app.run(debug=True)