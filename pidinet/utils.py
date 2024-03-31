"""
Utility functions for training

Author: Zhuo Su, Wenzhe Liu
Date: Aug 22, 2020
"""

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

import os
from skimage.transform import resize

import torch

def load_checkpoint(args, running_file):
    model_dir = os.path.join(os.path.dirname(__file__), 'trained_models')
    latest_filename = os.path.join(model_dir, 'latest.txt')
    model_filename = os.path.join(model_dir, 'table5_pidinet.pth')
    state = None
    try:
        if os.path.exists(model_filename):
            state = torch.load(model_filename, map_location='cpu')
        else:
            print(f"Checkpoint file '{model_filename}' does not exist.")
    except Exception as e:
        print(f"Error loading checkpoint: {e}")
    return state
