from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-pattern-4-NS"


@dataclass
class NistschemaSvIvListBooleanPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-pattern-4"
        namespace = "NISTSchema-SV-IV-list-boolean-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"[1]{1} false [0]{1} true true [0]{1}",
            "tokens": True,
        }
    )
