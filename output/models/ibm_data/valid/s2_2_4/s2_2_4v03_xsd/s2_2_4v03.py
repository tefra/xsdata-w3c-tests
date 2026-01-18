from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass(kw_only=True)
class T1:
    class Meta:
        name = "t1"

    a1: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    a2: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class T0:
    class Meta:
        name = "t0"

    e1: list[T1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
    e2: list[T1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class RootType:
    class Meta:
        name = "rootType"

    hi1: T0 = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    hi2: T0 = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "a"
