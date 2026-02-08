from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooTest:
    class Meta:
        name = "fooTest"

    value: str = field(default="")


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    foo_test: list[FooTest] = field(
        default_factory=list,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
