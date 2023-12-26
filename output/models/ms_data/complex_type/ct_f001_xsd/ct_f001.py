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
            "required": True,
        },
    )


@dataclass
class FooType(MyType):
    class Meta:
        name = "fooType"


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
