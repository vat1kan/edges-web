import cv2
import numpy as np
import base64
import os

def hed(image):
    H, W = None, None  # Initialize H and W
    try:
        if image is not None:  # Check if image is not None before accessing its shape
            (H, W) = image.shape[:2]  # Assign H and W here
        
            blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(W, H), swapRB=False, crop=False)

            prototxt_path = os.path.join(os.path.dirname(__file__), 'model', 'deploy.prototxt')
            caffemodel_path = os.path.join(os.path.dirname(__file__), 'model', 'hed_pretrained_bsds.caffemodel')

            net = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)
            net.setInput(blob)
            
            hed = net.forward()
            hed = cv2.resize(hed[0, 0], (W, H))
            hed = (255 * hed).astype("uint8")
            
            hed_colored = cv2.cvtColor(hed, cv2.COLOR_GRAY2BGR)
            
            success, encoded_image = cv2.imencode('.png', hed_colored)
            if not success:
                raise Exception("Could not encode the edge-detected image.")

            encoded_edges_image = base64.b64encode(encoded_image).decode('utf-8')
            
            return encoded_edges_image
        else:
            raise Exception("Decoded image is None.")
    except Exception as e:
        print("Error in hed_edgemap:", str(e))
        # Return a default image when an error occurs
        return base64.b64encode(cv2.imencode('.png', np.zeros((H or 1, W or 1, 3), dtype=np.uint8))[1]).decode('utf-8')





