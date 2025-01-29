import os

from blue_objects import file, README

from blue_fusion import NAME, VERSION, ICON, REPO_NAME


items = []


def build():
    return README.build(
        items=items,
        path=os.path.join(file.path(__file__), ".."),
        ICON=ICON,
        NAME=NAME,
        VERSION=VERSION,
        REPO_NAME=REPO_NAME,
    )
