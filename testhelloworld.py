import pytest
from helloworld import *

def test_hello():
    result=hello()
    assert result == 'Hello world'
