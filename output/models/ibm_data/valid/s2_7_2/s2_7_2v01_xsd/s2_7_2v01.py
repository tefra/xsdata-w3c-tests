from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class B:
    class Meta:
        name = "b"
        nillable = True
        namespace = "a"

    value: None | int = field(
        metadata={
            "nillable": True,
        }
    )


@dataclass(kw_only=True)
class T:
    class Meta:
        name = "t"

    b: None | B = field(
        metadata={
            "type": "Element",
            "namespace": "a",
            "nillable": True,
        }
    )


@dataclass(kw_only=True)
class Root(T):
    class Meta:
        name = "root"
        namespace = "a"
