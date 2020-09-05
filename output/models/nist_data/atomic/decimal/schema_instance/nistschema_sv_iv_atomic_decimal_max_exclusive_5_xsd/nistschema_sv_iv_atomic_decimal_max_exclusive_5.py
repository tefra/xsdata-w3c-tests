from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxExclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-5-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=999999999999999999
        )
    )
