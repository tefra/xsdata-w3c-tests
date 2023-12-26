from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class Mytype1:
    class Meta:
        name = "mytype1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    attr_test1: Optional[int] = field(
        default=None,
        metadata={
            "name": "attrTest1",
            "type": "Attribute",
            "namespace": "a",
        },
    )
    attr_test2: Optional[str] = field(
        default=None,
        metadata={
            "name": "attrTest2",
            "type": "Attribute",
            "namespace": "a",
        },
    )


@dataclass
class FooType(Mytype1):
    class Meta:
        name = "fooType"
