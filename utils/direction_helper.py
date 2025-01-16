import os

# Define the directory structure
directory_structure = {
    "project_root": {
        "audio_processing": [
            "whisper_asr.py",
            "audio_utils.py"
        ],
        "text_analysis": [
            "deepseek_client.py",
            "summary_utils.py"
        ],
        "app": {
            "app.py": None,
            "templates": [],
            "static": []
        },
        "data": {
            "uploads": [],
            "outputs": []
        },
        "requirements.txt": None,
        "config.py": None,
        "README.md": None
    }
}

# Base path
base_path = "./"

# Recursive function to create directories and files
def create_structure(base, structure):
    for name, content in structure.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):  # It's a directory
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):  # Directory with files
            os.makedirs(path, exist_ok=True)
            for file_name in content:
                open(os.path.join(path, file_name), 'a').close()
        else:  # It's a file
            open(path, 'a').close()

# Create the directory structure
create_structure(base_path, directory_structure)

print("Directory structure created successfully!")
