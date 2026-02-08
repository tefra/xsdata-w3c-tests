from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    my_ele3: str = field(
        metadata={
            "name": "myEle3",
            "type": "Element",
            "namespace": "",
        }
    )
    my_ele4: int = field(
        metadata={
            "name": "myEle4",
            "type": "Element",
            "namespace": "",
        }
    )
    foo_type: None | str = field(
        default=None,
        metadata={
            "name": "fooType",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
