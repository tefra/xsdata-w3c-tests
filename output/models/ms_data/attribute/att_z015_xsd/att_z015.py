from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Base:
    """
    :ivar a:
    """
    class Meta:
        name = "base"

    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Derived(Base):
    class Meta:
        name = "derived"


@dataclass
class Doc(Derived):
    class Meta:
        name = "doc"
