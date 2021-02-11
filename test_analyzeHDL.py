from blood_tests import analyzeHDL

def test_analyzeHDL():
    value = analyzeHDL(70)
    assert value == "Normal"
