from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-2-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=7.81196934271684e+16
        )
    )