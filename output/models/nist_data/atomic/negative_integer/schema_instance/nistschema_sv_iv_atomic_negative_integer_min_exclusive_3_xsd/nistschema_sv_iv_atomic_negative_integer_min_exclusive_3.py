from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicNegativeIntegerMinExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": -900435039333670416,
        }
    )
