import base64


def is_base64(sb):
    """
    Check if message is base64, based on this [StackOverflow](https://stackoverflow.com/a/45928164) answer
    """
    try:
        if not sb:
            return False
        if isinstance(sb, str):
            sb_bytes = bytes(sb, "ascii")
        elif isinstance(sb, bytes):
            sb_bytes = sb
        else:
            raise ValueError("Argument must be string or bytes")
        return base64.b64encode(base64.b64decode(sb_bytes)) == sb_bytes
    except Exception:
        return False
