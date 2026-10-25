"""Transformation: map feed rows to the Invoice Data Model (id, vendor, due_date, amount, paid)."""
from datetime import date
from decimal import Decimal, InvalidOperation
from typing import Dict, List, Tuple


def to_model(rows: List[Dict[str, str]]) -> Tuple[List[Dict], List[Dict]]:
    """Return (records, rejected); a row is rejected when a required field is missing or invalid."""
    records, rejected = [], []
    for r in rows:
        try:
            records.append({"id": r["invoice_id"].strip(), "vendor": r["vendor"].strip(), "due_date": date.fromisoformat(r["due_date"]),
                            "amount": Decimal(r["amount"]), "paid": r.get("paid", "false").strip().lower() == "true"})
        except (KeyError, ValueError, InvalidOperation, AttributeError) as e:
            rejected.append({"row": r, "reason": type(e).__name__})
    return records, rejected
