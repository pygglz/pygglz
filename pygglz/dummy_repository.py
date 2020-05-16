from .state_repository import StateRepository


class DummyRepository(StateRepository):
    def __init__(self):
        super().__init__()
