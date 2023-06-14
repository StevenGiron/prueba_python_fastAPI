import hubspot
from fastapi import APIRouter, Depends
from hubspot.crm.contacts import SimplePublicObjectInputForCreate, ApiException
from datetime import datetime
from sqlalchemy.orm import Session

from models.contact import Contact
from models.user_log import UserLog
from middlewares.db import get_db


contact = APIRouter()
token = "pat-na1-bfa3f0c0-426b-4f0e-b514-89b20832c96a"

hubspot_client = hubspot.Client.create(access_token=token)


@contact.post('/create_contact')
async def create_contact(contact: Contact, db: Session = Depends(get_db())):

    datetime_api_call = datetime.now()
    log_entry = UserLog(timestamp=datetime_api_call)
    db.add(log_entry)
    db.commit()

    properties = {
        "company": contact.company,
        "email": contact.email,
        "firstname": contact.firstname,
        "lastname": contact.lastname,
        "phone": contact.phone,
        "website": contact.website
    }
    simple_public_object_input_for_create = SimplePublicObjectInputForCreate(properties=properties, associations=[])
    try:
        api_response = hubspot_client.crm.contacts.basic_api.create(
            simple_public_object_input_for_create=simple_public_object_input_for_create)
        print(api_response)
    except Exception as e:
        return {"error": str(e)}
