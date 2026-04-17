"""
Git Archiver.

Implementation of the archiver API for the gitpython module.
"""
import logging
from typing import Any, Dict, List, Tuple

import git.exc
from git.objects import Commit
from git.repo import Repo

from wily.archivers import BaseArchiver, Revision
from wily.config.types import WilyConfig

logger = logging.getLogger(__name__)


class InvalidGitRepositoryError(Exception):
    """Error for when a folder is not a git repo."""

    pass


class DirtyGitRepositoryError(Exception):
    """Error for a dirty git repository (untracked files)."""

    def __init__(self, untracked_files: List[str]):
        """
        Raise error for untracked files.

        :param untracked_files: List of untracked files
        :param untracked_files: ``list``
        """
        self.untracked_files = untracked_files
        self.message = "Dirty repository, make sure you commit/stash files first"


def get_tracked_files_dirs(repo: Repo, commit: Commit) -> Tuple[List[str], List[str]]:
    """Get tracked files in a repo for a commit hash using ls-tree."""
    pass


def whatchanged(
    commit_a: Commit, commit_b: Commit
) -> Tuple[List[str], List[str], List[str]]:
    """Get files added, modified and deleted between commits."""
    pass


class GitArchiver(BaseArchiver):
    """Gitpython implementation of the base archiver."""

    name = "git"

    def __init__(self, config: "WilyConfig"):
        """
        Instantiate a new Git Archiver.

        :param config: The wily configuration
        """
        try:
            self.repo = Repo(config.path)
        except git.exc.InvalidGitRepositoryError as e:
            raise InvalidGitRepositoryError from e

        self.config = config
        if self.repo.head.is_detached:
            self.current_branch = self.repo.head.object.hexsha
        else:
            self.current_branch = self.repo.active_branch
        assert not self.repo.bare, "Not a Git repository"

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
        pass

    def finish(self):
        """
        Clean up any state if processing completed/failed.

        For git, will checkout HEAD on the original branch when finishing
        """
        pass

    def find(self, search: str) -> Revision:
        """
        Search a string and return a single revision.

        :param search: The search term.

        :return: An instance of revision.
        """
        pass
