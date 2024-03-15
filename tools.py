import base64
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
from HED.hed_edges import hed
from pidinet.getEdges import PiDiNet

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

def edge_detection(method, uploaded_images):
    detection_result = []
    for image in uploaded_images:
        if image.filename != '':
            filename = image.filename
            if method == 'PiDiNet':
                image_data, image_bytes = pidinet_reader(image)
                edge_image = PiDiNet(image_data,image_bytes)
            
            original_image = image_reader(image)
            if method == "HED":
                if isinstance(original_image, str):
                    image = base64.b64decode(original_image)
                    image = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
                edge_image = hed(image)
    
            edges_entry = {
                'filename':filename,
                'original_image':original_image,
                'edges_image':edge_image
            }
            detection_result.append(edges_entry)
    
    return detection_result

def noised_pidinet(uploaded_images,noise_type,noise_param):
    detection_result = []
    for image in uploaded_images:
        filename = image.filename
        image_data, image_bytes = pidinet_reader(image)
        image_array = np.array(image_bytes)

        # if noise_type == "gauss":
        #     image_array = gauss(image=image_array, std_dev=noise_param)
        # elif noise_type == "impulse":
        #     image = impulse(image=image_array, probability=noise_param)
        # elif noise_type == "speckle":
        #     image = speckle(image=image_array, intensity=noise_param)

        if noise_type == "gauss":
            image_array = gauss(image=image_array, std_dev=noise_param)
        elif noise_type == "impulse":
            image_array = impulse(image=image_array, probability=noise_param)
        elif noise_type == "speckle":
            image_array = speckle(image=image_array, intensity=noise_param)


        edge_image = PiDiNet(image_data,Image.fromarray(image_array))

        edges_entry = {
                    'filename':f"{filename} with {noise_type} noise (param {noise_param})",
                    'original_image': base64Convert(image_array),
                    'edges_image':edge_image
                }
        detection_result.append(edges_entry)
    
    return detection_result

def noised_hed(uploaded_images,noise_type,noise_param):
    detection_result = []
    for image in uploaded_images:
        image_name = image.filename
        image_data = image.read()
        image = np.array(Image.open(BytesIO(image_data)).convert('RGB'))

        if noise_type == "gauss":
            image = gauss(image=image, std_dev=noise_param)
        elif noise_type == "impulse":
            image = impulse(image=image, probability=noise_param)
        elif noise_type == "speckle":
            image = speckle(image=image, intensity=noise_param)

        edge_image = hed(image)

        edges_entry = {
                    'filename':f"{image_name} with {noise_type} noise (param {noise_param})",
                    'original_image': base64Convert(image),
                    'edges_image':edge_image
                }
        detection_result.append(edges_entry)
    return detection_result

def gauss(image,std_dev):
    mean = 0
    rows, cols, chanels = image.shape
    gaussian_noise = np.random.normal(mean, std_dev, (rows, cols, chanels))
    noisy_image = cv2.add(np.float32(image), np.float32(gaussian_noise), dtype=cv2.CV_32F)
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

def impulse(image, probability):
    noisy_image = np.copy(image)
    noise_mask = np.random.rand(*image.shape[:2]) < probability
    noisy_image[noise_mask] = 0
    noisy_image[noise_mask ^ 1] = 255
    return noisy_image

def speckle(image, intensity):
    row, col, ch = image.shape
    gauss = np.random.randn(row, col, ch)
    noisy = image + image * gauss * intensity
    noisy_image = np.clip(noisy, 0, 255).astype(np.uint8)

    return noisy_image