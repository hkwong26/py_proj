import pytest

def func(x):
    return x+1

def response(x):
    return f"Input {x}"

@pytest.fixture
def setup() -> int:
    return 1023

@pytest.fixture
def actingon(setup)-> str:
    results = response(setup)
    return results 

def test_answer(actingon):
    assert actingon == "Input 1023"   # Assert
    assert func(4) == 5
