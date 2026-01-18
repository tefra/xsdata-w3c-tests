from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Xtype:
    class Meta:
        name = "XType"

    message: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    min: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    max: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class X(Xtype):
    pass
