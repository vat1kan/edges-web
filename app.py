from flask import Flask, render_template, request
from pidinet.getEdges import PiDiNet, get_base64_image
from HED.hed_edges import hed
from tools import *

app = Flask(__name__)

# @app.route('/pidinet', methods=['GET', 'POST'])
# def upload_files():
#     if request.method == 'POST':
#         uploaded_files = request.files.getlist('file')
        
        # pidinet_edges = []
        # for uploaded_file in uploaded_files:
        #     if uploaded_file.filename != '':
        #         result_image = PiDiNet(uploaded_file)
        #         original_image = image_reader(uploaded_file)
        #         #base64_image = get_base64_image(result_image)
        #         result_entry = {
        #             'filename':uploaded_file.filename,
        #             'original_image':original_image,
        #             'edges_image':result_image#base64_image 
        #         }

        #         pidinet_edges.append(result_entry)

        # return render_template('result.html', results=pidinet_edges)

    #return render_template('index.html')

# @app.route('/hed',methods=['GET','POST'])
# def hed_evaluating():
#     if request.method == 'POST':
#         uploaded_files = request.files.getlist('file')

#         result_items = []
#         for uploaded_file in uploaded_files:
#             if uploaded_file.filename != '':
#                 original_image = image_reader(uploaded_file)
#                 edge_image = hed(original_image)
#                 result_entry = {
#                     'filename':uploaded_file.filename,
#                     'original_image':original_image,
#                     'edges_image':edge_image
#                 }

#                 result_items.append(result_entry)

#         return render_template('result.html', results=result_items)

#     return render_template('index.html')


@app.route('/pidinet', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('file')
        add_noise = request.form.get('add_noise')
        return render_template('result.html', results=edge_detection("PiDiNet",uploaded_images=uploaded_files))
    return render_template('index.html')
        

@app.route('/hed',methods=['GET','POST'])
def hed_evaluating():
    if request.method == 'POST':
        uploaded_files = request.files.getlist('file')
        return render_template('result.html', results=edge_detection("HED",uploaded_images=uploaded_files))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)