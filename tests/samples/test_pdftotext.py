from pathlib import Path
from poppler_wrap.pdftotext import Pdftotext

PDF_PATH = Path('examples', 'docs', 'hellobye.pdf')


def test_sample_exists():
    assert PDF_PATH.exists() == True

def test_params():
    p = Pdftotext(PDF_PATH)
    assert p.params == ('-layout',
                         '-f 1',
                         '-l 1',
                         PDF_PATH,
                         '-',)
def test_statement():
    p = Pdftotext(PDF_PATH)
    s = p.statement()
    assert s == 'pdftotext -layout -f 1 -l 1 {} -'.format(PDF_PATH)

def test_text_run():
    p = Pdftotext(PDF_PATH)
    p.run()
    assert p.has_run() is True
    assert p.text == 'a'

# def test_default_first_page():
#     p = Pdftotext(PDF_PATH)
#     p.run()
#     assert p.text
# #    assert p.text == 'Hello'
