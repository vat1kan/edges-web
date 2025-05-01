import cv2
import traceback
import numpy as np
from flask import Flask, render_template, request
from newtools import edge_detection

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
def hed_evaluating():
    if request.method == 'POST':
        pass
    
    return render_template('form.html',method = "HED")

@app.route('/comparasion',methods=['GET','POST'])
def comparasion():
    pass


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    # tb = traceback.format_exc()
    # tb_lines = traceback.format_exc().split('\n')
    # error = tb_lines[-2]
    # error_log = tb_lines[-3].strip()
    # message = {
    #     'error':error,
    #     'error_log':error_log
    # }
    return render_template('traceback.html', traceback=e), 500

if __name__ == '__main__':
    app.run()