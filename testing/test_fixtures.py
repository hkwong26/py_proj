import pytest

def output(x):
    return "Output {cata}".format(**x)

@pytest.fixture
def variable():
    return {"cata" : "values"}

def test_fixIn(variable):
    assert output(variable) == "Output values"