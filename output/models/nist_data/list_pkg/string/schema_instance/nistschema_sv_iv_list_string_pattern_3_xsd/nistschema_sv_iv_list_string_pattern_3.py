from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-string-pattern-3-NS"


@dataclass
class NistschemaSvIvListStringPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-string-pattern-3"
        namespace = "NISTSchema-SV-IV-list-string-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_11654-1789 \d{1,5}_([A-Z][a-z]{1,20}_){3}Street_([A-Z][a-z]{1,20}_){1},_[A-Z]{2}_19111-1980 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_15774-1852 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_18248-1891 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15314",
            tokens=True
        )
    )
