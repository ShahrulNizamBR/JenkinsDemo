import pytest
from helloworld import *

#This is a test case

def test_hello():
    result=hello()
    assert result == 'Hello world'
