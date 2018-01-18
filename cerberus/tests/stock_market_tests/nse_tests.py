import unittest
from datetime import date
from datetime import timedelta
from cerberus.data.nse.nse_suite import NSESuite

class NSETests(unittest.TestCase):

    def test_it_can_import_nifty_50_index_from_latest_year(self):
        current_date = date.today() 
        year_ago = current_date - timedelta(weeks=52)
        nse = NSESuite(start=year_ago, end=current_date)
        nse.imp(symbol="NIFTY NEXT 50", index=True) 

        assert len(Index.all()) == 365
        assert any(rel.name == "next" for rel in Index.first(name="NIFTY NEXT 50").relationships())
        assert any(rel.name == "prev" for rel in Index.last(name="NIFTY NEXT 50").relationships())
