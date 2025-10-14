import numpy as np
import cv2

def extract_rooftop(img_pil):
    img = np.array(img_pil)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5,5), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    mask = np.zeros_like(gray)
    if contours:
        largest = max(contours, key=cv2.contourArea)
        cv2.drawContours(mask, [largest], -1, 255, thickness=cv2.FILLED)
    else:
        largest = None

    pixel_area = cv2.contourArea(largest) if largest is not None else 0

    # Assume 0.5m x 0.5m per pixel (adjust if known)
    pixel_to_m2 = 0.5 * 0.5
    area_m2 = pixel_area * pixel_to_m2

    mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    return mask_rgb, area_m2
