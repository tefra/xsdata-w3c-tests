from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class E1:
    class Meta:
        name = "e1"
        nillable = True

    e3: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e4: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    e5: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
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
