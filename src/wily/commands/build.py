"""
Builds a cache based on a source-control history.

TODO : Convert .gitignore to radon ignore patterns to make the build more efficient.

"""
import multiprocessing
import os
import pathlib
from sys import exit
from typing import Any, Dict, List, Tuple

from progress.bar import Bar

from wily import logger
from wily.archivers import Archiver, FilesystemArchiver, Revision
from wily.archivers.git import InvalidGitRepositoryError
from wily.config.types import WilyConfig
from wily.operators import Operator, resolve_operator
from wily.state import State


def run_operator(
    operator: Operator, revision: Revision, config: WilyConfig, targets: List[str]
) -> Tuple[str, Dict[str, Any]]:
    """
    Run an operator for the multiprocessing pool.

    :param operator: The operator to use
    :param revision: The revision index
    :param config: The runtime configuration
    :param targets: Files/paths to scan
    """
    pass


def build(config: WilyConfig, archiver: Archiver, operators: List[Operator]) -> None:
    """
    Build the history given an archiver and collection of operators.

    :param config: The wily configuration
    :param archiver: The archiver to use
    :param operators: The list of operators to execute
    """
    pass
