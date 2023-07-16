from dataclasses import dataclass, field
from typing import Dict, Optional


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
        }
    )
    my_element2: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement2",
            "type": "Element",
            "namespace": "",
        }
    )
    my_element3: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement3",
            "type": "Element",
            "namespace": "",
        }
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        }
    )


@dataclass
class FooType(MyType):
    class Meta:
        name = "fooType"

    my_element1: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement1",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    local_attr: Optional[object] = field(
        default=None,
        metadata={
            "name": "localAttr",
            "type": "Attribute",
        }
    )
    my_attr: Optional[object] = field(
        default=None,
        metadata={
            "name": "myAttr",
            "type": "Attribute",
        }
    )
    local_attr1: Optional[object] = field(
        default=None,
        metadata={
            "name": "localAttr1",
            "type": "Attribute",
        }
    )
    my_attr1: Optional[object] = field(
        default=None,
        metadata={
            "name": "myAttr1",
            "type": "Attribute",
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
