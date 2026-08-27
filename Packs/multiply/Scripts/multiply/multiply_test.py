def test_passing():
    """This test will pass because the assertions are true."""
    assert 1 + 1 == 2
    assert "hello".upper() == "HELLO"

def test_failing():
    """This test will fail intentionally."""
    assert 1 + 1 == 3