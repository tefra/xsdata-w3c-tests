from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Temp:
    class Meta:
        name = "temp"

    a: Temp.A = field(
        metadata={
            "type": "Element",
        }
    )
    x: object = field(
        metadata={
            "type": "Attribute",
        }
    )
    y: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class A:
        b: None | object = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
