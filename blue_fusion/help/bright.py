from typing import List, Dict

from blue_options.terminal import show_usage, xtra

urls: Dict[str, str] = {
    "github": "https://github.com/ChenHongruixuan/BRIGHT",
    "huggingface": "https://huggingface.co/datasets/Kullervo/BRIGHT",
}


def help_browse(
    tokens: List[str],
    mono: bool,
) -> str:
    options = " | ".join(urls.keys())

    return show_usage(
        [
            "@fusion",
            "bright",
            "browse",
            f"[{options}]",
        ],
        "browse bright.",
        mono=mono,
    )


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
    "browse": help_browse,
    "install": help_install,
}
