"""Module for data models used to model entities of bookkeeping.
"""
from datetime import datetime as dt
import pytz


class Account:

    def __init__(
        self,
        title: str,
        account_number: int,
        ) -> None:
        self.title = title
        self.account_number = account_number

    def __hash__(self):
        return hash((self.title, self.account_number))

    def __lt__(self, other):
        assert isinstance(other, type(self))
        if self.account_number < other.account_number:
            return True
        else:
            return False

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            raise NotImplementedError()
        if (
            self.title == other.title
            and
            self.account_number == other.account_number
            ):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"{str(self.account_number).rjust(20)}| {str(self.title).ljust(80)}"



class ChartOfAccounts(set):

    def __init__(self, accounts_list):
        super().__init__()
        if accounts_list:
            for account in accounts_list:
                self.add_account(account)

    def add_account(self, account: Account) -> None:
        assert isinstance(account, Account)
        self.add(account)

    def sort(self):
        return sorted(self)

    def __str__(self) -> str:
        s = "="*25 + " Chart Of Accounts " + "="*25 + "\n"
        s += "|" + "Account Number".upper().rjust(20) + "|" + "Title".upper().ljust(80) + "\n"
        for account in self.sort():
            s += "|" + "-"*20 + "|" + "-"*80 + "\n"
            s += "|" + account.__str__() + "\n"
        s += "|" + "-"*20 + "|" + "-"*80 + "\n"
        return s


class Transaction:

    def __init__(
        self,
        title: str,
        utc_datetime: dt,
        ) -> None:
        self.title = title
        self.utc_datetime = utc_datetime

    @property
    def utc_datetime(self) -> dt:
        return self._utc_datetime

    @utc_datetime.setter
    def utc_datetime(self, utc_datetime: dt) -> None:
        try:
            assert (
                utc_datetime.tzinfo is None
                or
                utc_datetime.tzinfo == pytz.utc
                )
        except AssertionError:
            raise AssertionError(
                "the utc_datetime parameter must be either naive datetime "
                "or have UTC timezone but it got a timezone of "
                f"'{utc_datetime.tzinfo}'"
            )
        self._utc_datetime = utc_datetime.replace(tzinfo=pytz.utc)



    def __str__(self) -> str:
        s = "======== Transaction ===========\n"
        s += self.title + "\n"
        return s

    def __repr__(self) -> str:
        s = "Transaction(\n"
        s += f"\ttitle='{self.title}',\n"
        s += "\tutcdatetime="
        s += repr(self.utc_datetime).replace(', tzinfo=<UTC>)','),') + "\n"
        s += ")"
        return s