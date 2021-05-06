from fastapi import APIRouter, BackgroundTasks

from stocky.account.evs import accounts
from stocky.account.evs.application import AccountApplication
from stocky.account.command.producer import account_producer
from stocky.account.command.payloads import (CreateAccountPayload, DepositPayload, WithdrawalPayload)

router = APIRouter()

@router.post("/account")
@account_producer(accounts)
async def create_account(info: CreateAccountPayload, tasks: BackgroundTasks):
    return accounts.create_account(info.name)

@router.post("/account/{id}/deposit")
@account_producer(accounts)
async def deposit(deposit: DepositPayload):
    accounts.deposit(deposit)

@router.post("account/{id}/withdrawal")
@account_producer(accounts)
async def withdrawal(withdrawal: WithdrawalPayload):
    accounts.withdrawal(withdrawal)