# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""Test that test pdftotext's OOPness even without opening a PDF"""

import pytest
from poppler_wrap.pdftotext import Pdftotext


def test_has_infile():
    pt = Pdftotext('somefile.pdf')
    assert pt.infile  == 'somefile.pdf'

def test_requires_infile():
    with pytest.raises(TypeError):
        p = Pdftotext()

def test_default_attrs():
    pt = Pdftotext('what')
    assert type(pt) == Pdftotext
    assert pt.layout == '-layout'
    assert pt.page_number == 1


def test_params():
    pt = Pdftotext('nuff')
    assert pt.params == ('-layout', '-f 1', '-l 1', 'nuff', '-',)


def test_pdftotext_command():
    pt = Pdftotext('null')
    assert pt.name == 'pdftotext'
    assert pt.command == 'pdftotext'



def test_to_dict():
    dp = Pdftotext('somefile.pdf', page_number=5).to_dict()
    assert dp['hi'] == 'bye'
    assert dp['page_number'] == 5

