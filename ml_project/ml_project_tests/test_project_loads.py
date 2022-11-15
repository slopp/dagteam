from ml_project import ml_project

def test_ml_project_loads():
    # will raise errors if the project can't load
    # similar to loading a failing project in dagit
    ml_project.load_all_definitions()
