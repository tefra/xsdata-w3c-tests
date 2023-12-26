from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    my_ele3: Optional[str] = field(
        default=None,
        metadata={
            "name": "myEle3",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    my_ele4: Optional[int] = field(
        default=None,
        metadata={
            "name": "myEle4",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    foo_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "fooType",
            "type": "Attribute",
        },
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
