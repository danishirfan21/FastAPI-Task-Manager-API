from pydantic import BaseModel, EmailStr

# User Pydantic schemas


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserInDB(UserBase):
    id: int
    hashed_password: str

    class Config:
        orm_mode = True
