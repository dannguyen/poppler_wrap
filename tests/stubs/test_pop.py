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


def test_destructure():
    pt = Pop('x', 'y')
    assert type(pt.params) is tuple
    assert type(pt._makeargs()) is tuple


def test_statement():
    pt = Pop('pdffoo', 'x', 'y')
    assert pt.statement() == 'pdffoo x y'


def test_dead_pop():
    pt = Pop('dead')
    assert type(pt.params) is tuple
    assert not pt.has_run()


def test_run_pop():
    _foo = 'echo'
    _parms = 'hello'
    pt = Pop('echo', 'hello')
    pt.run()

    assert pt.has_run() is True
    assert pt.command == 'echo'
    assert pt.params == ('hello',)
    assert pt.text.strip() == 'hello'
    assert pt.content.strip() == b'hello'


def test_pop_metaargs():
    pt = Pop('wat')
    args = pt._makeargs()
    assert type(args) is tuple



def test_non_run_pop_to_dict():
    dp = Pop('whatev').to_dict()
    assert dp['name'] == 'whatev'
    assert dp['has_run'] == False
    assert dp['text'] == None
    assert dp['params'] == tuple()

