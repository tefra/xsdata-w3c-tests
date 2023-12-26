from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-c"


@dataclass
class CtA:
    class Meta:
        name = "ct-A"

    a1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    a2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class E1(CtA):
    class Meta:
        name = "e1"
        namespace = "ns-c"
