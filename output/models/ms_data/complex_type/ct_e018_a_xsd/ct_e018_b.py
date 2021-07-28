from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    attr_test1: Optional[int] = field(
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
