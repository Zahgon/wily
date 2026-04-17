"""
Graph command.

Draw graph in HTML for a specific metric.
"""

from pathlib import Path
from typing import Optional, Tuple, Union

import plotly.graph_objs as go
import plotly.offline

from wily import format_datetime, logger
from wily.config.types import WilyConfig
from wily.operators import Metric, resolve_metric, resolve_metric_as_tuple
from wily.state import State


def metric_parts(metric):
    """Convert a metric name into the operator and metric names."""
    pass


def path_startswith(filename: str, path: str) -> bool:
    """Check whether a filename starts with a given path in platform-agnostic way."""
    pass


def graph(
    config: WilyConfig,
    path: Tuple[str, ...],
    metrics: str,
    output: Optional[str] = None,
    x_axis: Optional[str] = None,
    changes: bool = True,
    text: bool = False,
    aggregate: bool = False,
    plotlyjs: Union[bool, str] = True,
) -> None:
    """
    Graph information about the cache and runtime.

    :param config: The configuration.
    :param path: The path to the files.
    :param metrics: The Y and Z-axis metrics to report on.
    :param output: Save report to specified path instead of opening browser.
    :param x_axis: Name of metric for x-axis or "history".
    :param changes: Only graph changes.
    :param text: Show commit message inline in graph.
    :param aggregate: Aggregate values for graph.
    :param plotlyjs: How to include plotly.min.js.
    """
    pass
