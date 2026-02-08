from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: bytes = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "max_length": 5,
            "format": "base16",
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
