"""
A module for working with the .wily/ cache directory.

This API is not intended to be public and should not be consumed directly.
The API in this module is for archivers and commands to work with the local cache

"""

import json
import os.path
import pathlib
import shutil
from typing import Any, Dict, List, Union

from wily import __version__, logger
from wily.archivers import ALL_ARCHIVERS, Archiver, Revision
from wily.config.types import WilyConfig
from wily.lang import _
from wily.operators import resolve_operator


def exists(config: WilyConfig) -> bool:
    """
    Check whether the .wily/ directory exists.

    :param config: The configuration

    :return: Whether the .wily directory exists
    """
    pass


def create_index(config: WilyConfig) -> None:
    """Create the root index."""
    pass


def create(config: WilyConfig) -> str:
    """
    Create a wily cache.

    :param config: The configuration
    :return: The path to the cache
    """
    pass


def clean(config: WilyConfig) -> None:
    """
    Delete a wily cache.

    :param config: The configuration
    """
    pass


def store(
    config: WilyConfig,
    archiver: Union[Archiver, str],
    revision: Revision,
    stats: Dict[str, Any],
) -> pathlib.Path:
    """
    Store a revision record within an archiver folder.

    :param config: The configuration
    :param archiver: The archiver to get name from (e.g. 'git')
    :param revision: The revision
    :param stats: The collected data

    :return: The absolute path to the created file
    """
    pass


def store_archiver_index(
    config: WilyConfig, archiver: Union[Archiver, str], index: List[Dict[str, Any]]
) -> pathlib.Path:
    """
    Store an archiver's index record for faster search.

    :param config: The configuration
    :param archiver: The archiver to get name from (e.g. 'git')
    :param index: The archiver index record

    :return: The absolute path to the created file
    """
    pass


def list_archivers(config: WilyConfig) -> List[str]:
    """
    List the names of archivers with data.

    :param config: The configuration

    :return: A list of archiver names
    """
    pass


def get_default_metrics(config: WilyConfig) -> List[str]:
    """
    Get the default metrics for a configuration.

    :param config: The configuration
    :return: Return the list of default metrics in this index
    """
    pass


def has_archiver_index(config: WilyConfig, archiver: Union[Archiver, str]) -> bool:
    """
    Check if this archiver has an index file.

    :param config: The configuration
    :param archiver: The name of the archiver type (e.g. 'git')

    :return: Whether the archiver's index exists.
    """
    pass


def get_archiver_index(config: WilyConfig, archiver: Union[Archiver, str]) -> Any:
    """
    Get the contents of the archiver index file.

    :param config: The configuration
    :param archiver: The name of the archiver type (e.g. 'git')
    :return: The index data
    """
    pass


def get(
    config: WilyConfig, archiver: Union[Archiver, str], revision: str
) -> Dict[Any, Any]:
    """
    Get the data for a given revision.

    :param config: The configuration
    :param archiver: The archiver to get name from (e.g. 'git')
    :param revision: The revision ID
    :return: The data record for that revision
    """
    pass
