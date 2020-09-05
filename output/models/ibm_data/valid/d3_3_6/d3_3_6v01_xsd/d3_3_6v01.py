from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_D3_3_6_v01"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_D3_3_6_v01"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=0,
            max_inclusive=5
        )
    )
