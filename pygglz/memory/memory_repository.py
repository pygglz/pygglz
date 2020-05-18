from ..state_repository import StateRepository


class MemoryRepository(StateRepository):
    """A memory repository managed the features states in memory (in a dict)."""

    def __init__(self):
        super().__init__()
