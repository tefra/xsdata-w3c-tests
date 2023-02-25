from dataclasses import dataclass, field
from typing import Optional


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


@dataclass
class Doc(Derived):
    class Meta:
        name = "doc"
