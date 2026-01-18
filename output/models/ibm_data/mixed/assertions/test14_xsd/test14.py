from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class XType:
    class Meta:
        name = "X_Type"

    value: int = field(
        metadata={
            "required": True,
        }
    )
    a: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Example:
    x: list[XType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
