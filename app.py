import traceback
from flask import Flask, render_template, request
from tools import edge_detection, comparison

app = Flask(__name__)

@app.route("/")
def about():
    return render_template("about.html")

@app.route('/pidinet', methods=['GET', 'POST'])
def pidinet():
    if request.method == 'POST':

        file_list = request.files.getlist('file') or []
        ground_truth_raw = request.files.getlist('ground_truth') or []

        if not file_list:
            return "No input files uploaded", 400

        data = edge_detection(
            imgs=file_list,
            method='PiDiNet',
            noise_type = request.form.get('noise_type') or None,
            noise_value = request.form.get('noise_value'),
            ground_truth = [f for f in ground_truth_raw if f and f.filename]
        )

        return render_template('result.html', result=data)

    return render_template('form.html', method="PiDiNet")


@app.route('/hed',methods=['GET','POST'])
def hed():
    if request.method == 'POST':

        file_list = request.files.getlist('file') or []
        ground_truth_raw = request.files.getlist('ground_truth') or []

        if not file_list:
            return "No input files uploaded", 400

        data = edge_detection(
            imgs=file_list,
            method='HED',
            noise_type = request.form.get('noise_type') or None,
            noise_value = request.form.get('noise_value'),
            ground_truth = [f for f in ground_truth_raw if f and f.filename]
        )

        return render_template('result.html', result=data)

    return render_template('form.html', method="HED")

@app.route('/comparison',methods=['GET','POST'])
def methods_comparison():
    if request.method == 'POST':

        file_list = request.files.getlist('file') or []
        ground_truth_raw = request.files.getlist('ground_truth') or []

        if not file_list:
            return "No input files uploaded", 400

        data = comparison(
            imgs=file_list,
            method='Comparison',
            noise_type = request.form.get('noise_type') or None,
            noise_value = request.form.get('noise_value'),
            ground_truth = [f for f in ground_truth_raw if f and f.filename]
        )

        return render_template('result.html', result=data)

    return render_template('form.html', method="Comparison")


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    tb = traceback.format_exc()
    message = {'traceback': tb}
    return render_template('traceback.html', traceback=message['traceback']), 500

if __name__ == '__main__':
    app.run(debug=True)