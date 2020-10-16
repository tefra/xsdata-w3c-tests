from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-pattern-2-NS"


@dataclass
class NistschemaSvIvUnionShortGYearPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-pattern-2"
        namespace = "NISTSchema-SV-IV-union-short-gYear-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\-\d{3}",
        }
    )
