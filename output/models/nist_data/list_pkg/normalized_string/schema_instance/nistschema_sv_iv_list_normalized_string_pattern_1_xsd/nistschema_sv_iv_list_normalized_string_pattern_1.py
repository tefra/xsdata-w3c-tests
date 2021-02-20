from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-pattern-1-NS"


@dataclass
class NistschemaSvIvListNormalizedStringPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-pattern-1"
        namespace = "NISTSchema-SV-IV-list-normalizedString-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_13058 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14172 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_13454 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_10133-1061 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_10981 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16632 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_19839",
            "tokens": True,
        }
    )
