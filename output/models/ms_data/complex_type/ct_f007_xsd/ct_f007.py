from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ForwardRef


@dataclass(kw_only=True)
class MyType:
    class Meta:
        name = "myType"

    my_element_or_my_element2: None | MyType.MyElement | MyType.MyElement2 = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "myElement",
                        "type": ForwardRef("MyType.MyElement"),
                        "namespace": "",
                    },
                    {
                        "name": "myElement2",
                        "type": ForwardRef("MyType.MyElement2"),
                        "namespace": "",
                    },
                ),
            },
        )
    )
    my_attr: None | object = field(
        default=None,
        metadata={
            "name": "myAttr",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class MyElement:
        value: str = field(default="")

    @dataclass(kw_only=True)
    class MyElement2:
        value: str = field(default="")


@dataclass(kw_only=True)
class FooType(MyType):
    class Meta:
        name = "fooType"

    my_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
