from sqlalchemy import String, Integer, CheckConstraint, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base
from .symbol import Symbol

class Words(Base):
    kanji: Mapped[str] = mapped_column(String, nullable=False)
    hiragana: Mapped[str] = mapped_column(String, nullable=False)
    translation: Mapped[str] = mapped_column(String, nullable=False)
    romaji: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)
    starting_symbol_id: Mapped[int] = mapped_column(Integer, ForeignKey('symbols.id'), nullable=True)
    __table_args__ = (
        CheckConstraint("category IN ('verb', 'subject', 'predicate', 'adverb', 'adjective', 'phrase')"),
    )