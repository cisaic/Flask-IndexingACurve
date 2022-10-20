import sys

path = '/home/cisaic/Flask-IndexingACurve/flaskr'
if path not in sys.path:
    sys.path.append(path)

from flask import Flask, render_template, request
import draw_curve as dc
import draw_curve2 as dc2
import json

app = Flask(__name__)


# TODO: Add clear function
@app.route('/', methods=['POST', 'GET'])
def index():
    step_hilbert2d = dc.draw_curve('dcabac')
    step_hilbert3d = dc2.step_hilbert3D(2, 2)
    hilbert3d = dc2.draw_hilbert3D(2, 3)
    if request.method == 'POST':
        sequence = request.form['sequence']
        step_hilbert2d = dc.draw_curve(sequence)
        return render_template('index.html',
                               hilbert3d=hilbert3d,
                               step_hilbert3d=step_hilbert3d,
                               step_hilbert2d=step_hilbert2d)
    else:
        return render_template('index.html',
                               hilbert3d=hilbert3d,
                               step_hilbert3d=step_hilbert3d, step_hilbert2d=step_hilbert2d)


if __name__ == '__main__':
    app.run(debug=True)
