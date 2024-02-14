from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class type_doc_list(BaseModel):
    #model_config = ConfigDict(extra='allow')
    type_doc_id: str | None = None
    type_doc_name: str | None = None
    #cc_id: str | None = None

    class Config:
        orm_mode = True