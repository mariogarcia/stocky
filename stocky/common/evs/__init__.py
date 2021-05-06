from eventsourcing.system import System, SingleThreadedRunner
from stocky.common.evs.application import AccountApplication, AccountApplicationProducer

# init
system = System(pipes=[[AccountApplication, AccountApplicationProducer]])
runner = SingleThreadedRunner(system)
runner.start()

accounts = runner.get(AccountApplication)
producer = AccountApplicationProducer()

accounts.lead(producer)
producer.follow(accounts.__class__.__name__, accounts.log)