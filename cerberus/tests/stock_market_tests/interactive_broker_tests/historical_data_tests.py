import unittest
import datetime
import swigibpy
from threading import Thread
from cerberus.services.interactive_broker.ib_wrapper import IBWrapper
from cerberus.auxiliary.yaml_validator import YamlValidator as yv

class InteractiveBrokerHistoricalDataTests(unittest.TestCase):
    def setUp(self):
        self.connection = swigibpy.EPosixClientSocket(ewrapper=IBWrapper)

    def test_it_can_retrieve_account_summary(self):
        self.connection.eConnect(4001)
        
        assert response.status_code == 200

