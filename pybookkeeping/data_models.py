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
        self._analyzed = False
        self.journal_entries = []

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

    @property
    def analyzed(self) -> bool:
        return self._analyzed

    def validate_journal_entries(
        self,
        journal_entries,
        ):
        debit_sum = 0
        credit_sum = 0
        assert type(journal_entries) == list
        assert len(journal_entries) > 0
        for details, account, debit, credit in journal_entries:
            assert isinstance(account, Account)
            debit_sum += debit
            credit_sum += credit
        if debit_sum != credit_sum:
            raise ValueError(
                "debit adn credit does not match for the journal entry"
            )

    def add_journal_entries(
        self,
        journal_entries,
        ):
        self.validate_journal_entries(journal_entries)
        self.journal_entries = journal_entries
        self._analyzed = True

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            raise NotImplementedError(
                "not same types are not implemented"
                )
        if self.utc_datetime < other.utc_datetime:
            return True
        else:
            return False

    def __str__(self) -> str:
        s = "======== Transaction ===========\n"
        s += self.title + "\n"
        if self._analyzed:
            for details, account, debit, credit in self.journal_entries:
                if details is None:
                    s += str(account).strip().ljust(50) + "|" + str(debit).ljust(12) + "|"  + str(credit).ljust(12) + "\n" 
                else:
                    s += (str(account.account_number).ljust(10).strip() + "| " + str(details).strip() ).ljust(50) + "|" + str(debit).ljust(12) + "|"  + str(credit).ljust(12) + "\n" 
        return s

    def __repr__(self) -> str:
        s = "Transaction(\n"
        s += f"\ttitle='{self.title}',\n"
        s += "\tutcdatetime="
        s += repr(self.utc_datetime).replace(', tzinfo=<UTC>)','),') + "\n"
        s += ")"
        return s


class Journal:

    def __init__(self) -> None:
        self._transactions = []
        self._start_date = None
        self._last_date = None

    @property
    def transactions(self):
        return self._transactions

    @property
    def start_date(self):
        return self._start_date

    @property
    def last_date(self):
        return self._last_date

    def add_transaction(self, transaction: Transaction):
        assert isinstance(transaction, Transaction)
        assert transaction.analyzed is True
        self._transactions.append(transaction)
        if not self._start_date:
            self._start_date = transaction.utc_datetime
        else:
            self._start_date = min(
                self.start_date,
                transaction.utc_datetime,
            )
        if not self._last_date:
            self._last_date = transaction.utc_datetime
        else:
            self._last_date = max(
                self.last_date,
                transaction.utc_datetime,
            )
        self._transactions = sorted(self._transactions)

    def __str__(self) -> str:
        s = "="*25 + " Genral Journal " + "="*25 + "\n"
        for transaction in self.transactions:
            s += str(transaction) + "\n"
        return s
