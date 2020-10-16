from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-NMTOKEN-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicNmtokenPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-NMTOKEN-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-NMTOKEN-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\c{33}",
        }
    )
