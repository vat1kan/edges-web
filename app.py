from flask import Flask, render_template, request
from HED import hed_edges  # Assuming hed_edges is the function for edge detection
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

    for file in uploaded_files:
        if file:
            file_name = file.filename
            image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
            hed = hed_edges(image)  # Assuming hed_edges is the function for edge detection
            hed_encoded = base64.b64encode(cv2.imencode('.png', hed)[1]).decode('utf-8')

            result_entry = {
                'file_name': file_name,
                'original_image': base64.b64encode(cv2.imencode('.png', image)[1]).decode('utf-8'),
                'edge_result': hed_encoded
            }

            hed_results.append(result_entry)

    return render_template('result.html', hed_list=hed_results)

if __name__ == '__main__':
    app.run(debug=True)
