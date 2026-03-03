import my_package.my_module as mod
import pytest

# fixture is a function that
# can run set up (e.g. connecting to a db)
# and returns a result

@pytest.fixture
def setup():
    testdata = [1, 2, 3, 4, 5, 6, 7]
    return testdata

@pytest.fixture
def alternate_setup():
    return ['Tom', 'Lane']

def test_add(alternate_setup):
    result = mod.add(alternate_setup)
    assert result == 28

def test_subtract(alternate_setup):
    result = mod.subtract(alternate_setup)
    assert result == -28