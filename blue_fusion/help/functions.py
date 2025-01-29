from typing import List

from blue_options.terminal import show_usage, xtra
from abcli.help.generic import help_functions as generic_help_functions

from blue_fusion.help.bright import help_functions as help_bright
from blue_fusion import ALIAS


def help_browse(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "actions|repo"

    return show_usage(
        [
            "@fusion",
            "browse",
            f"[{options}]",
        ],
        "browse blue_fusion.",
        mono=mono,
    )


help_functions = generic_help_functions(plugin_name=ALIAS)

help_functions.update(
    {
        "browse": help_browse,
        "bright": help_bright,
    }
)
