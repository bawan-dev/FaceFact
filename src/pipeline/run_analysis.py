"""Minimal analysis pipeline (metadata only)."""
from src.data.image_loader import load_image_rgb


def analyze_image_metadata(path_str: str) -> dict[str, int]:
    """
    Load an image and return basic metadata (height, width, channels).
    """
    image = load_image_rgb(path_str)

    height, width = image.shape[0], image.shape[1]
    channels = 1 if image.ndim == 2 else image.shape[2]

    return {
        "height": height,
        "width": width,
        "channels": channels,
    }