from beanie import Document, Indexed
from camel_converter import to_camel


class User(Document):
    user_name: Indexed(str, unique=True)  # type: ignore
    password: str

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

    class Settings:
        name = "users"
