from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-negativeInteger-pattern-4-NS"


@dataclass
class NistschemaSvIvListNegativeIntegerPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-negativeInteger-pattern-4"
        namespace = "NISTSchema-SV-IV-list-negativeInteger-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\-\d{1} \-\d{4} \-\d{7} \-\d{10} \-\d{13} \-\d{18}",
            "tokens": True,
        }
    )
