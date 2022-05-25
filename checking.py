# from pathlib import Path
# import sys
# BASE_DIR = Path(__file__).resolve().parent  # setting up the BASE_DIR to Parent directory
# FEATURE_DIR = BASE_DIR.joinpath("features").resolve() # adding the feature directory to fetch the feature file
# print(FEATURE_DIR)
# print(sys.modules[__name__])

from pathlib import Path


BASE_DIR=Path(__file__).parent.resolve()
FEATURE_DIR=BASE_DIR / "feature"
print(FEATURE_DIR)