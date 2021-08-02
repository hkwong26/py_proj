def inc(x):
    return x+1

def retTruth(x):
    return True

def test_answer():
    assert inc(50) == 51
    assert inc(48) == 49
    assert retTruth(3) == True
    x=10
    y=100
    assert x*10 == y
    assert x != y