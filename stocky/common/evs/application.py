from uuid import UUID
from eventsourcing.application import Application
from stocky.common.evs.domain import Account

class AccountApplication(Application):
    def create_account(self, name: str):
        account = Account.create(name)
        self.save(account)
        return account.id

    def deposit(self, id: str, deposit: float):
        account = self.repository.get(UUID(id))
        account.deposit(deposit)
        self.save(account)

    def withdrawal(self, withdrawal: float):
        account = self.repository.get(id)
        account.withdrawal(withdrawal)
        self.save(account)

    def info(self, id: str):        
        return self.repository.get(id)

    def notify(self, events):
        for event in events:
            print("producing totally!!!!", event)
        
from eventsourcing.application import AggregateNotFound
from eventsourcing.system import ProcessApplication
from eventsourcing.dispatch import singledispatchmethod


class Counters(ProcessApplication):

    def policy(self, domain_event, process_event):
        pass

    @singledispatchmethod
    def policy(self, domain_event, process_event):
        """Default policy"""

    # @policy.register(Account.create)
    def _(self, domain_event, process_event):
        what = domain_event.what
        counter_id = Counter.create_id(what)
        try:
            counter = self.repository.get(counter_id)
        except AggregateNotFound:
            counter = Counter.create(what)
        counter.increment()
        process_event.save(counter)

    def get_count(self, what):
        counter_id = Counter.create_id(what)
        try:
            counter = self.repository.get(counter_id)
        except AggregateNotFound:
            return 0
        return counter.count