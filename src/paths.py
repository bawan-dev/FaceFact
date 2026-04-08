"""Project path definitions."""
from pathlib import Path

# Project root = one level above /src
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
SAMPLE_INPUTS_DIR = DATA_DIR / "sample_inputs"

OUTPUTS_DIR = PROJECT_ROOT / "outputs"
REPORTS_DIR = OUTPUTS_DIR / "reports"
DEBUG_IMAGES_DIR = OUTPUTS_DIR / "debug_images"
LOGS_DIR = OUTPUTS_DIR / "logs"
