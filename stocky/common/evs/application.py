from abc import ABC
from uuid import UUID

from eventsourcing.application import Application
from eventsourcing.dispatch import singledispatchmethod
from eventsourcing.system import Follower, Leader, Promptable, ProcessApplication

from stocky.common.evs.domain import Account

class AccountApplication(Leader, Application, ABC):
    def create_account(self, name: str):
        '''
        creates a new account with the name of the holder
        '''
        account = Account.create(name)
        self.save(account)
        return account.id

    def deposit(self, id: str, amount: float):
        '''
        deposits some amount of money in the system
        '''
        account = self.repository.get(UUID(id))
        account.deposit(amount)
        self.save(account)

    def withdrawal(self, id: str, amount: float):
        '''
        withdraws some amount of money from the system
        '''
        account = self.repository.get(UUID(id))
        account.withdrawal(amount)
        self.save(account)

    def info(self, id: str):        
        '''
        returns the current account status
        '''
        return self.repository.get(id)


class AccountApplicationProducer(ProcessApplication, Promptable):
    @singledispatchmethod
    def policy(self, domain_event, process_event):
        """Default policy"""
        print("could be used as a producer")

    def receive_prompt(self, name: str):
        print("used for simple metrics, not so useful")
