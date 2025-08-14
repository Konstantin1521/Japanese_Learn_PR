from typing import Sequence, Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

from backend.src.models import Symbol


class HiraganaService:
    @staticmethod
    async def get_hiragana(session: AsyncSession) -> Sequence[Symbol]:
        stmt = select(Symbol).where(Symbol.alphabet=="hiragana")
        result: Result = await session.execute(stmt)
        elements = result.scalars().all()
        return elements

    @staticmethod
    async def get_hiragana_symbol(session: AsyncSession, symbol_ids: list[int]) -> Sequence[Symbol]:
        stmt = select(Symbol).where(Symbol.id.in_(symbol_ids))
        result: Result = await session.execute(stmt)
        elements = result.scalars().all()
        return elements

    @staticmethod
    async def get_hiragana_by_rowid(session: AsyncSession, row_id: int) -> Sequence[Symbol]:
        stmt = select(Symbol).where(Symbol.row == row_id, Symbol.alphabet=="hiragana")
        result: Result = await session.execute(stmt)
        elements = result.scalars().all()
        return elements



hs = HiraganaService()