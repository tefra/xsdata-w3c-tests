from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class MyType:
    class Meta:
        name = "myType"

    my_element1: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement1",
            "type": "Element",
            "namespace": "",
        },
    )
    my_element2: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement2",
            "type": "Element",
            "namespace": "",
        },
    )
    my_element3: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement3",
            "type": "Element",
            "namespace": "",
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

    my_element2: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    my_element3: Any = field(
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
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
