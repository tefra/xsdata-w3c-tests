from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class MyType:
    class Meta:
        name = "myType"

    my_element1_or_my_element2_or_my_element3: Optional[str] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "myElement1",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "myElement2",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "myElement3",
                    "type": str,
                    "namespace": "",
                },
            ),
        }
    )
    local_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        }
    )


@dataclass
class FooType(MyType):
    class Meta:
        name = "fooType"

    my_element4: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement4",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    attr1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    attr2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    attr3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    attr4: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
