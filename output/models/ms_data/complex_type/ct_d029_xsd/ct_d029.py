from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class MyType:
    class Meta:
        name = "myType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class FooType(MyType):
    class Meta:
        name = "fooType"

    any_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
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
class Root(FooType):
    class Meta:
        name = "root"
