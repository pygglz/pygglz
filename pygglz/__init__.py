"""pygglz managed features toggles and is designed after the Java
togglz framework.
"""
from .features import Features
from .http_repository import HttpRepository

"""features This is the global access point to feature state.

Use features to query the feature states. features then delegates
to the current feature context. This can be the global feature
context or a sub context associated with the current thread, e.g.
in unit testing contexts.
"""
features = Features()

"""configure Main configuration entry point."""
configure = features.configure

"""new_feature_context Establish a new sub feature context."""
new_feature_context = features.new_feature_context
