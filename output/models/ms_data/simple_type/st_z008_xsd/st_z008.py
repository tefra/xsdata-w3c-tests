from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class T1:
    class Meta:
        name = "t1"

    value: None | object = field(default=None)


@dataclass(kw_only=True)
class T2(T1):
    class Meta:
        name = "t2"

    att: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    e1: list[T1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
    e2: list[T2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
