"""Image loading utilities."""
from typing import Any

import cv2
import numpy as np

from src.utils.validation import validate_image_path


def load_image_rgb(path_str: str) -> np.ndarray:
    """Load an image from disk and return it as an RGB numpy array."""
    path = validate_image_path(path_str)

    image_bgr: Any = cv2.imread(str(path))
    if image_bgr is None:
        raise ValueError(f"Failed to read image file: {path}")

    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    return image_rgb
