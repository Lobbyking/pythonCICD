import datetime
import string

import pytest
import random
from hypothesis import given, strategies as st
from hypothesis.strategies import composite

import mtb.components.component as comp
from mtb.components.project import Project


@pytest.fixture
def input_value():
    return 8


@pytest.mark.filterwarnings
def test_calc(input_value):
    result_str = ''
    for i in range(4):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for y in range(input_value))
        assert comp.calc(result_str) == result_str[::-1]

    with pytest.raises(ValueError, match=r'^String is to short$'):
        comp.calc('test')


names = st.text(alphabet=string.ascii_letters, min_size=5, max_size=20)
managers = st.text(alphabet=string.ascii_letters, min_size=2, max_size=4)
creationDates = st.dates(min_value=datetime.date(2000, 1, 1))


@composite
def projects(draw):
    name = draw(names)
    manager = draw(managers)
    creationDate = draw(creationDates)
    return Project(name, manager, creationDate)


@given(projects())
def test_projectInputValues(projects):
    print(f'Input: ({projects.toString()})')
    assert len(projects.name) >= 5
    assert len(projects.name) <= 20
    assert str.isalpha(projects.name) == True
    assert len(projects.manager) >= 2
    assert len(projects.manager) <= 4
    assert str.isalpha(projects.manager) == True
    assert projects.creationDate >= datetime.date(2000, 1, 1)
