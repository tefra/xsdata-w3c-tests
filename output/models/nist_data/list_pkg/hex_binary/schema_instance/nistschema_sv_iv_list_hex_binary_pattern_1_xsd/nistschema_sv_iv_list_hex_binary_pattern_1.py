from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-pattern-1-NS"


@dataclass
class NistschemaSvIvListHexBinaryPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-pattern-1"
        namespace = "NISTSchema-SV-IV-list-hexBinary-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"[0-9A-F]{22} [0-9A-F]{70} [0-9A-F]{66} [0-9A-F]{2} [0-9A-F]{30} [0-9A-F]{38}",
            "tokens": True,
        }
    )
