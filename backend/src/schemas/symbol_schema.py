from pydantic import BaseModel
from pydantic import ConfigDict


class SymbolBase(BaseModel):
    symbol: str
    romaji: str
    alphabet: str
    row: int



class SymbolRead(SymbolBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
