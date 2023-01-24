import itertools
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

RE_GITHUB = re.compile(r"(?:https?:\/\/)?(?:www.)?github.com\/[^\/]*\/([^\/]*)\/?")
RE_GHPAGES = re.compile(r"(?:https?:\/\/)?[^\/.]*.github.io\/([^\/]*)\/?")

DATA_DIR = os.path.abspath("_data")
STATS_FILE = os.path.join(DATA_DIR, "stats.yml")
SHIELDS_DIR = os.path.abspath("shields")

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
        stats["month"] = plugin["stats"]["install_events_month"]
        stats["week"] = plugin["stats"]["install_events_week"]

        # Try to get the plugin title from the homepage or archive
        for (regex, url) in itertools.product(
            (RE_GITHUB, RE_GHPAGES),
            (plugin["homepage"], plugin["archive"]),
        ):
            if re_match := regex.match(url):
                stats["title"] = re_match.group(1)
                break
        else:
            print("Cannot find title from urls")
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

# write back to the file
with open(STATS_FILE, "wt") as file:
    yaml.dump(list(DATA.values()), file, Dumper=yaml.Dumper)

# Update plugin shields endpoints
for plugin in DATA.values():
    PLUGIN_DIR = os.path.join(SHIELDS_DIR, plugin["name"])
    print("Updating shields for {}".format(plugin["name"]))
    os.makedirs(PLUGIN_DIR, exist_ok=True)

    def write_shield_endpoint(name, label, message):
        with open(os.path.join(PLUGIN_DIR, f"{name}.json"), "w+") as file:
            json.dump({**DEFAULT_SHIELD, "label": label, "message": str(message)}, file)

    write_shield_endpoint("total", "Active Instances", plugin["total"])
    write_shield_endpoint("month", "New Monthly", plugin["month"])
    write_shield_endpoint("week", "New Weekly", plugin["week"])


# Update author shields endpoints
print("Updating author shields")
instances = {
    "total": sum([e["total"] for e in DATA.values()]),
    "month": sum([e["month"] for e in DATA.values()]),
    "week": sum([e["week"] for e in DATA.values()]),
}


def write_shield_endpoint(name, label, message):
    with open(os.path.join(SHIELDS_DIR, f"{name}.json"), "w+") as file:
        json.dump({**DEFAULT_SHIELD, "label": label, "message": str(message)}, file)


write_shield_endpoint("count", "Plugins", len(DATA))
write_shield_endpoint("total", "Active Instances", instances["total"])
write_shield_endpoint("month", "New Monthly", instances["month"])
write_shield_endpoint("week", "New Weekly", instances["week"])

print("Done!")
