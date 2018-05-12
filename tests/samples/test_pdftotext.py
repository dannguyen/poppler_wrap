from pathlib import Path
from poppler_wrap.pdftotext import Pdftotext

PDF_PATH = Path('examples', 'docs', 'hellobye.pdf')


def test_sample_exists():
    assert PDF_PATH.exists() == True

def test_args():
    p = Pdftotext(PDF_PATH)
    args = p._makeargs()
    assert type(args) is tuple
#    assert args == ('pdftotext', '-layout', '-f', 1, '-l', 1, PDF_PATH, '-')

def test_params():
    p = Pdftotext(PDF_PATH)
    parms = p.params
    assert type(parms) is tuple
    assert parms ==  ('-layout', '-f', 1, '-l', 1, PDF_PATH, '-')


def test_statement():
    p = Pdftotext(PDF_PATH)
    s = p.statement()
    assert s == 'pdftotext -layout -f 1 -l 1 {} -'.format(PDF_PATH)

def test_first_page_run():
    """by default, pdftotext only converts the very first page"""
    p = Pdftotext(PDF_PATH)
    p.run()
    assert p.has_run() is True
    assert 'hello' in p.text
    assert '1' in p.text


def test_page_pick():
    p = Pdftotext(PDF_PATH, page_number=2)
    p.run()
    assert 'world' in p.text
    assert '2' in p.text
