from uuid import uuid4
from eventsourcing.domain import Aggregate, AggregateCreated, AggregateEvent

class Account(Aggregate):
    def __init__(self, full_name: str):
        self.full_name: str = full_name
        self.balance: float = 0

    class Created(AggregateCreated):
        full_name: str

    class Deposit(AggregateEvent):
        deposit: float = 0

        def apply(self, aggregate: "Account") -> None:
            aggregate.balance += self.deposit

    class Withdrawal(AggregateEvent):
        withdrawal: float = 0

        def apply(self, aggregate: "Account") -> None:
            aggregate.balance -= self.withdrawal

    @classmethod
    def create(cls, full_name: str):
        return cls._create(cls.Created, id=uuid4(), full_name=full_name)

    def deposit(self, deposit: float):
        self.trigger_event(self.Deposit, deposit=deposit)

    def withdrawal(self, withdrawal: float):
        self.trigger_event(self.Withdrawal, withdrawal=withdrawal)