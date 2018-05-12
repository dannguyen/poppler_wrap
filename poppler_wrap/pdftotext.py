"""
# https://www.mankier.com/1/pdftotext
"""

from pathlib import Path
from poppler_wrap.pop import Pop

SAMPLE_PATH = Path('examples', 'pdfs', 'facebook-ira-ad.pdf')

class Pdftotext(Pop):
    def __init__(self, infile=SAMPLE_PATH,
                       layout_type='-layout',
#                        output_path='-', stdout_type=sb.PIPE
                        ):
        __name = 'pdftotext'
        self.infile = infile
        self.layout_type = layout_type
        super().__init__(__name, self.layout_type, infile)


