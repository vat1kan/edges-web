import base64
import cv2
import numpy as np
from HED.hed_edges import hed
from pidinet.getEdges import PiDiNet

def image_reader(uploaded_file):
    uploaded_file.seek(0)
    file_content = uploaded_file.read()
    
    if not file_content:
        print('empty')
        return None
    image = cv2.imdecode(np.frombuffer(file_content, np.uint8), cv2.IMREAD_COLOR)
    if image is None:
        print('failed to decode image')
        return None
    decoded_image = base64.b64encode(cv2.imencode('.png', image)[1]).decode('utf-8')
    return decoded_image

def edge_detection(method, uploaded_images):
    detection_result = []
    for image in uploaded_images:
        if image.filename != '':

            if method == 'PiDiNet':
                edge_image = PiDiNet(image)
            
            original_image = image_reader(image)
            
            if method == "HED":
                edge_image = hed(original_image)
    
            edges_entry = {
                'filename':image.filename,
                'original_image':original_image,
                'edges_image':edge_image
            }

            detection_result.append(edges_entry)
    return detection_result

def add_noise(type, image, param):
    if type=="gaussian":
        image = gauss(image=image,std_dev=param)
    elif type=="impulse":
        image = impulse(image=image,noise_probability=param)
    else:
        image = speckle(image=image, intensity=param)
    
    return image


def gauss(image,std_dev):
    mean = 0
    rows, cols, chanels = image.shape
    gaussian_noise = np.random.normal(mean, std_dev, (rows, cols, chanels))
    noisy_image = cv2.add(np.float32(image), np.float32(gaussian_noise), dtype=cv2.CV_32F)
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    
    return noisy_image

def impulse(image, noise_probability):
    noisy_image = np.copy(image)
    noise_mask = np.random.rand(*image.shape[:2]) < noise_probability
    noisy_image[noise_mask] = 0
    noisy_image[noise_mask ^ 1] = 255

    return noisy_image

def speckle(image, intensity):
    row, col, ch = image.shape
    gauss = np.random.randn(row, col, ch)
    noisy = image + image * gauss * intensity
    noisy_image = np.clip(noisy, 0, 255).astype(np.uint8)

    return noisy_image