from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    attr_test: Optional[object] = field(
        default=None,
        metadata={
            "name": "attrTest",
            "type": "Attribute",
        }
    )
    attr_test1: Optional[object] = field(
        default=None,
        metadata={
            "name": "attrTest1",
            "type": "Attribute",
        }
    )
    attr_test2: Optional[object] = field(
        default=None,
        metadata={
            "name": "attrTest2",
            "type": "Attribute",
        }
    )
    attr_test3: Optional[object] = field(
        default=None,
        metadata={
            "name": "attrTest3",
            "type": "Attribute",
        }
    )
    attr_test4: Optional[object] = field(
        default=None,
        metadata={
            "name": "attrTest4",
            "type": "Attribute",
        }
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
