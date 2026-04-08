"""Input validation helpers."""
from pathlib import Path

ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp"}


def validate_image_path(path_str: str) -> Path:
    """Validate that a path exists and is a supported image file."""
    if not path_str or not isinstance(path_str, str):
        raise ValueError("Image path must be a non-empty string.")

    path = Path(path_str)

    if not path.exists():
        raise ValueError(f"Image path does not exist: {path}")
    if not path.is_file():
        raise ValueError(f"Image path is not a file: {path}")
    if path.suffix.lower() not in ALLOWED_IMAGE_EXTENSIONS:
        raise ValueError(
            f"Unsupported image extension '{path.suffix}'. "
            f"Allowed: {sorted(ALLOWED_IMAGE_EXTENSIONS)}"
        )

    return path
