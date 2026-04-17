"""
Filesystem Archiver.

Implementation of the archiver API for a standard directory (no revisions)
"""
import hashlib
import logging
import os.path
from typing import Any, Dict, List

from wily.archivers import BaseArchiver, Revision
from wily.config.types import WilyConfig

logger = logging.getLogger(__name__)


class FilesystemArchiver(BaseArchiver):
    """Basic implementation of the base archiver."""

    name = "filesystem"

    def __init__(self, config: "WilyConfig"):
        """
        Instantiate a new Filesystem Archiver.

        :param config: The wily configuration
        """
        self.config = config

    def revisions(self, path: str, max_revisions: int) -> List[Revision]:
        """
        Get the list of revisions.

        :param path: the path to target.
        :param max_revisions: the maximum number of revisions.
        :return: A list of revisions.
        """
        pass

    def checkout(self, revision: Revision, options: Dict[Any, Any]) -> None:
        """
        Checkout a specific revision.

        :param revision: The revision identifier.
        :param options: Any additional options.
        """
        # effectively noop since there are no revision
        pass
