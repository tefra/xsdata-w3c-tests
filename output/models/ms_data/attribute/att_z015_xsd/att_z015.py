from dataclasses import dataclass, field
from typing import Optional, Any


@dataclass
class Base:
    class Meta:
        name = "base"

    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Derived(Base):
    class Meta:
        name = "derived"

    a: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        }
    )


@dataclass
class Doc(Derived):
    class Meta:
        name = "doc"
