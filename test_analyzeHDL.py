from blood_tests import analyzeHDL

def test_analyzeHDL1():
    value = analyzeHDL(70)
    assert value == "Normal"

def test_analyzeHDL2():
    value = analyzeHDL(50)
    assert value == "Borderline Low"

def test_analyzeHDL3():
    value = analyzeHDL(20)
    assert value == "Low"