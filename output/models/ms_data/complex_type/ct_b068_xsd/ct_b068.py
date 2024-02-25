from dataclasses import dataclass, field
from typing import Optional, Type, Union


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    my_element_or_my_ele2: Optional[
        Union["FooType.MyElement", "FooType.MyEle2"]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "myElement",
                    "type": Type["FooType.MyElement"],
                    "namespace": "",
                },
                {
                    "name": "myEle2",
                    "type": Type["FooType.MyEle2"],
                    "namespace": "",
                },
            ),
        },
    )
    attr_test: Optional[object] = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        },
    )
    attr_test2: Optional[object] = field(
        default=None,
        metadata={
            "name": "attrTest2",
            "type": "Attribute",
        },
    )

    @dataclass
    class MyElement:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class MyEle2:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
