# See LICENSE.txt for licensing terms

# TODO(stephenfin): Switch to 'importlib.metadata' once we drop support for
# Python < 3.8
import importlib.metadata

try:
    version = importlib.metadata.version('rst2pdf')
except importlib.metadata.PackageNotFoundError:
    version = None
