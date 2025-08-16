from sqlalchemy import String, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from .symbol import Symbol


class Grammar(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    kanji: Mapped[str] = mapped_column(String, nullable=False)
    hiragana: Mapped[str] = mapped_column(String, nullable=False)
    translation: Mapped[str] = mapped_column(String, nullable=False)
    romaji: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)
    starting_symbol_id: Mapped[int] = mapped_column(Integer, ForeignKey('symbols.id'), nullable=True)
    __table_args__ = (
        CheckConstraint("category = 'particle'"),
    )