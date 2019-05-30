# This file must be in the notebooks directory.
# It allows us to import python modules from elsewhere within this project.

import sys
import os

module_path = os.path.abspath(os.path.join(os.pardir, os.pardir))
if module_path not in sys.path:
    sys.path.append(module_path)
