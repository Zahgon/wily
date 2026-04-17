"""
Index command.

Print information about the wily cache and what is in the index.
"""
from typing import List, Tuple

import tabulate

from wily import MAX_MESSAGE_WIDTH, format_date, format_revision, logger
from wily.config.types import WilyConfig
from wily.helper import get_maxcolwidth, get_style
from wily.state import State


def index(
    config: WilyConfig, include_message: bool = False, wrap: bool = False
) -> None:
    """
    Show information about the cache and runtime.

    :param config: The wily configuration
    :param include_message: Include revision messages
    :param wrap: Wrap long lines
    """
    pass
