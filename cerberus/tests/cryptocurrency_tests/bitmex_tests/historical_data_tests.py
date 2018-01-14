import unittest
from cerberus.services.bitmex.bitmex_wrapper import BitmexWrapper

class BitmexHistoricalDataTests(unittest.TestCase):
    def setUp(self):
        self.bitmex_wrapper = BitmexWrapper()

    def test_it_can_retrieve_order_history(self):
        response = self.bitmex_wrapper.get('order')

        assert response.status_code == 200

    def it_can_retrieve_eth_data(self):
        pass

    def it_can_retrieve_instruments(self):
       pass 

    
    def tearDown(self):
        pass

