import unittest
from cerberus.services.bitmex.bitmex_wrapper import BitmexWrapper

class BitmexHistoricalDataTests(unittest.TestCase):
    def setUp(self):
        self.bitmex_wrapper = BitmexWrapper()

    def test_it_can_retrieve_order_history(self):
        response = self.bitmex_wrapper.query(verb='GET', path='order')

        assert response.status_code == 200

    def test_it_can_retrieve_instruments(self):
        response = self.bitmex_wrapper.query(verb='GET', path='instrument')

        assert response.status_code == 200

    def test_it_can_retrieve_eth_data(self):
        response = self.bitmex_wrapper.query(verb='GET', path='position', params={'symbol': 'ETH'})

        assert response.status_code == 200
    
    def tearDown(self):
        pass

