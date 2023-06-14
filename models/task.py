from pydantic import BaseModel
from typing import List


class Task(BaseModel):
    name: str
    description: str
    assignees: List[str]
    team_id: str

