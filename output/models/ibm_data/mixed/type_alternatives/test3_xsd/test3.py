from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class MinimalA:
    class Meta:
        name = "MINIMAL_A"

    b: int = field(
        metadata={
            "name": "B",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class X:
    a: MinimalA = field(
        metadata={
            "name": "A",
            "type": "Element",
            "namespace": "",
        }
    )
    a_attribute: None | bool = field(
        default=None,
        metadata={
            "name": "a",
            "type": "Attribute",
        },
    )
