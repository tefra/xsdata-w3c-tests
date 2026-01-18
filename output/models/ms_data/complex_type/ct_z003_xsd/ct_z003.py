from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class C1:
    e1: list[C1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 10,
        },
    )


@dataclass(kw_only=True)
class Foo(C1):
    class Meta:
        name = "foo"
