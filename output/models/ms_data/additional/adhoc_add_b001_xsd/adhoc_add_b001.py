from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

__NAMESPACE__ = "ns-a"


@dataclass(kw_only=True)
class NsAAft:
    class Meta:
        name = "ns-a-aft"

    x: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
    y: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Aft(NsAAft):
    class Meta:
        name = "aft"
        namespace = "ns-a"


@dataclass(kw_only=True)
class MyType(NsAAft):
    class Meta:
        name = "myType"

    y: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Abc(MyType):
    class Meta:
        name = "abc"
        namespace = "ns-a"


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    a_or_abc: None | str | Abc = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "abc",
                    "type": Abc,
                    "namespace": "ns-a",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Root(Foo):
    class Meta:
        name = "root"
        namespace = "ns-a"
