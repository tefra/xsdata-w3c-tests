from dataclasses import dataclass, field
from typing import Dict, Optional, Type, Union, Any


@dataclass
class MyType:
    class Meta:
        name = "myType"

    my_element1_or_my_element2_or_my_element3: Optional[
        Union["MyType.MyElement1", "MyType.MyElement2", "MyType.MyElement3"]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "myElement1",
                    "type": Type["MyType.MyElement1"],
                    "namespace": "",
                },
                {
                    "name": "myElement2",
                    "type": Type["MyType.MyElement2"],
                    "namespace": "",
                },
                {
                    "name": "myElement3",
                    "type": Type["MyType.MyElement3"],
                    "namespace": "",
                },
            ),
        },
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass
    class MyElement1:
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
    class MyElement3:
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

    my_element2_or_my_element3: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any_attributes: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    my_element1: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement1",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    my_attr1: Optional[object] = field(
        default=None,
        metadata={
            "name": "myAttr1",
            "type": "Attribute",
        },
    )
    my_attr2: Optional[object] = field(
        default=None,
        metadata={
            "name": "myAttr2",
            "type": "Attribute",
        },
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
