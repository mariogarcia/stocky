from pydantic import BaseModel

class CreateAccountPayload(BaseModel):
    name: str

class DepositPayload(BaseModel):
    deposit: float

class WithdrawalPayload(BaseModel):
    withdrawal: float