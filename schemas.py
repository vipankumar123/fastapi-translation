# from typing import List, Union
from pydantic import BaseModel

class LeadSchema(BaseModel):
    first_name: str
    last_name: str
    work_phone: str

    class Config:
        orm_mode = True


