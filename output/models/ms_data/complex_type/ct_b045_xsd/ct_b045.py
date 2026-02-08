from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    my_element: str = field(
        metadata={
            "name": "myElement",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
