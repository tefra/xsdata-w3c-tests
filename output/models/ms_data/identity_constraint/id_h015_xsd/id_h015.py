from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Kid:
    class Meta:
        name = "kid"

    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Uid:
    class Meta:
        name = "uid"

    val: str = field(
        default="test",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    uid: list[Uid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    kid: list[Kid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
