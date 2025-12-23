import uuid
from pydantic import BaseModel, Field, EmailStr, ConfigDict, constr
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Модель данных пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class CreateUserRequestSchema(BaseModel):
    """
    Запрос на создание пользователя.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr
    password: constr(min_length=8)
    last_name: str
    first_name: str
    middle_name: str


class CreateUserResponseSchema(BaseModel):
    """
    Ответ с данными созданного пользователя.
    """
    user: UserSchema
