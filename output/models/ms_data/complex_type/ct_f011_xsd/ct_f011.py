from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MyType:
    class Meta:
        name = "myType"

    my_element_or_my_element2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "myElement",
                    "type": str,
                    "namespace": "",
                },
                {
                    "name": "myElement2",
                    "type": str,
                    "namespace": "",
                },
            ),
        }
    )
    my_attr: Optional[object] = field(
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
