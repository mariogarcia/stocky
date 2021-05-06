from pydantic import BaseModel

class CreateAccountPayload(BaseModel):
    name: str

class DepositPayload(BaseModel):
    amount: float

class WithdrawalPayload(BaseModel):
    amount: float