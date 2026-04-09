# Build Log FaceFact

This is a simple, running log of how I built FaceFact.

Last updated: 2026-04-08

Stage 1 - Project setup
1. Picked the project name FaceFact.
2. Created the local project folder.
3. Set up a Python virtual environment in .venv.
4. Installed dependencies from requirements.txt.
5. Created the base folder structure.
6. Initialized Git, made the first commit, and pushed to GitHub.

Stage 2 - Core package foundation
1. Created src/__init__.py with app name and version.
2. Added src/paths.py for central path definitions.
3. Added src/config.py for basic app settings.
4. Ran small import tests to confirm everything works.

Stage 3 — Input validation and image loading
1. Added package markers for src/data and src/utils.
2. Added a validation helper for image paths.
3. Tested the validator using a fake path.
4. Added the image loader that returns RGB arrays.
5. Ran a safe test to confirm the loader fails cleanly on a missing file.

Stage 4 — Minimal pipeline metadata
1. Added src/pipeline package marker.
2. Added a pipeline function that loads an image and returns height/width channels.
3. Tested the pipeline by generating a tiny test image.

Stage 5 — Under-eye darkness (simple heuristic)
1. Added analysis package marker for src/analysis.
2. Created a basic under-eye darkness estimator using brightness comparison.
3. Tested the estimator with a synthetic image.

Stage 6 — Basic skin feature analysis
1. Added a skin_features analyzer using simple redness and texture heuristics.
2. Tested it with a synthetic image.

Notes
- I update this file as I go.
- I keep the wording simple on purpose
