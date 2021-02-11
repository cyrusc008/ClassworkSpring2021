def test_fever_check():
    from temperature_check import fever_check
    data = [98, 98.5, 100.5, 99]
    answer = fever_check(data)
    expected = True
    assert answer == expected
