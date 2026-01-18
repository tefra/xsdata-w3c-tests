from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    my_element_or_my_ele2: None | FooType.MyElement | FooType.MyEle2 = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "myElement",
                    "type": ForwardRef("FooType.MyElement"),
                    "namespace": "",
                },
                {
                    "name": "myEle2",
                    "type": ForwardRef("FooType.MyEle2"),
                    "namespace": "",
                },
            ),
        },
    )
    attr_test: None | object = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        },
    )
    attr_test2: None | object = field(
        default=None,
        metadata={
            "name": "attrTest2",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class MyElement:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )

    @dataclass(kw_only=True)
    class MyEle2:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
