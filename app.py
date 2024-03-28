from flask import Flask, render_template, request
from tools import *

app = Flask(__name__)

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
            gt_arrays = [cv2.imdecode(np.fromstring(gt.read(), np.uint8), cv2.IMREAD_UNCHANGED) for gt in gts]
            return render_template('result.html', results=noised_pidinet(uploaded_images=uploaded_files, noise_type=getNoiseType, noise_param=getNoiseParam, gt=gt_arrays))
        elif noise_check:
            getNoiseType = request.form.get('noise_type')
            getNoiseParam = float(request.form.get('noise_parameter'))
            return render_template('result.html', results=noised_pidinet(uploaded_images=uploaded_files, noise_type=getNoiseType, noise_param=getNoiseParam, gt=None))
        elif metrics_calculation:
            gts = request.files.getlist('ground_truth')
            gt_arrays = [cv2.imdecode(np.fromstring(gt.read(), np.uint8), cv2.IMREAD_UNCHANGED) for gt in gts]
            return render_template('result.html', results=edge_detection(method="PiDiNet", uploaded_images=uploaded_files, gt=gt_arrays))

        return render_template('result.html', results=edge_detection(method="PiDiNet",uploaded_images=uploaded_files,gt=None))
    
    return render_template('index.html')
        

@app.route('/hed',methods=['GET','POST'])
def hed_evaluating():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('file')
        noise_check = request.form.get('noise_check')
        metrics_calculation = request.form.get('calculate_metrics')

        if noise_check and metrics_calculation:
            gts = request.files.getlist('ground_truth')
            gt_arrays = [cv2.imdecode(np.fromstring(gt.read(), np.uint8), cv2.IMREAD_UNCHANGED) for gt in gts]
            getNoiseType = request.form.get('noise_type')
            getNoiseParam = float(request.form.get('noise_parameter'))
            return render_template('result.html', results=noised_hed(uploaded_images=uploaded_files,noise_type=getNoiseType,noise_param=getNoiseParam,gt=gt_arrays))
        elif noise_check:
            getNoiseType = request.form.get('noise_type')
            getNoiseParam = float(request.form.get('noise_parameter'))
            return render_template('result.html', results=noised_hed(uploaded_images=uploaded_files,noise_type=getNoiseType,noise_param=getNoiseParam,gt=None))
        elif metrics_calculation:
            gts = request.files.getlist('ground_truth')
            gt_arrays = [cv2.imdecode(np.fromstring(gt.read(), np.uint8), cv2.IMREAD_UNCHANGED) for gt in gts]
            return render_template('result.html', results=edge_detection("HED",uploaded_images=uploaded_files,gt=gt_arrays))

        return render_template('result.html', results=edge_detection("HED",uploaded_images=uploaded_files,gt=None))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)