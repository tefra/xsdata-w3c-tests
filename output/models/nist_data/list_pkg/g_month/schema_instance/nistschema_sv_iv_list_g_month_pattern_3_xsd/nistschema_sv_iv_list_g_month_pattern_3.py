from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-pattern-3-NS"


@dataclass
class NistschemaSvIvListGMonthPattern3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-pattern-3"
        namespace = "NISTSchema-SV-IV-list-gMonth-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"--1\d --0\d --1\d --0\d --0\d --0\d --\d8",
            "tokens": True,
        }
    )
