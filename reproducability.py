import json
import os
import hashlib

class ReproManager:
    def save_config(self, config, path="config.json"):
        with open(path, "w") as f:
            json.dump(config, f, indent=4)

    def hash_data(self, data):
        return hashlib.sha256(str(data).encode()).hexdigest()
