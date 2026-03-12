# Day 22: Virtual Environments
# notes about isolating project packages using venv and pip

import sys

# inspect python execution environment
print("Python path:", sys.executable)
print("Running inside venv?", hasattr(sys, 'real_prefix') or (sys.base_prefix != sys.prefix))

# exercise 1: print sys.path elements
print("sys.path paths:")
for path in sys.path[:3]:
    print("  ", path)

# challenge: check if package is installed programmatically
def check_library_installed(lib_name):
    try:
        __import__(lib_name)
        return True
    except ImportError:
        return False

print("Is NumPy installed?", check_library_installed("numpy"))
print("Is Requests installed?", check_library_installed("requests"))
print("Is bogus package installed?", check_library_installed("non_existent"))
