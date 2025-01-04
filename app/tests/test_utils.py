from app.utils import is_base64


def test_message_is_base64():
    assert not is_base64("not base64")
    assert is_base64("dGVzdA==")  # dGVzdA== = "test" in base64


def test_message_is_base64():
    assert not is_base64("not base64")
    assert is_base64("dGVzdA==")  # dGVzdA== = "test" in base64


def test_bytes_input():
    assert is_base64(b"dGVzdA==")  # b"dGVzdA==" = "test" in base64
    assert not is_base64(b"not base64")


def test_invalid_input():
    assert not is_base64(12345)  # Invalid input type
    assert not is_base64(None)  # Invalid input type


def test_empty_string():
    assert not is_base64("")  # Empty string is not base64


def test_special_characters():
    assert not is_base64("!@#$%^&*()")  # Special characters are not base64
