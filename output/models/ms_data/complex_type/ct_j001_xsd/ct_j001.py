from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class MyType:
    class Meta:
        name = "myType"

    my_element1: str = field(
        metadata={
            "name": "myElement1",
            "type": "Element",
            "namespace": "",
        }
    )
    my_element2: str = field(
        metadata={
            "name": "myElement2",
            "type": "Element",
            "namespace": "",
        }
    )
    my_element3: str = field(
        metadata={
            "name": "myElement3",
            "type": "Element",
            "namespace": "",
        }
    )
    my_attr: None | object = field(
        default=None,
        metadata={
            "name": "myAttr",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class FooType(MyType):
    class Meta:
        name = "fooType"

    my_element4: None | str = field(
        default=None,
        metadata={
            "name": "myElement4",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
