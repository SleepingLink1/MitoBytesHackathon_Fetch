from pydantic import BaseModel, EmailStr
from typing import Optional


class Address(BaseModel):
    address1: str
    address2: Optional[str] = None
    city: str
    state: str
    postcode: str
    country: str


class ContactInfo(BaseModel):
    email: EmailStr
    phone: str
    address: Address