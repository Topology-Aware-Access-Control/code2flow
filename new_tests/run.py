import sys
import os
from pathlib import Path


FILE_DIR = Path(__file__).parent.resolve()
ROOT_DIR = FILE_DIR.parent
sys.path.append(str(ROOT_DIR))

from code2flow.engine import code2flow

code2flow([f"{FILE_DIR}/test1.py", f"{FILE_DIR}/stub.py"], f"{FILE_DIR}/out1.json", "py")