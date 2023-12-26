from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Foo:
    class Meta:
        name = "foo"

    my_ele1: Optional[str] = field(
        default=None,
        metadata={
            "name": "myEle1",
            "type": "Element",
            "namespace": "",
        },
    )
    my_ele2: Optional[int] = field(
        default=None,
        metadata={
            "name": "myEle2",
            "type": "Element",
            "namespace": "",
        },
    )
    my_ele3: Optional[int] = field(
        default=None,
        metadata={
            "name": "myEle3",
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class FooType(Foo):
    class Meta:
        name = "fooType"

    my_ele1: Optional[str] = field(
        default=None,
        metadata={
            "name": "myEle1",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    my_ele2: Optional[int] = field(
        default=None,
        metadata={
            "name": "myEle2",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
