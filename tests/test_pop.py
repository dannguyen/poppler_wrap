# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""Tests for `poppler_wrap` package."""

import pytest
from poppler_wrap.pop import Pop

def test_pop_name():
    pt = Pop('pdfwhatever')
    assert type(pt) == Pop
    assert pt.name == 'pdfwhatever'
    assert pt.command == pt.name
