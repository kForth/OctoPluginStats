import sys

if not sys.version_info.major == 3 and int(sys.version_info.minor) >= 7:
    print("Incompatible Python version, need 3.7+")
    sys.exit(-1)

import json
import os
from typing import Dict, Union

DATA: Dict[str, Dict[str, Union[int, str, list]]] = {}

DEFAULT = {
    "schemaVersion": 1,
    "namedLogo": "OctoPrint",
    "labelColor": "white",
    "color": "brightgreen",
}

# Read current stats
if os.path.isfile(os.path.abspath(os.path.join("data", "stats.json"))):
    print("Reading stored data")
    with open(os.path.abspath(os.path.join("data", "stats.json")), "rt") as file:
        DATA = json.load(file)

# Process the data
SHIELDS_DIR = os.path.abspath(os.path.join("data", "shields"))
for plugin_id, data in DATA.items():
    print("Creating endpoints for {}".format(plugin_id))
    PLUGIN_DIR = os.path.join(SHIELDS_DIR, plugin_id)
    os.makedirs(PLUGIN_DIR, exist_ok=True)
    with open(os.path.join(PLUGIN_DIR, "total.json"), "w+") as file:
        json.dump(
            {**DEFAULT, "label": "Installations", "message": str(data["total"])}, file
        )

print("Done!")
