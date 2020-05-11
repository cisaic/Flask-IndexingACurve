from flask import Flask, render_template, url_for, request, redirect
from curve-index import hilbert_index


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        expression = request.form['sequence']
        return render_template('index.html', result=expression)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
