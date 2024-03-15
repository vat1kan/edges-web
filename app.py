from flask import Flask, render_template, request
from pidinet.getEdges import PiDiNet, get_base64_image
from HED.hed_edges import hed
from tools import *

app = Flask(__name__)

@app.route('/pidinet', methods=['GET', 'POST'])
def pidinet():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('file')
        noise_check = request.form.get('noise_check')

        if noise_check:
            getNoiseType = request.form.get('noise_type')
            getNoiseParam = float(request.form.get('noise_parameter'))
            return render_template('result.html', results=noised_pidinet(uploaded_images=uploaded_files,noise_type=getNoiseType,noise_param=getNoiseParam))
        
        return render_template('result.html', results=edge_detection(method="PiDiNet",uploaded_images=uploaded_files))
    return render_template('index.html')
        

@app.route('/hed',methods=['GET','POST'])
def hed_evaluating():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('file')
        noise_check = request.form.get('noise_check')

        if noise_check:
            getNoiseType = request.form.get('noise_type')
            getNoiseParam = float(request.form.get('noise_parameter'))
            return render_template('result.html', results=noised_hed(uploaded_images=uploaded_files,noise_type=getNoiseType,noise_param=getNoiseParam))
        
        return render_template('result.html', results=edge_detection("HED",uploaded_images=uploaded_files))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)