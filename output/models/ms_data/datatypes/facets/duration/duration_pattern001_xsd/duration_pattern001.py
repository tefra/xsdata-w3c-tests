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
            "required": True,
            "pattern": r"P\p{Nd}{1,4}Y\p{Nd}{1,2}MT\p{Nd}{1,2}H",
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
