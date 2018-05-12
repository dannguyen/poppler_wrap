"""
https://www.mankier.com/1/pdfinfo
"""

from pathlib import Path
from poppler_wrap.pop import Pop

SAMPLE_PATH = Path('examples', 'pdfs', 'facebook-ira-ad.pdf')

class Pdfinfo(Pop):
    def __init__(self, infile=SAMPLE_PATH):
