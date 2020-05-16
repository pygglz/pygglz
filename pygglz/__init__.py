from .dummy_repository import DummyRepository
from .features import Features
from .file_repository import FileRepository

features = Features()
configure = features.configure
new_feature_context = features.new_feature_context
