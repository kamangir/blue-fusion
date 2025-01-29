import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from blue_fusion import NAME
from blue_fusion.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="void",
)
parser.add_argument(
    "--arg",
    type=bool,
    default=0,
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "void":
    success = True
else:
    success = None

sys_exit(logger, NAME, args.task, success)
