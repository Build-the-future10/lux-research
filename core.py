import datetime
import uuid

class ResearchProject:
    def __init__(self, title, author):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.created = datetime.datetime.now()
        self.experiments = []

    def add_experiment(self, experiment):
        self.experiments.append(experiment)

    def summary(self):
        return {
            "Project ID": self.id,
            "Title": self.title,
            "Author": self.author,
            "Created": self.created,
            "Experiments": len(self.experiments)
        }
