from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooTest:
    class Meta:
        name = "fooTest"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[A-C]{0,2}",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    foo_test: FooTest = field(
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
        }
    )
