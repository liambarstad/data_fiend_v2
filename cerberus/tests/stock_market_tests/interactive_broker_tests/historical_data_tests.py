import unittest
import datetime
from threading import Thread
from cerberus.services.interactive_broker.ib_wrapper import IBWrapper
from cerberus.services.interactive_broker.ib_client import IBClient

class InteractiveBrokerHistoricalDataTests(unittest.TestCase):
    def setUp(self):
        self.ib_wrapper = IBWrapper()
        self.ib_client = IBClient()
        self.client_thread = Thread(target = self.ib_client.run_interface)

    def test_it_can_retrieve_order_history(self):
        self.client_thread.start()
        start_date = datetime.datetime(year=2017,
                month=2,
                day=2,
                hour=16,
                minute=43)
        end_date = datetime.datetime(year=2017,
                month=9,
                day=2,
                hour=2,
                minute=22)
        response = self.ib_wrapper.get_hist(start=start_date, end=end_date, instrument="AAPL")
        assert response.status_code == 200

