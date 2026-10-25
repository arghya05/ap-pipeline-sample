"""Data-quality report for one pipeline run."""


def quality_report(records, rejected) -> dict:
    total = len(records) + len(rejected)
    return {"rows": total, "loaded": len(records), "rejected": len(rejected), "reject_reasons": sorted({r["reason"] for r in rejected})}
