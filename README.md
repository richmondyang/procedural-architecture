# Procedural Architecture
Blender toolset for procedural layout and building generation

## Development Setup
### Initial Setup
This project is developed in VS Code

Ensure the latest version of Python and Blender are installed.

Opening up the project in VS Code should automatically prompt for recommended VS Code extensions to be downloaded. The necessary settings for these extensions will also be configured once downloaded.

Once these have been downloaded:
- Use ```Ctrl+Shift+P```.
- Type out "Blender: Start".
- Select a Blender executable. Make sure the executable selected is the latest version of Blender. Confirm if prompted by VS Code to make the selected executable the default.
- Once Blender launches, go to "Edit > Preferences > Display" and enable "Developer Extras" and "Python Tooltips".

To ensure setup has worked properly, check that these paths exist:
- ```${CONFIG}/extensions/vscode_development/procedural_architecture```
- ```${CONFIG}/scripts/modules```

Where ```${CONFIG}``` is the path where the selected Blender executable lives.

Once VS Code has been configured, set up and activate a virtual environment for downloading python packages:

Windows (PowerShell)  
```
python -m venv .venv  
```

Windows (Command Prompt)  
```
python -m venv .venv  
```

macOS / Linux  
```
python3 -m venv .venv 
```

Once a virtual environment has been set up, install these packages: 
```
pip install fake-bpy-module
```

### Every development session
Make sure your virtual environment is active each session:

Windows (PowerShell)  
```
.venv\Scripts\Activate.ps1
```

Windows (Command Prompt)  
```
.venv\Scripts\activate.bat
```

macOS / Linux  
```
source .venv/bin/activate
```

Deactivate your virtual environment after each session:

Windows / macOS / Linux
```
deactivate
```

### Running Tests
To run the test suite, use:
```
${CONFIG}/blender.exe --background --factory-startup --python tests/__init__.py
```
Where ```${CONFIG}``` is where your blender executable lives.
 
**NOTE: Tests must follow the naming scheme ```test_*.py```**
