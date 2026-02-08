from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class MyType:
    class Meta:
        name = "myType"

    my_ele1: str = field(
        metadata={
            "name": "myEle1",
            "type": "Element",
            "namespace": "",
        }
    )
    my_ele2: str = field(
        metadata={
            "name": "myEle2",
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class FooType(MyType):
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
