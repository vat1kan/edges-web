"""
(Generating edge maps)
Pixel Difference Networks for Efficient Edge Detection (accepted as an ICCV 2021 oral)
See paper in https://arxiv.org/abs/2108.07009

Author: Zhuo Su, Wenzhe Liu
Date: Aug 22, 2020
"""
from . import models
import torchvision.transforms as transforms
from .models.convert_pidinet import convert_pidinet
from .utils import *
from PIL import Image
import torch
import numpy as np
import argparse
import base64
from io import BytesIO

parser = argparse.ArgumentParser(description='PyTorch Pixel Difference Convolutional Networks')
args = parser.parse_args()

def PiDiNet(image_data,image):
    global args
    model = getattr(models, 'pidinet_converted')(args)
    # if uploaded_file.filename == '':
    #     print("No image uploaded.")
    #     return None
    # image_data = uploaded_file.read()
    # image = Image.open(BytesIO(image_data)).convert('RGB')

    checkpoint = load_checkpoint(args, BytesIO(image_data))
    if checkpoint is None:
        print("Checkpoint is None.")
        return None
    model.load_state_dict(convert_pidinet(checkpoint['state_dict'], 'carv4'))
    
    return get_base64_image(test(model, image))

def test(model, image):
    model.eval()

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    image_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        _, _, H, W = image_tensor.shape
        results = model(image_tensor)
        result = torch.squeeze(results[-1]).cpu().numpy()

    results_all = torch.zeros((len(results), 1, H, W))
    for i in range(len(results)):
        results_all[i, 0, :, :] = results[i]

    result_image = Image.fromarray((result * 255).astype(np.uint8))
    return result_image

def get_base64_image(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str