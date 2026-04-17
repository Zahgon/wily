"""
For managing the state of the wily process.

Contains a lazy revision, index and process state model.
"""
from collections import OrderedDict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from wily import cache, logger
from wily.archivers import Archiver, BaseArchiver, Revision, resolve_archiver
from wily.config.types import WilyConfig
from wily.operators import Operator, get_metric


@dataclass
class IndexedRevision:
    """Union of revision and the operators executed."""

    revision: Revision
    operators: List
    _data = None

    @staticmethod
    def fromdict(d: Dict[str, Any]) -> "IndexedRevision":
        """Instantiate from a dictionary."""
        pass

    def asdict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        pass

    def get(
        self, config: WilyConfig, archiver: str, operator: str, path: str, key: str
    ) -> Any:
        """
        Get the metric data for this indexed revision.

        :param config: The wily config.
        :param archiver: The archiver.
        :param operator: The operator to find
        :param path: The path to find
        :param key: The metric key
        """
        pass

    def get_paths(self, config: WilyConfig, archiver: str, operator: str) -> List[str]:
        """
        Get the indexed paths for this indexed revision.

        :param config: The wily config.
        :param archiver: The archiver.
        :param operator: The operator to find

        :return: A list of paths
        """
        pass

    def store(
        self, config: WilyConfig, archiver: Union[Archiver, str], stats: Dict[str, Any]
    ) -> Path:
        """
        Store the stats for this indexed revision.

        :param config: The wily config.
        :param archiver: The archiver.
        :param stats: The data
        """
        pass


class Index:
    """The index of the wily cache."""

    archiver: Archiver
    config: WilyConfig
    operators = None
    data: List[Any]

    def __init__(self, config: WilyConfig, archiver: Archiver):
        """
        Instantiate a new index.

        :param config: The wily config.
        :param archiver: The archiver.
        """
        self.config = config
        self.archiver = archiver
        self.data = (
            cache.get_archiver_index(config, archiver.name)
            if cache.has_archiver_index(config, archiver.name)
            else []
        )

        self._revisions = OrderedDict(
            {d["key"]: IndexedRevision.fromdict(d) for d in self.data}
        )

    def __len__(self):
        """Use length of revisions as len."""
        return len(self._revisions)

    @property
    def last_revision(self) -> IndexedRevision:
        """Return the most recent revision."""
        pass

    @property
    def revisions(self) -> List[IndexedRevision]:
        """List of all the revisions."""
        return list(self._revisions.values())

    @property
    def revision_keys(self) -> List[str]:
        """List of all the revision indexes."""
        pass

    def __contains__(self, item: Union[str, Revision]) -> bool:
        """Check if index contains `item`."""
        if isinstance(item, Revision):
            return item.key in self._revisions
        elif isinstance(item, str):
            return item in self._revisions
        else:
            raise TypeError("Invalid type for __contains__ in Index.")

    def __getitem__(self, index) -> IndexedRevision:
        """Get the revision for a specific index."""
        return self._revisions[index]

    def add(self, revision: Revision, operators: List[Operator]) -> IndexedRevision:
        """
        Add a revision to the index.

        :param revision: The revision.
        :param operators: Operators for the revision.
        """
        pass

    def save(self):
        """Save the index data back to the wily cache."""
        pass


class State:
    """
    The wily process state.

    Includes indexes for each archiver.
    """

    archivers: List[str]
    config: WilyConfig
    index: Dict[str, Index]
    default_archiver: str
    operators: Optional[List[Operator]] = None

    def __init__(
        self,
        config: WilyConfig,
        archiver: Optional[Union[Archiver, BaseArchiver]] = None,
    ):
        """
        Instantiate a new process state.

        :param config: The wily configuration.
        :param archiver: The archiver (optional).
        """
        if archiver:
            self.archivers = [archiver.name]
        else:
            self.archivers = cache.list_archivers(config)
        logger.debug("Initialised state indexes for archivers %s", self.archivers)
        self.config = config
        self.index = {}
        for _archiver in self.archivers:
            self.index[_archiver] = Index(self.config, resolve_archiver(_archiver))
        self.default_archiver = self.archivers[0]

    def ensure_exists(self):
        """Ensure that cache directory exists."""
        pass
