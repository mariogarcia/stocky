from eventsourcing.system import System, SingleThreadedRunner
from stocky.common.evs.application import AccountApplication, Counters

# init
system = System(pipes=[[AccountApplication, Counters]])
runner = SingleThreadedRunner(system)
runner.start()

accounts = runner.get(AccountApplication)