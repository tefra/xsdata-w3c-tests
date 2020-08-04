from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-pattern-1-NS"


@dataclass
class NistschemaSvIvListGDayPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-pattern-1"
        namespace = "NISTSchema-SV-IV-list-gDay-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"---\d7 ---2\d ---\d9 ---\d8 ---\d8 ---\d8 ---\d2 ---0\d",
            tokens=True
        )
    )
