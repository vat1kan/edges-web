import cv2
import base64
import numpy as np
from PIL import Image
from io import BytesIO
from HED.hed_edges import hed
from pidinet.getEdges import PiDiNet
from skimage.util import random_noise
from sklearn.metrics import precision_score, recall_score, f1_score

def image_reader(uploaded_file):
    uploaded_file.seek(0)
    file_content = uploaded_file.read()
    if not file_content:
        print('The file is empty')
        return None
    image = cv2.imdecode(np.frombuffer(file_content, np.uint8), cv2.IMREAD_COLOR)
    if image is None:
        print('Failed to decode image')
        return None
    decoded_image = base64.b64encode(cv2.imencode('.png', image)[1]).decode('utf-8')
    return decoded_image

def pidinet_reader(image):
        image_data = image.read()
        image_bytes = Image.open(BytesIO(image_data)).convert('RGB')
        return image_data, image_bytes

def base64Convert(image_array):
    pil_image = Image.fromarray(image_array)
    buffered = BytesIO()
    pil_image.save(buffered, format="png")
    encoded_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return encoded_image

def getBase64Image(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

def edge_detection(method, uploaded_images, gt):

    detection_result = []

    for idx, image in enumerate(uploaded_images):
        if image.filename != '':
            filename = image.filename
            
            if method == 'PiDiNet':
                image_data, image_bytes = pidinet_reader(image)
                edge_image = PiDiNet(image_data,image_bytes)
                if gt != None:
                    recall, precision, f1, fom = evaluating(np.array(edge_image),gt[idx])
                    metrics = {'recall': recall, 'precision': precision, 'f1_score': f1, 'FOM': fom}

            original_image = image_reader(image)
            if method == "HED":
                if isinstance(original_image, str):
                    image = base64.b64decode(original_image)
                    image = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
                edge_image = hed(image)
                if gt != None:
                    recall, precision, f1, fom = evaluating(np.array(edge_image),gt[idx])
                    metrics = {'recall': recall, 'precision': precision, 'f1_score': f1, 'FOM': fom}
    
            edges_entry = {
                'method':method,
                'filename':filename,
                'original_image':original_image,
                'edges_image':base64Convert(edge_image) if method=='HED' else getBase64Image(edge_image),
                'metrics': metrics if gt != None else None
            }
            detection_result.append(edges_entry)
    
    return detection_result

def noised_pidinet(uploaded_images,noise_type,noise_param, gt):
    detection_result = []
    for idx, image in enumerate(uploaded_images):
        filename = image.filename
        image_data, image_bytes = pidinet_reader(image)
        image_array = np.array(image_bytes)

        if noise_type == "gauss":
            image_array = gauss(image=image_array, var=noise_param)
        elif noise_type == "impulse":
            image_array = impulse(image=image_array, var=noise_param)
        elif noise_type == "speckle":
            image_array = speckle(image=image_array, var=noise_param)

        edge_image = PiDiNet(image_data,Image.fromarray(image_array))
        if gt != None:
            recall, precision, f1, fom = evaluating(np.array(edge_image),gt[idx])
            metrics = {'recall': recall, 'precision': precision, 'f1_score': f1, 'FOM': fom}

        edges_entry = {
                    'method':"PiDiNet",
                    'filename':f"{filename} with {noise_type} noise (param {noise_param})",
                    'original_image': base64Convert(image_array),
                    'edges_image': getBase64Image(edge_image),
                    'metrics': metrics if gt != None else None
                }
        detection_result.append(edges_entry)
    
    return detection_result

def noised_hed(uploaded_images,noise_type,noise_param,gt):
    detection_result = []
    for idx, image in enumerate(uploaded_images):
        image_name = image.filename
        image_data = image.read()
        image = np.array(Image.open(BytesIO(image_data)).convert('RGB'))

        if noise_type == "gauss":
            image = gauss(image=image, var=noise_param)
        elif noise_type == "impulse":
            image = impulse(image=image, var=noise_param)
        elif noise_type == "speckle":
            image = speckle(image=image, var=noise_param)

        edge_image = hed(image)
        if gt != None:
            recall, precision, f1, fom = evaluating(np.array(edge_image),gt[idx])
            metrics = {'recall': recall, 'precision': precision, 'f1_score': f1, 'FOM': fom}

        edges_entry = {
                    'method':"HED",
                    'filename':f"{image_name} with {noise_type} noise (param {noise_param})",
                    'original_image': base64Convert(image),
                    'edges_image':base64Convert(edge_image),
                    'metrics': metrics if gt != None else None
                }
        detection_result.append(edges_entry)
        
    return detection_result

def gauss(image, var):
    noisy_image = random_noise(image, mode='gaussian', var=var)
    noisy_image = (255 * noisy_image).astype(np.uint8)
    return noisy_image

def impulse(image, var):
    noisy_image = random_noise(image, mode='s&p', amount=var)
    noisy_image = (255 * noisy_image).astype(np.uint8)
    return noisy_image

def speckle(image, var):
    noisy_image = random_noise(image, mode='speckle', var=var)
    noisy_image = (255 * noisy_image).astype(np.uint8)
    return noisy_image

def evaluating(edges, gt):
    ground_truth_binary = (gt > 0).astype(np.uint8)
    edges_numeric = np.asarray(edges, dtype=np.float32)
    detected_edges_binary = (edges_numeric > 0).astype(np.uint8)
    detected_edges_binary = (edges > 0).astype(np.uint8)
    precision = np.round(precision_score(ground_truth_binary.flatten(), detected_edges_binary.flatten()),4)
    recall = np.round(recall_score(ground_truth_binary.flatten(), detected_edges_binary.flatten()),4)
    f1 = np.round(f1_score(ground_truth_binary.flatten(), detected_edges_binary.flatten()),4)

    boundary_pixels_A = np.column_stack(np.where(edges == 1))
    object_pixels_GT = np.column_stack(np.where(gt == 1))
    m = len(boundary_pixels_A)
    n = len(object_pixels_GT)
    if m == 0 or n == 0:
        return 0, 0, 0, 0
    d = np.zeros(m)
    for i in range(m):
        dist = np.sum((boundary_pixels_A[i, :] - object_pixels_GT) ** 2, axis=1)
        d[i] = np.min(dist)
    alfa = 1 / 9
    FOM = np.round(np.sum(1 / (1 + alfa * d)) / max(m, n),4)

    return recall, precision, f1, FOM