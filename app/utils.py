import base64
import json
from fastapi import FastAPI
from pathlib import Path

from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html


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


def generate_static_docs(app: FastAPI, output_dir: str):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    openapi_schema = app.openapi()
    with open(f"{output_dir}/openapi.json", "w") as f:
        json.dump(openapi_schema, f, indent=2)

    swagger_ui = get_swagger_ui_html(
        openapi_url="./openapi.json",
        title=f"{app.title} - Swagger UI",
    ).body.decode("utf-8")
    with open(f"{output_dir}/docs.html", "w") as f:
        f.write(swagger_ui)
    redoc = get_redoc_html(
        openapi_url="./openapi.json",
        title=f"{app.title} - ReDoc",
    ).body.decode("utf-8")
    with open(f"{output_dir}/redoc.html", "w") as f:
        f.write(redoc)
