import importlib
import sys
from importlib import metadata
 
print(f"Python: {sys.version.split()[0]}")
print(f"Executable: {sys.executable}")
 
try:
    import concordia
    print(f"concordia imported from: {concordia.__file__}")
except ImportError as e:
    print(f"FAILED to import concordia: {e}")
    sys.exit(1)
 
try:
    print(f"gdm-concordia version: {metadata.version('gdm-concordia')}")
except metadata.PackageNotFoundError:
    print("Package metadata for 'gdm-concordia' not found (may be a source/editable install).")
 
submodules = [
    "concordia.agents.entity_agent",
    "concordia.language_model.language_model",
    "concordia.typing.entity",
]
 
for name in submodules:
    try:
        importlib.import_module(name)
        print(f"OK:     {name}")
    except Exception as e:
        print(f"FAILED: {name} -> {type(e).__name__}: {e}")
 