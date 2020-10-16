from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar attr_test1:
    :ivar attr_test2:
    :ivar attr_test:
    """
    class Meta:
        name = "fooType"

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
