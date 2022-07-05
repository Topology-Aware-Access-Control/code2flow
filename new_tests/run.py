import sys
from pathlib import Path
import json

FILE_DIR = Path(__file__).parent.resolve()
ROOT_DIR = FILE_DIR.parent
sys.path.append(str(ROOT_DIR))

from code2flow.engine import code2flow

res = code2flow([f"{FILE_DIR}/test2.py", f"{FILE_DIR}/stub.py"], language="py", level='CRITICAL')
print(res)