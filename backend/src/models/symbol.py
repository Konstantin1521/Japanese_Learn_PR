from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base

class Symbol(Base):

    symbol: Mapped[str] = mapped_column(String, unique=True, index=True)
    romaji: Mapped[str] = mapped_column(String, index=True)
    alphabet: Mapped[str] = mapped_column(String)
    row: Mapped[str] = mapped_column(String)


