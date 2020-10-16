from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-a"


@dataclass
class CtB:
    """
    :ivar b1:
    :ivar b2:
    """
    class Meta:
        name = "ct-B"

    b1: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        }
    )
    b2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "ns-a",
            "required": True,
        }
    )


@dataclass
class E2(CtB):
    class Meta:
        name = "e2"
        namespace = "ns-a"
