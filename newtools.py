import cv2
import base64
import numpy as np
from PIL import Image
from io import BytesIO
from HED.hed_edges import hed
from scipy.spatial import cKDTree
from pidinet.getEdges import PiDiNet
from skimage.util import random_noise
from sklearn.metrics import precision_score, recall_score, f1_score

def image_reader(file):
    img = Image.open(file).convert('RGB')
    return np.array(img)

def image_to_base64(img_array):
    img = Image.fromarray(img_array)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    base64_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return base64_str

def gauss(image, var=0.005):
    noisy_image = random_noise(image, mode='gaussian', var=var)
    noisy_image = np.clip(255 * noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

def impulse(image, amount=0.01):
    noisy_image = random_noise(image, mode='s&p', amount=amount)
    noisy_image = np.clip(255 * noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

def speckle(image, var=0.005):
    noisy_image = random_noise(image, mode='speckle', var=var)
    noisy_image = np.clip(255 * noisy_image, 0, 255).astype(np.uint8)
    return noisy_image

def evaluating(img, gt):
    gt_bin = (gt > 0).astype(np.uint8)
    pred_bin = (img > 0).astype(np.uint8)

    precision = round(precision_score(gt_bin.ravel(), pred_bin.ravel(), zero_division=0), 4)
    recall = round(recall_score(gt_bin.ravel(), pred_bin.ravel(), zero_division=0), 4)
    f1 = round(f1_score(gt_bin.ravel(), pred_bin.ravel(), zero_division=0), 4)

    pred_coords = np.column_stack(np.where(pred_bin == 1))
    gt_coords = np.column_stack(np.where(gt_bin == 1))

    if len(pred_coords) == 0 or len(gt_coords) == 0:
        return recall, precision, f1, 0.0

    tree = cKDTree(gt_coords)
    dists, _ = tree.query(pred_coords, k=1)
    dists_sq = dists ** 2

    alfa = 1 / 9
    fom = round(np.sum(1 / (1 + alfa * dists_sq)) / max(len(pred_coords), len(gt_coords)), 4)

    return recall, precision, f1, fom

noise_functions = {
    'gauss': gauss,
    'impulse': impulse,
    'speckle': speckle
}

def edge_detection(imgs: list, method: str, noise_type: str, noise_value: float, ground_truth: list):
    try:
        result = []

        for idx, img_file in enumerate(imgs):
            img = image_reader(img_file)

            metrics = None

            if noise_type and noise_value:
                img = noise_functions[noise_type](img, float(noise_value))

            if method == 'HED':
                edges = hed(img)
            elif method == "PiDiNet":
                edges = PiDiNet(img)
            else:
                raise ValueError(f"Unknown method: {method}")

            edges_bgr = cv2.cvtColor(np.array(edges), cv2.COLOR_RGB2BGR)

            if ground_truth and len(ground_truth) > idx:
                try:
                    gt_image = np.array(Image.open(ground_truth[idx]).convert('RGB'))
                    recall, precision, f1, fom = evaluating(np.array(edges_bgr), gt_image)
                    metrics = {'recall': recall, 'precision': precision, 'f1_score': f1, 'FOM': fom}
                except Exception as e:
                    print(f"Error processing ground truth for image {idx+1}: {e}")
                    metrics = None
            else:
                metrics = None

            result.append({
                'method': method,
                'filename': f"<b>Image {idx+1}</b> with <b>{noise_type}</b> noise (param: <b>{noise_value}</b>)" 
                            if noise_value and float(noise_value) > 0 else f"<b>Image {idx+1}</b>",
                'original_image': image_to_base64(np.array(img)),
                'edges_image': image_to_base64(edges_bgr),
                'metrics': metrics
            })

        return result

    except Exception as e:
        print(f"Error in edge_detection: {e}")
        return [] 



