import unittest
from decimal import Decimal

from ap_pipeline.pipeline import run

FEED = "invoice_id,vendor,due_date,amount,paid\nINV-1,V-100,2026-09-01,120.00,false\nINV-3,V-100,bad,10.00,false\n"


class PipelineTest(unittest.TestCase):
    def test_run_maps_and_rejects(self):
        records, report = run(FEED)
        self.assertEqual(records[0]["amount"], Decimal("120.00"))
        self.assertEqual(report, {"rows": 2, "loaded": 1, "rejected": 1, "reject_reasons": ["ValueError"]})

    def test_paid_flag(self):
        records, _ = run("invoice_id,vendor,due_date,amount,paid\nI,V,2026-01-01,1,TRUE\n")
        self.assertTrue(records[0]["paid"])

    def test_missing_column_rejected(self):
        records, report = run("invoice_id,vendor,due_date\nI,V,2026-01-01\n")
        self.assertEqual(report["rejected"], 1)


if __name__ == "__main__":
    unittest.main()
