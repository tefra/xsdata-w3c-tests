from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Test:
    class Meta:
        name = "test"

    att: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    foo1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    foo2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Doc(Test):
    class Meta:
        name = "doc"
