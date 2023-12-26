from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ShoeType:
    class Meta:
        name = "shoeType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Shoesize(ShoeType):
    class Meta:
        name = "shoesize"
