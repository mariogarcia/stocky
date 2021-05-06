import uuid
from fastapi import APIRouter
from stocky.common.evs import accounts

router = APIRouter()

@router.get("/account/{id}")
async def account(id: str):
    account_id = uuid.UUID(id)
    return accounts.info(account_id)