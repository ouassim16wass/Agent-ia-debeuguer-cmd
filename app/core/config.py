import json
from pathlib import Path

def load_config():
    config_path = Path(__file__).parents[1] / "config.json"
    return json.loads(config_path.read_text())
