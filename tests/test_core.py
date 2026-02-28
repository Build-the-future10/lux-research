from lux_research.core import ResearchProject

def test_project_initialization():
    project = ResearchProject(name="Test")
    assert project.name == "Test"
