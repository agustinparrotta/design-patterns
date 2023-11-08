import abc
import logging
from typing import Type

logging.basicConfig(level="INFO")


class InvalidTransitionError(Exception):
    """Raised when trying to move to a target state from an unreachable source
    state.
    """


"""Note that MergeRequest and MergeRequestState have links to each other. 
The moment a transition is made, the former object will not have extra references 
and should be garbage-collected, so this relationship should be always 1:1. 
With some small and more detailed considerations, a weak reference might be used."""


class MergeRequestState(abc.ABC):
    def __init__(self, merge_request):
        self._merge_request = merge_request

    @abc.abstractmethod
    def open(self):
        ...

    @abc.abstractmethod
    def close(self):
        ...

    @abc.abstractmethod
    def merge(self):
        ...

    def __str__(self):
        return self.__class__.__name__


class Open(MergeRequestState):
    def open(self):
        self._merge_request.approvals = 0

    def close(self):
        self._merge_request.approvals = 0
        self._merge_request.state = Closed

    def merge(self):
        logging.info("merging %s", self._merge_request)
        logging.info("deleting branch %s", self._merge_request.source_branch)
        self._merge_request.state = Merged


class Closed(MergeRequestState):
    def open(self):
        logging.info("reopening closed merge request %s", self._merge_request)
        self._merge_request.state = Open

    def close(self):
        """Current state."""

    def merge(self):
        raise InvalidTransitionError("can't merge a closed request")


class Merged(MergeRequestState):
    def open(self):
        raise InvalidTransitionError("already merged request")

    def close(self):
        raise InvalidTransitionError("already merged request")

    def merge(self):
        """Current state."""


class MergeRequest:
    def __init__(self, source_branch: str, target_branch: str) -> None:
        self.source_branch = source_branch
        self.target_branch = target_branch
        self._state = None
        self.approvals = 0
        self.state = Open

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state_cls):
        """The state is a property, so not only is it public , but there
        is also a single place with the definitions of how states are created
        for a merge request, passing self as a parameter.
        """
        self._state = new_state_cls(self)

    def open(self):
        return self.state.open()

    def close(self):
        return self.state.close()

    def merge(self):
        return self.state.merge()

    def __str__(self):
        return f"{self.target_branch}:{self.source_branch}"


class MergeRequestLessBoilerplate:
    """Remove open, close and merge methods"""

    def __init__(self, source_branch: str, target_branch: str) -> None:
        self.source_branch = source_branch
        self.target_branch = target_branch
        self._state: MergeRequestState
        self.approvals = 0
        self.state: MergeRequestState = Open  # type: ignore

    @property
    def state(self) -> MergeRequestState:
        return self._state

    @state.setter
    def state(self, new_state_cls: Type[MergeRequestState]):
        self._state = new_state_cls(self)

    @property
    def status(self):
        return str(self.state)

    def __getattr__(self, method):
        return getattr(self.state, method)

    def __str__(self):
        return f"{self.target_branch}:{self.source_branch}"


if __name__ == "__main__":
    # mr = MergeRequest("feature-1", "master")
    mr = MergeRequestLessBoilerplate("feature-1", "master")

    mr.open()

    mr.approvals = 3
    mr.close()

    mr.open()

    mr.merge()

    # mr.close()
