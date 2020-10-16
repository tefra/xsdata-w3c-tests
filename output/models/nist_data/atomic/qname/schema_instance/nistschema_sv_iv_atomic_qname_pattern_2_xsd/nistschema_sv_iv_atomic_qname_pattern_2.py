from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-QName-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicQnamePattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-QName-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-QName-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"([\i-[:]][\c-[:]]*:)?[\i-[:]][\c-[:]]{20}",
        }
    )
