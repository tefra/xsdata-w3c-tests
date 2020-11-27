from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-pattern-2-NS"


@dataclass
class NistschemaSvIvListNormalizedStringPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-pattern-2"
        namespace = "NISTSchema-SV-IV-list-normalizedString-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_15950 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_15905 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_15311 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_12031 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_10376",
            "tokens": True,
        }
    )
