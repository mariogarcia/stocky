from fastapi import APIRouter

from stocky.common.evs import accounts
from stocky.common.evs.application import AccountApplication
from stocky.command.account.payloads import (CreateAccountPayload, DepositPayload, WithdrawalPayload)

# router for account-related URIs
router = APIRouter()

@router.post("/account")
async def create_account(info: CreateAccountPayload):
    '''
    creates a new account
    '''
    return accounts.create_account(info.name)

@router.post("/account/{id}/deposit")
async def deposit(id: str, deposit: DepositPayload):
    '''
    adds a deposit in a specific account
    '''
    accounts.deposit(id, deposit=deposit)

@router.post("account/{id}/withdrawal")
async def withdrawal(withdrawal: WithdrawalPayload):
    '''
    does a withdrawal from a specific account
    '''
    accounts.withdrawal(withdrawal)