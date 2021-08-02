import pytest

def f():
    raise SystemExit()

def test_mytest():
    with pytest.raises(SystemExit):
        f()

        