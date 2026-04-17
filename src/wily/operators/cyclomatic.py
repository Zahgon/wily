"""
Cyclomatic complexity metric for each function/method.

Provided by the radon library.
"""
import statistics
from typing import Any, Dict, Iterable

import radon.cli.harvest as harvesters
from radon.cli import Config
from radon.complexity import SCORE
from radon.visitors import Class, Function

from wily import logger
from wily.config.types import WilyConfig
from wily.lang import _
from wily.operators import BaseOperator, Metric, MetricType


class CyclomaticComplexityOperator(BaseOperator):
    """Cyclomatic complexity operator."""

    name = "cyclomatic"
    defaults = {
        "exclude": None,
        "ignore": None,
        "min": "A",
        "max": "F",
        "no_assert": True,
        "show_closures": False,
        "order": SCORE,
        "include_ipynb": True,
        "ipynb_cells": True,
    }

    metrics = (
        Metric(
            "complexity",
            _("Cyclomatic Complexity"),
            float,
            MetricType.AimLow,
            statistics.mean,
        ),
    )

    default_metric_index = 0  # MI

    def __init__(self, config: WilyConfig, targets: Iterable[str]):
        """
        Instantiate a new Cyclomatic Complexity operator.

        :param config: The wily configuration.
        :param targets: An iterable of paths from which to harvest metrics.
        """
        # TODO: Import config for harvester from .wily.cfg
        logger.debug("Using %s with %s for CC metrics", targets, self.defaults)

        self.harvester = harvesters.CCHarvester(targets, config=Config(**self.defaults))

    def run(self, module: str, options: Dict[str, Any]) -> Dict[Any, Any]:
        """
        Run the operator.

        :param module: The target module path.
        :param options: Any runtime options.
        :return: The operator results.
        """
        pass

    @staticmethod
    def _dict_from_function(l: Function) -> Dict[str, Any]:
        pass

    @staticmethod
    def _dict_from_class(l: Class) -> Dict[str, Any]:
        pass
