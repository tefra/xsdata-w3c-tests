from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class MyType:
    class Meta:
        name = "myType"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
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
class FooType(MyType):
    class Meta:
        name = "fooType"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    my_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
