from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicNegativeIntegerMaxExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-maxExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=-1.8493533915575357e+17
        )
    )