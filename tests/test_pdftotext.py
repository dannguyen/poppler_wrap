# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""Tests for `poppler_wrap` package."""

import pytest
from pathlib import Path
from poppler_wrap.pdftotext import Pdftotext

SAMPLE_PDF_PATH= Path('examples', 'pdfs', 'facebook-ira-ad.pdf')

def test_sample_exsts():
    assert SAMPLE_PDF_PATH.exists() == True

def test_pdftotext_command():
    pt = Pdftotext('somefile.pdf')
    assert type(pt) == Pdftotext
    assert pt.infile  == 'somefile.pdf'
    assert pt.name == 'pdftotext'
    # assert pt.name == 'pdftotext'
    # assert pt.command == 'pdftotext'
