from flask import Flask, render_template, request
import draw_curve as dc

app = Flask(__name__)


# TODO: Add clear function
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        sequence = request.form['sequence']
        result = dc.draw_curve(sequence)
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
