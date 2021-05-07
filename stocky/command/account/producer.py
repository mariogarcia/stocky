from stocky.command.account.domain import Account

def create_account(account: Account):
    print("====================> create_account() ==> {}".format(account.full_name))

def update_account(account: Account):
    print("====================> update_account() ==> {}".format(account.full_name))