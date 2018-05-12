import pytest
import sys, os
from poppler_wrap import pop

def test_hello():
    assert 'hello' == 'hello'


def test_pop():
    p = pop.Pop('whatever')
    assert type(p) == pop.Pop
    assert p.command == 'whatever'
    assert p.name == 'whatever'
