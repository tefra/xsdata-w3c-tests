from dataclasses import dataclass, field
from decimal import Decimal
from typing import List

__NAMESPACE__ = "foo"


@dataclass
class Root:
    """
    :ivar key:
    :ivar ref:
    """
    class Meta:
        name = "root"
        namespace = "foo"

    key: List[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ref: List[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
