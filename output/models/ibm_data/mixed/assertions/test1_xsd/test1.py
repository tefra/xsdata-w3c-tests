from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Xtype:
    class Meta:
        name = "XType"

    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    min: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class X(Xtype):
    pass
