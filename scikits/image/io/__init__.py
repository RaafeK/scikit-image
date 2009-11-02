"""Utilities to read and write images in various formats."""

from _plugins import load as load_plugin
from _plugins import use as use_plugin
from _plugins import available as plugins

# Add this plugin so that we can read images by default
load_plugin('pil')

from sift import *
from collection import *

from io import *
