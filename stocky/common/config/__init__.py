import os

def setup_event_sourcing():
    os.environ['CREATE_TABLE'] = 'true'
    os.environ['INFRASTRUCTURE_FACTORY'] = 'eventsourcing.sqlite:Factory'
    os.environ['SQLITE_DBNAME'] = 'file:/tmp/stocky.db'
  