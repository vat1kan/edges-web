import cv2
import traceback
import numpy as np
from flask import Flask, render_template, request
from tools import edge_detection, noised_hed, noised_pidinet

app = Flask(__name__)

@app.route("/")
def about():
    return render_template("about.html")

@app.route('/pidinet', methods=['GET', 'POST'])
def pidinet():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('file')
        noise_check = request.form.get('noise_check')
        metrics_calculation = request.form.get('calculate_metrics')
        
        if noise_check and metrics_calculation:
            getNoiseType = request.form.get('noise_type')
            getNoiseParam = float(request.form.get('noise_parameter'))
            gts = request.files.getlist('ground_truth')
            gt_arrays = [cv2.imdecode(np.frombuffer(gt.read(), np.uint8), cv2.IMREAD_UNCHANGED) for gt in gts]
            return render_template('result.html', results=noised_pidinet(uploaded_images=uploaded_files, noise_type=getNoiseType, noise_param=getNoiseParam, gt=gt_arrays))
        elif noise_check:
            getNoiseType = request.form.get('noise_type')
            getNoiseParam = float(request.form.get('noise_parameter'))
            return render_template('result.html', results=noised_pidinet(uploaded_images=uploaded_files, noise_type=getNoiseType, noise_param=getNoiseParam, gt=None))
        elif metrics_calculation:
            gts = request.files.getlist('ground_truth')
            gt_arrays = [cv2.imdecode(np.frombuffer(gt.read(), np.uint8), cv2.IMREAD_UNCHANGED) for gt in gts]
            return render_template('result.html', results=edge_detection(method="PiDiNet", uploaded_images=uploaded_files, gt=gt_arrays))

        return render_template('result.html', results=edge_detection(method="PiDiNet",uploaded_images=uploaded_files,gt=None))
    
    return render_template('form.html',method="PiDiNet")
        

@app.route('/hed',methods=['GET','POST'])
def hed_evaluating():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('file')
        noise_check = request.form.get('noise_check')
        metrics_calculation = request.form.get('calculate_metrics')

        if noise_check and metrics_calculation:
            gts = request.files.getlist('ground_truth')
            gt_arrays = [cv2.imdecode(np.frombuffer(gt.read(), np.uint8), cv2.IMREAD_UNCHANGED) for gt in gts]
            getNoiseType = request.form.get('noise_type')
            getNoiseParam = float(request.form.get('noise_parameter'))
            return render_template('result.html', results=noised_hed(uploaded_images=uploaded_files,noise_type=getNoiseType,noise_param=getNoiseParam,gt=gt_arrays))
        elif noise_check:
            getNoiseType = request.form.get('noise_type')
            getNoiseParam = float(request.form.get('noise_parameter'))
            return render_template('result.html', results=noised_hed(uploaded_images=uploaded_files,noise_type=getNoiseType,noise_param=getNoiseParam,gt=None))
        elif metrics_calculation:
            gts = request.files.getlist('ground_truth')
            gt_arrays = [cv2.imdecode(np.frombuffer(gt.read(), np.uint8), cv2.IMREAD_UNCHANGED) for gt in gts]
            return render_template('result.html', results=edge_detection("HED",uploaded_images=uploaded_files,gt=gt_arrays))

        return render_template('result.html', results=edge_detection("HED",uploaded_images=uploaded_files,gt=None))
    
    return render_template('form.html',method = "HED")

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    tb = traceback.format_exc()
    tb_lines = traceback.format_exc().split('\n')
    error = tb_lines[-2]
    error_log = tb_lines[-3].strip()
    message = {
        'error':error,
        'error_log':error_log
    }
    return render_template('traceback.html', traceback=message), 500

if __name__ == '__main__':
    app.run(debug=True)