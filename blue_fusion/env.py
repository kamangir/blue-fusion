import os
from blue_options.env import load_config, load_env

load_env(__name__)
load_config(__name__)


BLUE_FUSION_CONFIG = os.getenv(
    "BLUE_FUSION_CONFIG",
    "",
)
