from flask import Flask, render_template, request
from HED import hed_edges
from noise import gauss, impulse, speckle
from metrics import evaluating
import base64
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/result', methods=['POST'])
def result():
    uploaded_files = request.files.getlist('file')
    hed_results = []

    add_noise = request.form.get('add_noise')  # Check if checkbox is activated

    for file in uploaded_files:
        if file:
            file_name = file.filename
            # Convert image to a NumPy array
            image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

            # Apply noise if checkbox is activated
            if add_noise:
                noise_type = request.form.get('noise_type')
                noise_parameter = float(request.form.get('noise_parameter'))

                if noise_type == 'gauss':
                    image = gauss(image, std_dev=noise_parameter)
                elif noise_type == 'impulse':
                    image = impulse(image, noise_probability=noise_parameter)
                elif noise_type == 'speckle':
                    image = speckle(image, intensity=noise_parameter)

            hed = hed_edges(image)
            hed_encoded = base64.b64encode(cv2.imencode('.png', hed)[1]).decode('utf-8')

            result_entry = {
                'file_name': file_name,
                'original_image': base64.b64encode(cv2.imencode('.png', image)[1]).decode('utf-8'),
                'edge_result': hed_encoded
            }

            hed_results.append(result_entry)

    calculate_metrics = request.form.get('calculate_metrics')  # Check if metrics checkbox is activated

    if calculate_metrics:
        ground_truth_files = request.files.getlist('ground_truth')

        for i, gt_file in enumerate(ground_truth_files):
            if gt_file:
                # Convert ground truth image to a NumPy array
                gt_image = cv2.imdecode(np.frombuffer(gt_file.read(), np.uint8), cv2.IMREAD_COLOR)

                # Decode base64 string to bytes and convert to NumPy array
                decoded_edges = np.frombuffer(base64.b64decode(hed_results[i]['edge_result']), dtype=np.uint8)
                edges = cv2.imdecode(decoded_edges, cv2.IMREAD_GRAYSCALE)

                # Ensure both arrays have the same shape
                if edges.shape != gt_image.shape:
                    edges = cv2.resize(edges, (gt_image.shape[1], gt_image.shape[0]))

                # Assuming you have a function evaluating(edges, gt) in metrics.py
                recall, precision, f1, fom = evaluating(edges, gt_image)

                hed_results[i]['metrics'] = {
                    'recall': recall,
                    'precision': precision,
                    'f1': f1,
                    'fom': fom
                }

    return render_template('result.html', hed_list=hed_results)

if __name__ == '__main__':
    app.run(debug=True)
