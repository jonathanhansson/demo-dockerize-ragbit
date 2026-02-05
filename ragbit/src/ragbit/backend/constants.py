from pathlib import Path
import os

CURRENT_FILE = Path(__file__).resolve()

if os.path.exists("/app"):
    DATA_PATH = Path("/app/data")
else:
    DATA_PATH = CURRENT_FILE.parents[2] / "data"

DATA_PATH = Path(__file__).parents[1] / "data"
VECTOR_DB_PATH = Path(__file__).parent / "knowledge_base"