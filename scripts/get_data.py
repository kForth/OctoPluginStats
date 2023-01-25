import sys

if not sys.version_info.major == 3 and int(sys.version_info.minor) >= 7:
    print("Incompatible Python version, need 3.7+")
    sys.exit(-1)

import copy
import json
import os
import re
import time
from typing import Dict, Union

import requests
import yaml

PLUGIN_AUTHOR: str = "Kestin Goforth"

DEFAULT_SHIELD: dict = {
    "schemaVersion": 1,
    "namedLogo": "OctoPrint",
    "labelColor": "white",
    "color": "brightgreen",
    "style": "flat",
}

DATA_URL: str = "https://plugins.octoprint.org/plugins.json"

DATA: Dict[str, Dict[str, Union[int, str, list]]] = {}

# DATA STRUCTURE:
# {"plugin_id":
#   {
#       "total": 00,
#       "versions": {"0.1.0": 00, "0.2.0": 00}
#       "history": [
#           {"date": "2020-12-1", "total": 00, "versions": {"0.1.0": 00, "0.2.0": 00}},
#           "etc etc"
#       }
#   }
#  "etc...." for more plugins.

TODAY = time.strftime("%Y-%m-%d")

RE_GITHUB = re.compile(r"(?:https?:\/\/)github.com\/(?:.*)\/(.*)")

DATA_DIR = os.path.abspath("_data")
STATS_FILE = os.path.join(DATA_DIR, "stats.yml")
AUTHOR_FILE = os.path.abspath("author.json")

author = {
    "name": PLUGIN_AUTHOR,
    "plugins": 0,
    "instances_month": 0,
    "instances_week": 0,
    "install_events_month": 0,
    "install_events_week": 0,
}

# Read current data (if any)
if os.path.isfile(STATS_FILE):
    print("Reading stored data")
    with open(STATS_FILE, "rt") as file:
        raw = yaml.load(file, Loader=yaml.Loader)
        DATA = {e["name"]: e for e in raw}

# Get the data
response = requests.get(DATA_URL).json()

# Iterate through, find plugins by author
for plugin in response:
    if PLUGIN_AUTHOR in plugin["author"]:
        plugin_id = plugin["id"]
        print("Processing data for {}".format(plugin_id))
        # Test plugin data exists
        try:
            existing_data = DATA[plugin_id]
        except (KeyError, TypeError):
            # Plugin not seen before, create the dict
            DATA[plugin_id] = {"total": 0, "month": 0, "week": 0, "history": []}

        stats = copy.deepcopy(DATA[plugin_id])
        stats["name"] = plugin_id
        stats["total"] = plugin["stats"]["instances_month"]

        # Try to get the plugin title from the github homepage
        if re_match := RE_GITHUB.match(plugin["homepage"]):
            stats["title"] = re_match.group(1)
        else:
            stats["title"] = plugin["title"]

        # Remove the 31st day, if relevant
        if len(stats["history"]) >= 30:
            # Check it's not been run more than once per day, latest data is not today.
            if stats["history"][29]["date"] != TODAY:
                # remove earliest data
                stats["history"].pop(0)

        if not len(stats["history"]) or stats["history"][-1]["date"] != TODAY:
            # Add the latest point to the history
            stats["history"].append(
                {
                    "date": TODAY,
                    "total": plugin["stats"]["instances_month"],
                    "issues": plugin["github"]["issues"],
                }
            )

        # Put the data back
        DATA[plugin_id] = stats

        # Update author info
        author["plugins"] += 1
        author["instances_month"] += plugin["stats"]["instances_month"]
        author["instances_week"] += plugin["stats"]["instances_week"]
        author["install_events_month"] += plugin["stats"]["install_events_month"]
        author["install_events_week"] += plugin["stats"]["install_events_week"]

# write back to the file
with open(STATS_FILE, "wt") as file:
    yaml.dump(list(DATA.values()), file, Dumper=yaml.Dumper)

# Update author stats
print("Updating author stats")
with open(AUTHOR_FILE, "wt") as file:
    json.dump(author, file)

print("Done!")
