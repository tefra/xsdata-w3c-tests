from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "pattern": r"[0-9]{4}",
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
