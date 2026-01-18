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
            "pattern": r"-\p{Nd}{1,3}",
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
