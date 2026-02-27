import time

class Experiment:
    def __init__(self, name, function, *args, **kwargs):
        self.name = name
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.result = None
        self.runtime = None

    def run(self):
        start = time.time()
        self.result = self.function(*self.args, **self.kwargs)
        self.runtime = time.time() - start
        return self.result

    def metadata(self):
        return {
            "Name": self.name,
            "Runtime": self.runtime,
            "Result Type": str(type(self.result))
        }
