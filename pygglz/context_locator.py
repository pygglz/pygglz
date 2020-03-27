import threading


class ContextLocator(object):
    def __init__(self, global_instance):
        self.global_instance = global_instance
        self.thread_local = threading.local()

    def peek_context(self):
        instances = getattr(self.thread_local, "instances", None)
        if instances is not None and len(instances) > 0:
            context = instances[-1]
            if context is not None:
                return context

        return self.global_instance

    def push_context(self, context):
        instances = getattr(self.thread_local, "instances", None)
        if instances is None:
            instances = []
            self.thread_local.instances = instances

        instances.append(context)

    def pop_context(self):
        instances = getattr(self.thread_local, "instances", None)
        if instances is None:
            return

        instances.pop()
