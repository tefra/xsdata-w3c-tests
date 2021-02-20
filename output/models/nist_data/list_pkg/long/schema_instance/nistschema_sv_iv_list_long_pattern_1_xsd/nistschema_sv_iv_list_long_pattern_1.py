from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-long-pattern-1-NS"


@dataclass
class NistschemaSvIvListLongPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-long-pattern-1"
        namespace = "NISTSchema-SV-IV-list-long-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\-\d{18} \-\d{11} \-\d{7} \-\d{3} \d{1} \d{5} \d{9} \d{18}",
            "tokens": True,
        }
    )
