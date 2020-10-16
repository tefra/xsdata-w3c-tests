from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar value:
    :ivar attr_test1:
    :ivar attr_test2:
    """
    class Meta:
        name = "fooType"

    value: Optional[str] = field(
        default=None,
    )
    attr_test1: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrTest1",
            "type": "Attribute",
        }
    )
    attr_test2: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrTest2",
            "type": "Attribute",
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
