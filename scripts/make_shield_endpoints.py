import sys

if not sys.version_info.major == 3 and int(sys.version_info.minor) >= 7:
    print("Incompatible Python version, need 3.7+")
    sys.exit(-1)

import json
import os
from typing import Dict, Union

import yaml

DATA: Dict[str, Dict[str, Union[int, str, list]]] = {}

DEFAULT = {
    "schemaVersion": 1,
    "namedLogo": "OctoPrint",
    "labelColor": "white",
    "color": "brightgreen",
}

# Read current stats
DATA_DIR = os.path.abspath("_data")
STATS_FILE = os.path.join(DATA_DIR, "stats.yml")
if os.path.isfile(STATS_FILE):
    print("Reading stored data")
    with open(STATS_FILE, "rt") as file:
        DATA = yaml.load(file, Loader=yaml.Loader)

# Process the data
SHIELDS_DIR = os.path.abspath("shields")
for plugin in DATA:
    print("Creating endpoints for {}".format(plugin["name"]))
    PLUGIN_DIR = os.path.join(SHIELDS_DIR, plugin["name"])
    os.makedirs(PLUGIN_DIR, exist_ok=True)

    with open(os.path.join(PLUGIN_DIR, "total.json"), "w+") as file:
        json.dump(
            {**DEFAULT, "label": "Installations", "message": str(plugin["total"])}, file
        )

print("Done!")
