from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class model(BaseModel):
    #model_config = ConfigDict(extra='allow')
    model_id: str | None = None
    model_name: str | None = None
    cc_id: str | None = None

    class Config:
        orm_mode = True