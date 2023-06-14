from fastapi import FastAPI
from routes.contact import contact
from routes.task import task

app = FastAPI()

app.include_router(contact)
app.include_router(task)
