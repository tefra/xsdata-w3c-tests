from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-token-pattern-1-NS"


@dataclass
class NistschemaSvIvListTokenPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-token-pattern-1"
        namespace = "NISTSchema-SV-IV-list-token-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15685 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13673 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_10126 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_12533 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13175",
            "tokens": True,
        }
    )
