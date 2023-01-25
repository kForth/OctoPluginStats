# OctoPluginStats

[![GitHub Forks](https://img.shields.io/github/forks/kforth/OctoPluginStats?label=Forks&logo=GitHub&logoColor=black&labelColor=white&color=blue)](https://github.com/kForth/OctoPluginStats/network/members)
[![GitHub Stars](https://img.shields.io/github/stars/kforth/OctoPluginStats?label=Stars&logo=GitHub&logoColor=black&labelColor=white&color=blue)](https://github.com/kForth/OctoPluginStats/stargazers)
[![GitHub Watchers](https://img.shields.io/github/watchers/kforth/OctoPluginStats?label=Watchers&logo=GitHub&logoColor=black&labelColor=white&color=blue)](https://github.com/kForth/OctoPluginStats/watchers)

[![Plugins](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=Plugins&query=%24.plugins&url=https%3A%2F%2Fraw.githubusercontent.com%2FkForth%2FOctoPluginStats%2Fmain%2Fauthor.json&logo=OctoPrint&labelColor=white&style=flat)](https://plugins.octoprint.org/by_author#kestin-goforth)
[![Active Instances](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=Active%20Instances&query=%24.instances_month&url=https%3A%2F%2Fraw.githubusercontent.com%2FkForth%2FOctoPluginStats%2Fmain%2Fauthor.json&logo=OctoPrint&labelColor=white&style=flat)](https://plugins.octoprint.org/by_author#kestin-goforth)
[![New This Month](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=New%20This%20Month&query=%24.install_events_month&url=https%3A%2F%2Fraw.githubusercontent.com%2FkForth%2FOctoPluginStats%2Fmain%2Fauthor.json&logo=OctoPrint&labelColor=white&style=flat)](https://plugins.octoprint.org/by_author#kestin-goforth)
[![New This Week](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=New%20This%20Week&query=%24.install_events_week&url=https%3A%2F%2Fraw.githubusercontent.com%2FkForth%2FOctoPluginStats%2Fmain%2Fauthor.json&logo=OctoPrint&labelColor=white&style=flat)](https://plugins.octoprint.org/by_author#kestin-goforth)

Github Pages site for tracking installation statistics about your OctoPrint plugins.

It also hosts a [shields.io](https://shields.io) endpoint for stats about your plugins!

## Want to use this to track your own stats? Feel free!

And I'll even give you a little how-to, after forking this repository:

1. Update the links in `_data_/navbar.tml` to your own ones, not mine!
2. Delete the existing stats file (`_data/stats.yml`) and author file (`author.json`).
3. Edit the target `PLUGIN_AUTHOR` in the `scripts/get_data.py` file, [here](https://github.com/kforth/OctoPluginStats/blob/main/scripts/get_data.py#L16)
4. Run the script, either using the Github action (manually triggered) or via `python scripts/get_data.py` to generate the initial data
5. Make sure you have enabled the actions in repository settings. Last time I checked actions were disabled for forks by default.

That should be all, if you have any questions let me know!
