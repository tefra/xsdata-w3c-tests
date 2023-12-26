from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-pattern-3-NS"


@dataclass
class NistschemaSvIvListNormalizedStringPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-pattern-3"
        namespace = "NISTSchema-SV-IV-list-normalizedString-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_12432 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_10161 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11432-1137 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14004 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_19543-1772 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_16553-1944",
            "tokens": True,
        },
    )
