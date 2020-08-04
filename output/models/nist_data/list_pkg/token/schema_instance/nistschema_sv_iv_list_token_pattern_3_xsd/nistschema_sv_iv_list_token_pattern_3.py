from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-token-pattern-3-NS"


@dataclass
class NistschemaSvIvListTokenPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-token-pattern-3"
        namespace = "NISTSchema-SV-IV-list-token-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_11426-1564 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_12210 \d{1,5}_([A-Z][a-z]{1,20}_){4}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_10273 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_15228-1341 \d{1,5}_([A-Z][a-z]{1,20}_){5}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_19382 \d{1,5}_([A-Z][a-z]{1,20}_){2}Street_([A-Z][a-z]{1,20}_){3},_[A-Z]{2}_15012-1071 \d{1,5}_([A-Z][a-z]{1,20}_){1}Street_([A-Z][a-z]{1,20}_){2},_[A-Z]{2}_16723",
            tokens=True
        )
    )
