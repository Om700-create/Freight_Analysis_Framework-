import os

# Define the project structure
project_structure = {
    "data": {
        "raw": None,
        "external": None,
        "processed": None,
        "interim": None,
    },
    "notebooks": {
        "01_eda.ipynb": None,
        "02_data_cleaning.ipynb": None,
        "03_feature_engineering.ipynb": None,
        "04_modeling.ipynb": None,
        "05_visualization.ipynb": None,
    },
    "src": {
        "__init__.py": None,
        "data_preprocessing.py": None,
        "feature_engineering.py": None,
        "model_training.py": None,
        "visualization.py": None,
        "utils.py": None,
    },
    "models": None,
    "dashboards": {
        "app.py": None,
        "templates": None,
    },
    "reports": {
        "figures": None,
        "final_report.pdf": None,
    },
    "logs": None,
    "scripts": {
        "run_preprocessing.py": None,
        "run_training.py": None,
        "run_dashboard.py": None,
    },
    "tests": {
        "test_data_preprocessing.py": None,
        "test_feature_engineering.py": None,
        "test_model.py": None,
    },
    ".gitignore": None,
    "README.md": None,
    "requirements.txt": None,
    "environment.yml": None,
}

# Function to create files and directories
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if content is None:
            # Create a file
            with open(path, "w") as f:
                if name.endswith(".py"):
                    f.write("# Python script\n")
                elif name.endswith(".ipynb"):
                    f.write("{}")  # Empty notebook template
                elif name.endswith(".md"):
                    f.write("# Project Documentation\n")
                elif name.endswith(".yml"):
                    f.write("name: freight_analysis_env\nchannels:\n  - defaults\n")
                elif name.endswith(".txt"):
                    f.write("# List of Python dependencies\n")
        else:
            # Create a directory
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)

# Create the project structure in the current directory
if __name__ == "__main__":
    base_path = os.getcwd()  # Current working directory
    create_structure(base_path, project_structure)
    print("Project structure created successfully in the current directory!")
