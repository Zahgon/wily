"""
Diff command.

Compares metrics between uncommitted files and indexed files.
"""
import multiprocessing
import os
from pathlib import Path
from sys import exit
from typing import List, Optional

import radon.cli.harvest
import tabulate

from wily import format_date, format_revision, logger
from wily.archivers import resolve_archiver
from wily.commands.build import run_operator
from wily.config import DEFAULT_PATH
from wily.config.types import WilyConfig
from wily.helper import get_maxcolwidth, get_style
from wily.operators import (
    BAD_COLORS,
    GOOD_COLORS,
    OperatorLevel,
    get_metric,
    resolve_metric,
    resolve_operator,
)
from wily.state import State


def diff(
    config: WilyConfig,
    files: List[str],
    metrics: List[str],
    changes_only: bool = True,
    detail: bool = True,
    revision: Optional[str] = None,
    wrap: bool = False,
) -> None:
    """
    Show the differences in metrics for each of the files.

    :param config: The wily configuration
    :param files: The files to compare.
    :param metrics: The metrics to measure.
    :param changes_only: Only include changes files in output.
    :param detail: Show details (function-level)
    :param revision: Compare with specific revision
    :param wrap: Wrap output
    """
    pass
