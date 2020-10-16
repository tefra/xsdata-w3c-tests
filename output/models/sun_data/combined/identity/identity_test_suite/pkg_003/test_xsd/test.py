from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

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

    key: List["Root.Key"] = field(
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

    @dataclass
    class Key:
        """
        :ivar id:
        """
        id: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )
