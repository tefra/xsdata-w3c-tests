from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-3-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=-67428259604688900
        )
    )
