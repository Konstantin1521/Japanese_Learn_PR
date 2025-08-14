import sys
from pathlib import Path
from typing import Annotated, List

import fastapi
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import PydanticSchemaGenerationError
from sqlalchemy.ext.asyncio import AsyncSession


sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from backend.src.models import db_helper
from backend.src.schemas import symbol_schema
from backend.src.services.crud_alphabet import hs

router = APIRouter(tags=["hiragana"])

@router.get('/hiragana', response_model=List[symbol_schema.SymbolRead])
async def all_get_hiragana(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
) -> List[symbol_schema.SymbolRead]:
    try:
        hiragana = await hs.get_hiragana(session=session)

    except (RuntimeError, PydanticSchemaGenerationError):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Validated error"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return hiragana


@router.post('/hiragana/')
async def get_hiragana_by_id(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        symbol_ids: List[int],
) -> list[symbol_schema.SymbolRead]:
    try:
        symbols = await hs.get_hiragana_symbol(session=session, symbol_ids=symbol_ids)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Bad request')
    return symbols

@router.get('/hiragana/{row}')
async def get_hiragana_by_row(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        row: int,
):
    try:
        symbols = await hs.get_hiragana_by_rowid(session=session, row_id=row)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Bad request'
        )

    if len(symbols) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Not found'
        )

    return symbols