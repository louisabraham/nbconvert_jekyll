# file __init__.py
import os
import os.path

from traitlets import default
from traitlets.config import Config
from nbconvert.exporters.html import HTMLExporter


class JekyllExporter(HTMLExporter):
    """
    My custom exporter
    """

    @property
    def template_path(self):
        """
        We want to inherit from HTML template, and have template under
        `./templates/` so append it to the search path. (see next section)
        """
        return super().template_path + [os.path.join(os.path.dirname(__file__), "templates")]

    @default('template_file')
    def _template_file_default(self):
        return 'full_ga'
