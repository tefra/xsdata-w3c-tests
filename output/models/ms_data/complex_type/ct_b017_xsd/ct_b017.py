from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MyType:
    """
    :ivar my_ele1:
    :ivar my_ele2:
    """
    class Meta:
        name = "myType"

    my_ele1: Optional[str] = field(
        default=None,
        metadata={
            "name": "myEle1",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    my_ele2: Optional[str] = field(
        default=None,
        metadata={
            "name": "myEle2",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class FooType(MyType):
    """
    :ivar my_element:
    """
    class Meta:
        name = "fooType"

    my_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
