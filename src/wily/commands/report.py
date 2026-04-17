"""
Report command.

The report command gives a table of metrics for a specified list of files.
Will compare the values between revisions and highlight changes in green/red.
"""
from pathlib import Path
from shutil import copytree
from string import Template
from typing import Dict, Iterable, List, Tuple

import tabulate

from wily import MAX_MESSAGE_WIDTH, format_date, format_revision, logger
from wily.config.types import WilyConfig
from wily.helper import get_maxcolwidth
from wily.helper.custom_enums import ReportFormat
from wily.lang import _
from wily.operators import MetricType, resolve_metric_as_tuple
from wily.state import State

ANSI_RED = 31
ANSI_GREEN = 32
ANSI_YELLOW = 33


def report(
    config: WilyConfig,
    path: str,
    metrics: Iterable[str],
    n: int,
    output: Path,
    console_format: str,
    include_message: bool = False,
    format: ReportFormat = ReportFormat.CONSOLE,
    changes_only: bool = False,
    wrap: bool = False,
) -> None:
    """
    Show metrics for a given file.

    :param config: The configuration
    :param path: The path to the file
    :param metrics: List of metrics to report on
    :param n: Number of items to list
    :param output: Output path
    :param include_message: Include revision messages
    :param format: Output format
    :param console_format: Grid format style for tabulate
    :param changes_only: Only report revisions where delta != 0
    :param wrap: Wrap output
    """
    pass
