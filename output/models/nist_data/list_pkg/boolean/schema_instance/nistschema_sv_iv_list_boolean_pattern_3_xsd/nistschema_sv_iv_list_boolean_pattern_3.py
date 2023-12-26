from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-pattern-3-NS"


@dataclass
class NistschemaSvIvListBooleanPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-pattern-3"
        namespace = "NISTSchema-SV-IV-list-boolean-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[1]{1} false [1]{1} true [1]{1}",
            "tokens": True,
        },
    )
