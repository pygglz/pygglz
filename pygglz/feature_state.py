class FeatureState(object):
    def __init__(self, name: str, enabled: bool = False):
        self.name = name
        self.enabled = enabled

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __repr__(self):
        return "<FeatureState name={} enabled={}>".format(self.name, self.enabled)
