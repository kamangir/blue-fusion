from typing import List

from blue_options.terminal import show_usage, xtra


def help_install(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("recreate_env", mono=mono)

    return show_usage(
        [
            "@fusion",
            "bright",
            "install",
            f"[{options}]",
        ],
        "browse blue_plugin.",
        mono=mono,
    )


help_functions = {
    "install": help_install,
}
