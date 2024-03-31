import cv2
import numpy as np
import os

def hed(image):
    H, W = None, None
    try:
        if image is not None:
            (H, W) = image.shape[:2]
            blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(W, H), swapRB=False, crop=False)
            prototxt_path = os.path.join(os.path.dirname(__file__), 'model', 'deploy.prototxt')
            caffemodel_path = os.path.join(os.path.dirname(__file__), 'model', 'hed_pretrained_bsds.caffemodel')
            net = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)
            net.setInput(blob)
            hed = net.forward()
            hed = cv2.resize(hed[0, 0], (W, H))
            hed = (255 * hed).astype("uint8")
            return hed
        else:
            raise Exception("Decoded image is None.")
    except Exception as e:
        print("Error in hed_edgemap:", str(e))





