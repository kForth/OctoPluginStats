# {{cookiecutter.repo_name}}

[![GitHub Forks](https://img.shields.io/github/forks/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}?label=Forks&logo=GitHub&logoColor=black&labelColor=white&color=blue)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/network/members)
[![GitHub Stars](https://img.shields.io/github/stars/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}?label=Stars&logo=GitHub&logoColor=black&labelColor=white&color=blue)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/stargazers)
[![GitHub Watchers](https://img.shields.io/github/watchers/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}?label=Watchers&logo=GitHub&logoColor=black&labelColor=white&color=blue)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/watchers)

[![Plugins](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2F{{cookiecutter.github_username}}%2F{{cookiecutter.repo_name}}%2Fmain%2Fshields%2Fcount.json)](https://plugins.octoprint.org/by_author#kestin-goforth)
[![Active Instances](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2F{{cookiecutter.github_username}}%2F{{cookiecutter.repo_name}}%2Fmain%2Fshields%2Ftotal.json)](https://plugins.octoprint.org/by_author#kestin-goforth)
[![New This Month](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2F{{cookiecutter.github_username}}%2F{{cookiecutter.repo_name}}%2Fmain%2Fshields%2Fmonth.json)](https://plugins.octoprint.org/by_author#kestin-goforth)
[![New This Week](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2F{{cookiecutter.github_username}}%2F{{cookiecutter.repo_name}}%2Fmain%2Fshields%2Fweek.json)](https://plugins.octoprint.org/by_author#kestin-goforth)

Github Pages site for tracking installation statistics about your OctoPrint plugins.

It also hosts custom JSON endpoints for [shields.io](https://shields.io)!

## Want to use this to track your own stats? Feel free!

And I'll even give you a little how-to, after forking this repository:

1. Update the links in `_data_/navbar.tml` to your own ones, not mine!
2. Delete the existing stats file (`_data/stats.yml`) and the shields endpoints (`shields/`).
3. Edit the target `PLUGIN_AUTHOR` in the `scripts/get_data.py` file, [here](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/blob/main/scripts/get_data.py#L16)
4. Run the script, either using the Github action (manually triggered) or via `python scripts/get_data.py` to generate the initial data
5. Make sure you have enabled the actions in repository settings. Last time I checked actions were disabled for forks by default.

That should be all, if you have any questions let me know!
