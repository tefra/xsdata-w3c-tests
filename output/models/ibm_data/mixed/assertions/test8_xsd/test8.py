from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ShoeType:
    class Meta:
        name = "shoeType"

    value: int = field(
        metadata={
            "required": True,
        }
    )
    country: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Shoesize(ShoeType):
    class Meta:
        name = "shoesize"
