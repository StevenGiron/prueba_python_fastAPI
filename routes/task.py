import requests
from fastapi import APIRouter, Depends
from datetime import datetime
from sqlalchemy.orm import Session
from models.task_log import TaskLog
from middlewares.db import get_db

from models.task import Task

task = APIRouter()

token = 'pk_3182376_Q233NZDZ8AVULEGGCHLKG2HFXWD6MJLC'
click_up_url = 'https://api.clickup.com/api/v2/list/{900200532843}/task'


@task.post('/create_task')
async def sync_contacts(task: Task, db: Session = Depends(get_db())):

    datetime_api_call = datetime.now()
    log_entry = TaskLog(timestamp=datetime_api_call)
    db.add(log_entry)
    db.commit()

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get('https://api.hubapi.com/crm/v3/objects/contacts', headers=headers).json()

    if 'results' in response:
        ids = [result["id"] for result in response['results']]

    query = {
        "custom_task_ids": "true",
        "team_id": task.team_id
    }

    payload = {
        "name": task.name,
        "description": task.description,
        "assignees": ids,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "YOUR_API_KEY_HERE"
    }
    try:
        response = requests.post(click_up_url, json=payload, headers=headers, params=query)
        data = response.json()
        return data
    except Exception as e:
        return {"error": str(e)}

