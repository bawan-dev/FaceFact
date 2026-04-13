from __future__ import annotations

from src.analysis.under_eye import estimate_under_eye_darkness
from src.analysis.skin_features import estimate_skin_features
from src.data.image_loader import load_image_rgb
from src.pipeline.run_analysis import analyze_image_metadata


def build_report(path_str: str) -> dict:
    """
    Load an image and return a structured analysis report.
    """
    image_rgb = load_image_rgb(path_str)

    metadata = analyze_image_metadata(path_str)
    under_eye = estimate_under_eye_darkness(image_rgb)
    skin = estimate_skin_features(image_rgb)

    return {
        "metadata": metadata,
        "under_eye": under_eye,
        "skin_features": skin,
    }