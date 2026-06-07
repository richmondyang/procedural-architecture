# Procedural Architecture
Blender toolset for procedural layout and building generation

## Development Setup
### Initial Setup
This project is developed in VS Code

Ensure the latest version of Python and Blender are installed

Opening up the project in VS Code should automatically prompt for recommended VS Code extensions to be downloaded. The necessary settings for these extensions will also be configured once downloaded

Once these have been downloaded:
- Use ```Ctrl+Shift+P```.
- Type out "Blender: Start".
- Select a Blender executable. Make sure the executable selected is the latest version of Blender. Confirm if prompted by VS Code to make the selected executable the default.
- Once Blender launches, go to "Edit > Preferences > Display" and enable "Developer Extras" and "Python Tooltips"

To ensure setup has worked properly, check that these paths exist:
- ```${CONFIG}/extensions/vscode_development/procedural_architecture```
- ```${CONFIG}/scripts/modules```

Where ```${CONFIG}``` is the path where the selected Blender executable lives

### Every development session
Set up a virtual environment for downloading python packages

Windows (PowerShell)  
```
python -m venv .venv  
.venv\Scripts\Activate.ps1
```

Windows (Command Prompt)  
```
python -m venv .venv  
.venv\Scripts\activate.bat
```

macOS / Linux  
```
python3 -m venv .venv 
source .venv/bin/activate
```

Once a virtual environment has been setup for the current session, install these packages:  
```
pip install fake-bpy-module
```
