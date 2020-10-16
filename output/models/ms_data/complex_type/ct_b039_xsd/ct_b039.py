from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar my_element:
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
            "required": True,
        }
    )
    attr_test: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
