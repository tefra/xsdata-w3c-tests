from dataclasses import dataclass, field
from typing import Any, Dict, Optional


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

    any_element: Any = field(
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
    my_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    local_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
