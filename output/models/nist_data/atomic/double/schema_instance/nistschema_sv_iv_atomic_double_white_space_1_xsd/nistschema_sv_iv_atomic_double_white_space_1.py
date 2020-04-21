from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-double-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicDoubleWhiteSpace1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-double-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-double-whiteSpace-1-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            white_space="collapse"
        )
    )
