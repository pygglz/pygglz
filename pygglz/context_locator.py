import threading


class ContextLocator(object):
    def __init__(self, global_instance):
        self.global_instance = global_instance
        self.thread_local = threading.local()

    def peek_context(self):
        if self.thread_local.instances is not None:
            context = self.thread_local.instances[-1]
            if context is not None:
                return context

        return self.global_instance

    def push_context(self, context):
        if self.thread_local.instances is None:
            self.thread_local.instances = []

        self.thread_local.instances.append(context)

    def pop_context(self):
        if self.thread_local.instances is None:
            return

        self.thread_local.instances.pop()
