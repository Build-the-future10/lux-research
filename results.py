from dataclasses import dataclass
from typing import Any, Dict
import json


@dataclass
class ResearchResult:
    name: str
    value: Any
    metadata: Dict

    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value,
            "metadata": self.metadata
        }

    def save(self, path: str):
        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=4)
