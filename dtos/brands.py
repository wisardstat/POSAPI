from typing import List, Optional

from pydantic import BaseModel


class brand(BaseModel):
    brand_id: str
    brand_name: str
    cc_id: str

    class Config:
        orm_mode = True