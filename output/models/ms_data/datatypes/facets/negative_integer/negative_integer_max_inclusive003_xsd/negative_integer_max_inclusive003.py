from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_inclusive": -1,
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
