import cv2
import numpy as np

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