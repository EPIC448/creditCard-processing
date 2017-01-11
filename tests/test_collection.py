import unittest
from collections import deque

from utils.collection import CreditRecordsCollection
from utils.data import Accounts


accounts = deque([
    Accounts(
        name='Sam',
        account_number='123456789',
        limit='$3000',
        amount=0,
        verified='True'),
    Accounts(
        name='Teresa',
        account_number='393723943',
        limit='$3000',
        amount=0,
        verified='True'),
    Accounts(
        name='Mike',
        account_number='123456789',
        limit='$3000',
        amount=0,
        verified='True'),
    Accounts(
        name='Lauren',
        account_number='123456789',
        limit='$3000',
        amount=0,
        verified='True'),
    Accounts(
        name='Jack',
        account_number='123456789',
        limit='$3000',
        amount=0,
        verified='True'),
])


class CollectionTest(unittest.TestCase):
    def test_initialize_collection(self):
        collection = CreditRecordsCollection(accounts=accounts)
        self.assertEqual(collection.data['Sam']['amount'], 0)
