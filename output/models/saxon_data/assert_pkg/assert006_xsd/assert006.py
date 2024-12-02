from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Base:
    class Meta:
        name = "base"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Derived(Base):
    class Meta:
        name = "derived"


@dataclass
class Outer:
    class Meta:
        name = "outer"

    inner: list[Derived] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 4,
        },
    )
