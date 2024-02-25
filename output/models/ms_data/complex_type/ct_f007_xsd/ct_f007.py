from dataclasses import dataclass, field
from typing import Optional, Type, Union, Any


@dataclass
class MyType:
    class Meta:
        name = "myType"

    my_element_or_my_element2: Optional[
        Union["MyType.MyElement", "MyType.MyElement2"]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "myElement",
                    "type": Type["MyType.MyElement"],
                    "namespace": "",
                },
                {
                    "name": "myElement2",
                    "type": Type["MyType.MyElement2"],
                    "namespace": "",
                },
            ),
        },
    )
    my_attr: Optional[object] = field(
        default=None,
        metadata={
            "name": "myAttr",
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
    class MyElement2:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )


@dataclass
class FooType(MyType):
    class Meta:
        name = "fooType"

    my_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
