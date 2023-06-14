from pydantic import BaseModel


class Contact(BaseModel):
    company: str
    email: str
    firstname: str
    lastname: str
    phone: str
    website: str
