from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-normalizedString-pattern-4-NS"


@dataclass
class NistschemaSvIvListNormalizedStringPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-normalizedString-pattern-4"
        namespace = "NISTSchema-SV-IV-list-normalizedString-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_17466-1733 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16877 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_16698-1324 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_18587 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_10792 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11619-1091",
            tokens=True
        )
    )
