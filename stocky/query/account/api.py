import uuid
from fastapi import APIRouter

router = APIRouter()

@router.get("/account/{id}")
async def account(id: str):
    account_id = uuid.UUID(id)
    # here to query producer created views
    return account_id