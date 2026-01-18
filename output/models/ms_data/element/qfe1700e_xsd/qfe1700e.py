from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class E1:
    class Meta:
        name = "e1"
        nillable = True

    value: None | int = field(
        metadata={
            "nillable": True,
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    e1: None | E1 = field(
        metadata={
            "type": "Element",
            "nillable": True,
        }
    )
