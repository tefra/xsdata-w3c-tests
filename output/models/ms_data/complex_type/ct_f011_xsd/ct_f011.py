from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MyType:
    class Meta:
        name = "myType"

    my_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement",
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
    my_attr: Optional[str] = field(
        default=None,
        metadata={
            "name": "myAttr",
            "type": "Attribute",
        }
    )


@dataclass
class FooType(MyType):
    class Meta:
        name = "fooType"

    my_element3: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement3",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    my_element4: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement4",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
