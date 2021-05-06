from fastapi import APIRouter, BackgroundTasks

from stocky.account.evs import accounts
from stocky.account.evs.application import AccountApplication
from stocky.account.command.producer import account_producer
from stocky.account.command.payloads import (CreateAccountPayload, DepositPayload, WithdrawalPayload)

# router for account-related URIs
router = APIRouter()

@router.post("/account")
@account_producer(accounts)
async def create_account(info: CreateAccountPayload, tasks: BackgroundTasks):
    '''
    creates a new account
    '''
    return accounts.create_account(info.name)

@router.post("/account/{id}/deposit")
@account_producer(accounts)
async def deposit(deposit: DepositPayload):
    '''
    adds a deposit in a specific account
    '''
    accounts.deposit(deposit)

@router.post("account/{id}/withdrawal")
@account_producer(accounts)
async def withdrawal(withdrawal: WithdrawalPayload):
    '''
    does a withdrawal from a specific account
    '''
    accounts.withdrawal(withdrawal)