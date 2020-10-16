from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar my_element:
    :ivar my_ele2:
    :ivar attr_test:
    """
    class Meta:
        name = "fooType"

    my_element: Optional[str] = field(
        default=None,
        metadata={
            "name": "myElement",
            "type": "Element",
            "namespace": "",
        }
    )
    my_ele2: Optional[str] = field(
        default=None,
        metadata={
            "name": "myEle2",
            "type": "Element",
            "namespace": "",
        }
    )
    attr_test: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
