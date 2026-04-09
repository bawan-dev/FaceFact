"""Under-eye darkness analysis (simple heuristic)."""
from __future__ import annotations

import cv2
import numpy as np


def estimate_under_eye_darkness(image_rgb: np.ndarray) -> dict[str, float]:
    """
    Estimate under-eye darkness by comparing brightness in a rough under-eye
    band to a reference band on the lower face.

    Returns a dictionary with:
    - under_eye_mean: average brightness in the under-eye region (0-255)
    - reference_mean: average brightness in the reference region (0-255)
    - darkness_score: 0.0 to 1.0 (higher = darker under-eye vs reference)
    """
    if not isinstance(image_rgb, np.ndarray):
        raise ValueError("image_rgb must be a numpy array.")
    if image_rgb.ndim not in (2, 3):
        raise ValueError("image_rgb must be a 2D or 3D array.")
    if image_rgb.ndim == 3 and image_rgb.shape[2] != 3:
        raise ValueError("image_rgb must have 3 channels (RGB).")

    height, width = image_rgb.shape[0], image_rgb.shape[1]
    if height < 40 or width < 40:
        raise ValueError("image_rgb is too small for under-eye analysis.")

    # Convert to grayscale for brightness analysis
    if image_rgb.ndim == 3:
        gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
    else:
        gray = image_rgb

    # Rough under-eye region (relative coordinates)
    ue_y1 = int(height * 0.35)
    ue_y2 = int(height * 0.50)
    ue_x1 = int(width * 0.25)
    ue_x2 = int(width * 0.75)

    # Reference region (lower mid-face)
    ref_y1 = int(height * 0.60)
    ref_y2 = int(height * 0.80)
    ref_x1 = int(width * 0.25)
    ref_x2 = int(width * 0.75)

    if ue_y2 <= ue_y1 or ue_x2 <= ue_x1 or ref_y2 <= ref_y1 or ref_x2 <= ref_x1:
        raise ValueError("Computed regions are invalid. Image may be too small.")

    under_eye_region = gray[ue_y1:ue_y2, ue_x1:ue_x2]
    reference_region = gray[ref_y1:ref_y2, ref_x1:ref_x2]

    under_eye_mean = float(np.mean(under_eye_region))
    reference_mean = float(np.mean(reference_region))

    # Darkness score: how much darker the under-eye region is vs reference
    darkness_raw = (reference_mean - under_eye_mean) / 255.0
    darkness_score = max(0.0, min(1.0, darkness_raw))

    return {
        "under_eye_mean": under_eye_mean,
        "reference_mean": reference_mean,
        "darkness_score": darkness_score,
    }
