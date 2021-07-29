from dataclasses import dataclass, field
from typing import Optional


@dataclass
class E1:
    class Meta:
        name = "e1"
        nillable = True

    e3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    e4: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    e5: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    e1: Optional[E1] = field(
        default=None,
        metadata={
            "type": "Element",
            "nillable": True,
        }
    )
