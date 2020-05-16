from .dummy_repository import DummyRepository
from .features import Features
from .file_repository import FileRepository
from .http_repository import HttpRepository

features = Features()
configure = features.configure
new_feature_context = features.new_feature_context
