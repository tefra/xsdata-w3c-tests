from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-short-pattern-4-NS"


@dataclass
class NistschemaSvIvListShortPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-short-pattern-4"
        namespace = "NISTSchema-SV-IV-list-short-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\-\d{5} \-\d{4} \-\d{3} \-\d{2} \-\d{1} \d{1} \d{2} \d{3} \d{4} \d{5}",
            "tokens": True,
        }
    )
