from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: float = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": 1.1,
            "max_exclusive": 7.7,
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
