from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-int-pattern-1-NS"


@dataclass
class NistschemaSvIvListIntPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-int-pattern-1"
        namespace = "NISTSchema-SV-IV-list-int-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\-\d{10} \-\d{4} \-\d{2} \d{1} \d{3} \d{10}",
            "tokens": True,
        }
    )
