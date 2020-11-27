from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-negativeInteger-pattern-2-NS"


@dataclass
class NistschemaSvIvListNegativeIntegerPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-negativeInteger-pattern-2"
        namespace = "NISTSchema-SV-IV-list-negativeInteger-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"\-\d{1} \-\d{2} \-\d{3} \-\d{4} \-\d{5} \-\d{6} \-\d{7} \-\d{8} \-\d{9} \-\d{18}",
            "tokens": True,
        }
    )
