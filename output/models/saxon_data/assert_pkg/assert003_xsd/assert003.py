from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Temp:
    class Meta:
        name = "temp"

    a: Optional["Temp.A"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    x: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    y: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class A:
        b: Optional[object] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
