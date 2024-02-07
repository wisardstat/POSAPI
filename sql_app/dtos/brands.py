from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class brand(BaseModel):
    #model_config = ConfigDict(extra='allow')
    brand_id: str | None = None
    brand_name: str | None = None
    cc_id: str | None = None

    class Config:
        orm_mode = True