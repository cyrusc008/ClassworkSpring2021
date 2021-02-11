import pytest

@pytest.mark.parametrize("value, expected", [(70, "Normal"), 
                        (50, "Borderline Low"), (20, "Low")])
def test_analyzeHDL(value, expected):
    from blood_tests import analyzeHDL
    value = analyzeHDL(value)
    assert value == expected
