from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MyBase:
    class Meta:
        name = "myBase"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    a: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class A(MyBase):
    pass
