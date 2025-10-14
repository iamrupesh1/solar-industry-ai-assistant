from PIL import Image
import numpy as np
import cv2
from .helpers import convert_orientation

def analyze_image(image_file):
    """
    Analyze satellite rooftop image to extract metrics:
    area, usable area ratio, orientation, shading, and quality.

    Args:
        image_file: Uploaded image file object
    Returns:
        dict with detected_area_m2, usable_ratio, orientation, shading_factor, image_quality
    """

    # Load image with PIL
    img = Image.open(image_file).convert('RGB')
    img_np = np.array(img)

    # Placeholder: dummy sample values for demo
    detected_area_m2 = 1000.0
    usable_ratio = 0.58
    orientation_angle = 135  # degrees, e.g. SE
    shading_factor = 0.42
    image_quality = "Good"

    orientation = convert_orientation(orientation_angle)

    return {
        'detected_area_m2': detected_area_m2,
        'usable_ratio': usable_ratio,
        'orientation': orientation,
        'shading_factor': shading_factor,
        'image_quality': image_quality
    }
