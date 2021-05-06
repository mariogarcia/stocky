from fastapi import APIRouter

from stocky.command.account.api import router as account_capi
from stocky.query.account.api import router as account_qapi

api_router = APIRouter()

# account command/query
api_router.include_router(account_capi)
api_router.include_router(account_qapi)