import cv2
import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score
import base64

def evaluating(edges, gt):
    if isinstance(edges, str):
        # Decode base64 string to bytes and convert to NumPy array
        decoded_edges = np.frombuffer(base64.b64decode(edges), dtype=np.uint8)
        edges = cv2.imdecode(decoded_edges, cv2.IMREAD_GRAYSCALE)

    # Convert ground truth image to grayscale if it has multiple channels
    if len(gt.shape) > 2:
        gt = cv2.cvtColor(gt, cv2.COLOR_BGR2GRAY)

    # Ensure both arrays have the same shape
    print("Shapes before resizing:", edges.shape, gt.shape)  # Add this line for debugging
    if edges.shape != gt.shape:
        raise ValueError("The 'edges' and 'gt' arrays must have the same shape.")

    # Rest of the function remains unchanged
    detected_edges = cv2.threshold(edges, 0, 255, cv2.THRESH_BINARY)[1]
    ground_truth_binary = (gt > 0).astype(np.uint8)
    detected_edges_binary = (detected_edges > 0).astype(np.uint8)
    precision = np.round(precision_score(ground_truth_binary.flatten(), detected_edges_binary.flatten()), 5)
    recall = np.round(recall_score(ground_truth_binary.flatten(), detected_edges_binary.flatten()), 5)
    f1 = np.round(f1_score(ground_truth_binary.flatten(), detected_edges_binary.flatten()), 5)
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
    FOM = np.round(np.sum(1 / (1 + alfa * d)) / max(m, n), 4)

    return recall, precision, f1, FOM



