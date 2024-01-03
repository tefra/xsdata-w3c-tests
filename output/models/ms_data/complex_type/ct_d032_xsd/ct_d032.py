from dataclasses import dataclass, field
from typing import Dict, Optional, Any


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
    any_attributes: Dict[str, str] = field(
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
    my_attr1: Optional[object] = field(
        default=None,
        metadata={
            "name": "myAttr1",
            "type": "Attribute",
        },
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
