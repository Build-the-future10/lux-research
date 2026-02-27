import json

class ReportGenerator:
    def generate_json(self, data, path="report.json"):
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    def generate_markdown(self, summary, path="report.md"):
        with open(path, "w") as f:
            for k, v in summary.items():
                f.write(f"**{k}**: {v}\n\n")
