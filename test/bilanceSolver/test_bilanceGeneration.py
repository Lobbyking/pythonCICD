import numpy as np
import pytest
from hypothesis import given, strategies as st

import mtb.bilanceSolver.bilanceGeneration as bilanceGen


@pytest.fixture
def input_value():
    return [4, 6, 7]


def increase_array_value(arr):
    return [x + 1 for x in arr]


def increase_compare_value(comp):
    return comp + 5


def test_generateUnknownFstruct():
    assert type(bilanceGen.generateUnknownFstruct()) == type({'temp': np.nan, 'press': np.nan,
                                                              'concStd': np.array([np.nan]),
                                                              'massFlow': {'liquid': np.nan, 'gas': np.nan},
                                                              'enthFlow': {'liquid': np.nan, 'gas': np.nan},
                                                              'fractions': {'mMultPhase': np.array([np.nan]),
                                                                            'Vgas': np.array([np.nan]),
                                                                            'mGas': np.array([np.nan])},
                                                              'species': {'comp': np.nan, 'load': np.nan}})
    assert str(bilanceGen.generateUnknownFstruct()) == str({'temp': np.nan, 'press': np.nan,
                                                            'concStd': np.array([np.nan]),
                                                            'massFlow': {'liquid': np.nan, 'gas': np.nan},
                                                            'enthFlow': {'liquid': np.nan, 'gas': np.nan},
                                                            'fractions': {'mMultPhase': np.array([np.nan]),
                                                                          'Vgas': np.array([np.nan]),
                                                                          'mGas': np.array([np.nan])},
                                                            'species': {'comp': np.nan, 'load': np.nan}})


@pytest.mark.parametrize(
    'input, expected', [([4, 20, -7], 17), ([3, 2, 5, 7], 17), ([1, 2, 3, 4, 5, 6, 7, 8], 36)]
)
def test_addNumbers(input, expected):
    """Sum from input array should equal expected"""
    # print(f'Input: ({input}), Expected: ({expected})')
    assert bilanceGen.addNumbers(input) == expected


def test_addNumbersWithDynamicValues():
    x = [1, 2, 3, 4, 5]
    y = 15
    while 10 not in x:
        assert bilanceGen.addNumbers(x) == y
        x = increase_array_value(x)
        y = increase_compare_value(y)


def test_addNumbersWithDynamicValuesFail():
    x = [1, 2, 3, 4, 5]
    y = 15
    while True:
        if 10 in x: x.append(1)
        assert bilanceGen.addNumbers(x) == y
        x = increase_array_value(x)
        y = increase_compare_value(y)


@pytest.mark.odd
def test_checkIfOddFail():
    x = 1
    try:
        while True:
            bilanceGen.checkIfOdd(x)
            x = increase_compare_value(x)
    except Exception as e:
        assert False, f'Error occurred input value: {x}, raised exception: {e}'


@pytest.mark.odd
@given(st.integers(-500, 500).filter(lambda x: x != 0).filter(lambda x: x % 2 != 0))
def test_checkIfOddPass(x):
    try:
        assert bilanceGen.checkIfOdd(x) == True
    except Exception as e:
        assert False, f'Error occurred input value: {x}, raised exception: {e}'
