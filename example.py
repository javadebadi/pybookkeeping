from pybookkeeping.data_models import Account, ChartOfAccounts, Journal, Transaction

from datetime import datetime

account_cash = Account(
    title="Cash",
    account_number=101,
)
notes_receivable = Account(
    title="Notes Receivable",
    account_number=103,
)
accounts_receivable = Account(
    title="Accounts Receivable",
    account_number=105,
)
inventory = Account(
    title="Inventory",
    account_number=107,
)
supplies = Account(
    title="Supplies",
    account_number=108,
)
land = Account(
    title="Land",
    account_number=151,
)
building = Account(
    title="Building",
    account_number=152,
)
vehicles = Account(
    title="vehicle",
    account_number=153,
)
office_furniture = Account(
    title="Office furniture or equipment",
    account_number=154,
)
accounts_payable = Account(
    title="Accounts Payable",
    account_number=202,
)
capital_stock = Account(
    title="Capital Stock",
    account_number=301,
)

chart_of_accounts = ChartOfAccounts(
    [
        account_cash,
        notes_receivable,
        accounts_receivable,
        inventory,
        supplies,
        land,
        building,
        office_furniture,
        capital_stock,
        ]
    )

print(chart_of_accounts)

t1 = Transaction(
    title="Issued 200 shares of capital stock at $10 per share",
    utc_datetime=datetime(2019, 1, 15),
)
t2 = Transaction(
    title="Purchased a used truck",
    utc_datetime=datetime(2019, 1, 20),
)
t3 = Transaction(
    title="Purchased a lawnmower on account",
    utc_datetime=datetime(2019, 1, 20),
)
t4 = Transaction(
    title="Purchased supplies for cash",
    utc_datetime=datetime(2019, 1, 20),
)

t1.add_journal_entries(
    [
        (None, account_cash, 2000, 0),
        (None, capital_stock, 0, 2000),
        ]
)
t2.add_journal_entries(
    [
        ('Truck', vehicles, 800, 0),
        (None, account_cash, 0, 800),
        ]
)
t3.add_journal_entries(
    [
        ('Equipment', office_furniture, 250, 0),
        (None, accounts_payable, 0, 250),
        ]
)
t4.add_journal_entries(
    [
        (None, supplies, 180, 0),
        (None, account_cash, 0, 180),
        ]
)

j = Journal()
j.add_transaction(t1)
j.add_transaction(t2)
j.add_transaction(t3)
j.add_transaction(t4)


print(j)