from camel_converter.pydantic_base import CamelBase


class Token(CamelBase):
    access_token: str
    token_type: str


class TokenPayload(CamelBase):
    sub: str | None = None
