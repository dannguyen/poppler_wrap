from pathlib import Path
from poppler_wrap.pdftotext import Pdftotext

PDF_PATH = Path('examples', 'docs', 'hellobye.pdf')



def test_can_ints_be_used_as_args():
    p = Pdftotext(PDF_PATH)
    p.run()
    assert p.has_run() is True
