"""
Settings used by sample_project.

This consists of the general production settings, with an
optional import of any local settings
"""

# Import production settings.
from sample_project.settings.production import *

# Import optional local settings.
try:
    from sample_project.settings.local import *
except ImportError:
    pass