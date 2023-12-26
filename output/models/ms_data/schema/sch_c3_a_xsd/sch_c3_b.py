from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CtB:
    class Meta:
        name = "ct-B"

    b1: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    b2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class E2(CtB):
    class Meta:
        name = "e2"
