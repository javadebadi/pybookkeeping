"""A module to implement bookkeeper as a class.
"""
from pybookkeeping.data_models import (
    Account,
    ChartOfAccounts,
    Transaction,
    Journal,
)

class Bookkeeper:

    def __init__(
        self,
        chart_of_accounts: ChartOfAccounts,
        ) -> None:
        self.chart_of_accounts = chart_of_accounts