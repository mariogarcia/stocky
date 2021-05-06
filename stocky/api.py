from fastapi import APIRouter

from stocky.account.command.api import router as account_capi
from stocky.account.query.api import router as account_qapi

api_router = APIRouter()

# account command/query
api_router.include_router(account_capi)
api_router.include_router(account_qapi)