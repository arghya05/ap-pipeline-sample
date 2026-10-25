"""Ingestion: parse the vendor invoice feed (CSV with header)."""
import csv
import io
from typing import Dict, List


def parse_feed(csv_text: str) -> List[Dict[str, str]]:
    return [dict(r) for r in csv.DictReader(io.StringIO(csv_text))]
