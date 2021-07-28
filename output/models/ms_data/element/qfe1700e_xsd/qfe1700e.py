from dataclasses import dataclass, field
from typing import Optional


@dataclass
class E1:
    class Meta:
        name = "e1"
        nillable = True

    value: Optional[int] = field(
        default=None,
        metadata={
            "nillable": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    e1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        }
    )
