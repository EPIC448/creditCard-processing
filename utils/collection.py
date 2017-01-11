from collections import OrderedDict


class CreditRecordsCollection:

    def __init__(self, accounts):
        self.data = OrderedDict()
        self._initialize_accounts(accounts=accounts)

    def _initialize_accounts(self, accounts):
        while accounts:
            account = accounts.popleft()
            self.add(account)
        self.data = OrderedDict(sorted(self.data.items(), key=lambda t: t[0]))

    def add(self, account):
        self.data[account.name] = dict(
            account_number=account.account_number,
            limit=account.limit,
            amount=account.amount,
            verified=account.verified,
        )

    def charge(self, transaction):
        if self.data[transaction.name]['amount'] + \
                transaction.amount < \
                self.data[transaction.name]['limit']:

            self.data[transaction.name]['amount'] += transaction.amount
        else:
            pass

    def credit(self, transaction):
        self.data[transaction.name]['amount'] -= transaction.amount

    def process(self, transactions):
        while transactions:
            transaction = transactions.popleft()

            if transaction.type == 'Charge':
                self.charge(transaction)

            elif transaction.type == 'Credit':
                self.credit(transaction)

            else:
                break

    def __str__(self):
        response = ""
        for key, value in self.data.items():
            if value['verified']:
                response += "{}: ${}\n".format(key, value['amount'])
            else:
                response += "{}: {}\n".format(key, 'error')
        return response
