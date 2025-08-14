import sys
from pathlib import Path
from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession


sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from backend.src.models import db_helper
from backend.src.schemas import symbol_schema
from backend.src.services.crud_alphabet import hs
from backend.utils.config import settings

router = APIRouter(tags=["hiragana"])

@router.get('/hiragana', response_model=List[symbol_schema.SymbolRead])
async def all_get_hiragana(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
) -> List[symbol_schema.SymbolRead]:
    try:
        hiragana = await hs.get_all_symbols(
            session=session,
            alphabet=settings.kana.hg,
        )
        if not hiragana:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No hiragana symbols found"
            )

        return hiragana
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post('/hiragana/')
async def get_hiragana_by_id(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        symbol_ids: List[int],
) -> list[symbol_schema.SymbolRead]:
    try:
        symbols = await hs.get_symbols_by_ids(
            session=session,
            symbol_ids=symbol_ids,
        )
        if not symbols:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No symbols found with provided IDs"
            )
        return symbols

    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e))

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get('/hiragana/{row}')
async def get_hiragana_by_row(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        row: int,
):
    try:
        symbols = await hs.get_kana_by_rowid(
            session=session,
            row_id=row,
            alphabet=settings.kana.hg
        )
        if not symbols:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No hiragana found for row {row}"
            )
        return symbols
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )