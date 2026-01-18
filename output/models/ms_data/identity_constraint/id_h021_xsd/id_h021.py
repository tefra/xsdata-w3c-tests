from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "myNS.tempuri.org"


@dataclass(kw_only=True)
class Kid:
    class Meta:
        name = "kid"
        namespace = "myNS.tempuri.org"

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
        namespace = "myNS.tempuri.org"

    val: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "myNS.tempuri.org"

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
