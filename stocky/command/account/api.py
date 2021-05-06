from fastapi import APIRouter

from stocky.common.evs import accounts
from stocky.common.evs.application import AccountApplication
from stocky.command.account.payloads import (CreateAccountPayload, DepositPayload, WithdrawalPayload)

# router for account-related URIs
router = APIRouter()

@router.post("/account")
async def create_account(payload: CreateAccountPayload):
    '''
    creates a new account
    '''
    return accounts.create_account(payload.name)

@router.post("/account/{id}/deposit")
async def deposit(id: str, payload: DepositPayload):
    '''
    adds a deposit in a specific account
    '''
    accounts.deposit(id, amount=payload.amount)

@router.post("/account/{id}/withdrawal")
async def withdrawal(id: str, payload: WithdrawalPayload):
    '''
    does a withdrawal from a specific account
    '''
    accounts.withdrawal(id, amount=payload.amount)