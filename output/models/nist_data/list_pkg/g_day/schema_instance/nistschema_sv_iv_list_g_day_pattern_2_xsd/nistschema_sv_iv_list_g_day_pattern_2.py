from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-pattern-2-NS"


@dataclass
class NistschemaSvIvListGDayPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-pattern-2"
        namespace = "NISTSchema-SV-IV-list-gDay-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"---1\d ---\d4 ---1\d ---\d2 ---\d8 ---\d9 ---1\d ---\d1 ---\d4",
            "tokens": True,
        }
    )
