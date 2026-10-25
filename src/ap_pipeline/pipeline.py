"""One run: ingest -> transform -> data-quality report."""
from .dq import quality_report
from .ingest import parse_feed
from .transform import to_model


def run(csv_text: str):
    records, rejected = to_model(parse_feed(csv_text))
    return records, quality_report(records, rejected)
