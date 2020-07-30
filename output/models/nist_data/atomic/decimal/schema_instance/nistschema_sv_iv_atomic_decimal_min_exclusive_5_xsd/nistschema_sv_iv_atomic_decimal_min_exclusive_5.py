from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinExclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-5-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=999999999999999998
        )
    )
