from app.utils import is_base64


def test_message_is_base64():
    assert not is_base64("not base64")
    assert is_base64("dGVzdA==")  # dGVzdA== = "test" in base64
