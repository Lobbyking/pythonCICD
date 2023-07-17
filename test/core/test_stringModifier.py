import importlib
import string

import pytest
from hypothesis import given, strategies as st

from mtb.core.stringModifier import StringModifier


@pytest.fixture
def stringModifier():
    sm = StringModifier()
    return sm


def test_reverseString(stringModifier):
    x = 'flo'
    result = stringModifier.reverseString(x)
    assert result == 'olf'
    assert len(result) == len(x)
    assert sorted(result) == sorted(x)


@given(x=st.text(alphabet=string.ascii_letters))
def test_reverseStringHypothesis(x):
    sm = StringModifier()
    result = sm.reverseString(x)
    print(f'Input: ({x}), Output: ({result})')
    assert len(result) == len(x)
    assert result == x[::-1]
    assert sorted(result) == sorted(x)
