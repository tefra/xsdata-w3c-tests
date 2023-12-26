from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-pattern-5-NS"


@dataclass
class NistschemaSvIvListNormalizedStringPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-pattern-5"
        namespace = "NISTSchema-SV-IV-list-normalizedString-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_14600 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15165-1290 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_17813-1396 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18970 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_13025 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15706-1707 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_16336",
            "tokens": True,
        },
    )
