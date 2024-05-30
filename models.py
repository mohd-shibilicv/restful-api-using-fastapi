from pydantic import BaseModel, Field, field_validator, EmailStr


class UserRequestModel(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=0)

    @field_validator('username')
    def validate_username(cls, value):
        if not value.isalnum():
            raise ValueError('Username must be alphanumeric')
        return value


class UserResponseModel(BaseModel):
    id: int
    username: str
    email: str
    age: int
