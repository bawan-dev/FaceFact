"""Basic skin feature analysis (simple heuristics)."""
from __future__ import annotations

import cv2
import numpy as np


def estimate_skin_features(image_rgb: np.ndarray) -> dict[str, float]:
    """
    Estimate redness and a dryness proxy using simple pixel statistics.

    Returns:
    - redness_mean: average redness index (R - (G+B)/2)
    - redness_score: 0.0 to 1.0 (higher = more redness)
    - texture_edge_density: fraction of edge pixels in the region
    - dryness_score: 0.0 to 1.0 (higher = more texture, used as a dryness proxy)
    """
    if not isinstance(image_rgb, np.ndarray):
        raise ValueError("image_rgb must be a numpy array.")
    if image_rgb.ndim not in (2, 3):
        raise ValueError("image_rgb must be a 2D or 3D array.")
    if image_rgb.ndim == 3 and image_rgb.shape[2] != 3:
        raise ValueError("image_rgb must have 3 channels (RGB).")

    height, width = image_rgb.shape[0], image_rgb.shape[1]
    if height < 40 or width < 40:
        raise ValueError("image_rgb is too small for skin analysis.")

    # Define a rough central face region (no landmarks yet)
    y1 = int(height * 0.35)
    y2 = int(height * 0.75)
    x1 = int(width * 0.20)
    x2 = int(width * 0.80)

    region_rgb = image_rgb[y1:y2, x1:x2]

    # Redness index: R - (G+B)/2
    r = region_rgb[:, :, 0].astype(np.float32)
    g = region_rgb[:, :, 1].astype(np.float32)
    b = region_rgb[:, :, 2].astype(np.float32)

    redness_index = r - (g + b) / 2.0
    redness_mean = float(np.mean(redness_index))

    # Normalize to 0..1, clamp negatives to 0
    redness_score = max(0.0, min(1.0, redness_mean / 255.0))

    # Texture proxy using edge density
    gray = cv2.cvtColor(region_rgb, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    edge_density = float(np.mean(edges > 0))

    # Scale edge density into a 0..1 score
    dryness_score = max(0.0, min(1.0, edge_density * 10.0))

    return {
        "redness_mean": redness_mean,
        "redness_score": redness_score,
        "texture_edge_density": edge_density,
        "dryness_score": dryness_score,
    }
