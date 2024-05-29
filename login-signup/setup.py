import sys
from cx_Freeze import setup, Executable
import os

# Path to your Python script
script = "main.py"

# Path to the directory containing login_style.json
json_styles_dir = "json-styles"

# List of files to include in the build
include_files = [
    (os.path.join(json_styles_dir, "login_style.json"), "json-styles/login_style.json"),
    # Add more files if needed
]

# Build options
build_exe_options = {
    "packages": ["PySide6"],
    "include_files": include_files,
}

# Setup configuration
setup(
    name="MyApp",
    version="1.0",
    description="My PyQt application",
    options={"build_exe": build_exe_options},
    executables=[Executable(script=script, base=None)],
)

# Rename the generated executable file
exe_path = os.path.join("build", "exe.win-amd64-3.9", "main.exe")
new_name = "main.exe"
os.rename(exe_path, new_name)
