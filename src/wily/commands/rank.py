"""
Rank command.

The report command gives a table of files sorted according their ranking scheme
of a specified metric.
Will compare the values between files and return a sorted table.

TODO: Layer on Click invocation in operators section, __main__.py file
"""
import operator as op
import os
from pathlib import Path
from sys import exit
from typing import Optional

import radon.cli.harvest
import tabulate

from wily import format_date, format_revision, logger
from wily.archivers import resolve_archiver
from wily.config import DEFAULT_PATH, WilyConfig
from wily.helper import get_maxcolwidth, get_style
from wily.operators import resolve_metric_as_tuple
from wily.state import State


def rank(
    config: WilyConfig,
    path: Optional[str],
    metric: str,
    revision_index: str,
    limit: int,
    threshold: int,
    descending: bool,
    wrap: bool,
) -> None:
    """
    Rank command ordering files, methods or functions using metrics.

    :param config: The configuration.
    :param path: The path to the file.
    :param metric: Name of the metric to report on.
    :param revision_index: Version of git repository to revert to.
    :param limit: Limit the number of items in the table.
    :param threshold: For total values beneath the threshold return a non-zero exit code.
    :param descending: Rank in descending order
    :param wrap: Wrap output

    :return: Sorted table of all files in path, sorted in order of metric.
    """
    pass
