from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-pattern-1-NS"


@dataclass
class NistschemaSvIvListBooleanPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-pattern-1"
        namespace = "NISTSchema-SV-IV-list-boolean-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"true [0]{1} [0]{1} false [1]{1} false",
            tokens=True
        )
    )
