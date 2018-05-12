"""
# https://www.mankier.com/1/pdftotext
"""

from pathlib import Path
from poppler_wrap.pop import Pop


class Pdftotext(Pop):
    def __init__(self, infile,
                       page_number=1,
                       layout='-layout',):

        __name = 'pdftotext'
        self.infile = infile
        self.page_number = page_number
        self.layout = layout
        _parms = (
                    self.layout,
                    # add first and last page arguments
                   '-f',
                   self.page_number,
                   '-l',
                   self.page_number,
                   self.infile,
                   '-'
                   )
        super().__init__(__name, *_parms)


    def to_dict(self):
        d = super().to_dict()
        d['page_number'] = self.page_number
        d['hi'] = 'bye'
        return d
