import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_fusion import NAME
from blue_fusion.help.bright import urls
from blue_fusion.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="get_url",
)
parser.add_argument(
    "--what",
    type=str,
    default=list(urls.keys())[0],
    help=" | ".join(urls.keys()),
)
args = parser.parse_args()

success = False
if args.task == "get_url":
    success = args.what in urls
    print(urls.get(args.what, ""))
else:
    success = None

sys_exit(logger, NAME, args.task, success)
