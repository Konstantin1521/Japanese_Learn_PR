from typing import Type, TypeVar, Generic, Sequence

from sqlalchemy import select, String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

from backend.src.models import Symbol

ModelType = TypeVar("ModelType")

class KanaService:
    def __init__(self, model: Generic[ModelType]):
        self.model = model

    async def get_all_symbols(
            self,
            session: AsyncSession,
            alphabet: str
    ) -> Sequence[Symbol]:
        stmt = select(self.model).where(self.model.alphabet == alphabet)
        result: Result = await session.execute(stmt)
        elements = result.scalars().all()
        return elements


    async def get_symbols_by_ids(
            self,
            session: AsyncSession,
            symbol_ids: list[int]
    ) -> Sequence[Symbol]:
        stmt = select(self.model).where(self.model.id.in_(symbol_ids))
        result: Result = await session.execute(stmt)
        elements = result.scalars().all()
        return elements


    async def get_kana_by_rowid(
            self,
            session: AsyncSession,
            row_id: int,
            alphabet: str,
    ) -> Sequence[Symbol]:
        stmt = select(self.model).where(self.model.row == row_id, Symbol.alphabet==alphabet)
        result: Result = await session.execute(stmt)
        elements = result.scalars().all()
        return elements


hs = KanaService(Symbol)