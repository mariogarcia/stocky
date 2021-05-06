from uuid import uuid4
from eventsourcing.domain import Aggregate, AggregateCreated, AggregateEvent

class Account(Aggregate):
    def __init__(self):        
        self.name: str = ""
        self.balance: float = 0

    class Created(AggregateCreated):
        pass

    class Deposit(AggregateEvent):
        def apply(self, account):
            account.balance += 10000

    class Withdrawal(AggregateEvent):
        def __init__(self):
            self.withdrawal: float

        def apply(self, account):
            account.balance -= self.withdrawal

    @classmethod
    def create(cls, name: str):
        return cls._create(cls.Created, id=uuid4())

    def deposit(self, deposit: float):
        self.trigger_event(self.Deposit)

    def withdrawal(self, withdrawal: float):
        self.trigger_event(self.Withdrawal, withdrawal=withdrawal)