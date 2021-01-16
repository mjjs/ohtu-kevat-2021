from urllib import request
from project import Project

from toml import loads


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        config = loads(content)
        poetry_config = config["tool"]["poetry"]

        name = poetry_config["name"]
        desc = poetry_config["description"]
        deps = [k for [k, v] in poetry_config["dependencies"].items()]
        dev_deps = [k for [k, v] in poetry_config["dev-dependencies"].items()]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, deps, dev_deps)
