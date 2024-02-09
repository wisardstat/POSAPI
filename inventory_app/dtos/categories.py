from typing import List, Optional

from pydantic import BaseModel


class categories(BaseModel):
    group_id: str
    group_name: str
    group_sup: str | None = None
    group_type: str | None = None
    cc_id: str

    class Config:
        orm_mode = True