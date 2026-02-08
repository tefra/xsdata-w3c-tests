from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class B:
    e: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 5,
        },
    )
    f: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 5,
        },
    )
    type_value: str = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
        }
    )


@dataclass(kw_only=True)
class R(B):
    pass


@dataclass(kw_only=True)
class Root(B):
    class Meta:
        name = "root"
