
from typing import Optional
from pydantic import BaseModel

class JobCreate(BaseModel):
    name: str
    salary:int


class JobUpdate(BaseModel):
    name: Optional[str] = None
    salary: Optional[int] = None
