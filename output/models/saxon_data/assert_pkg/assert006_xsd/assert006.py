from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Base:
    """
    :ivar value:
    """
    class Meta:
        name = "base"

    value: Optional[int] = field(
        default=None,
    )


@dataclass
class Derived(Base):
    class Meta:
        name = "derived"



@dataclass
class Outer:
    """
    :ivar inner:
    """
    class Meta:
        name = "outer"

    inner: List[Derived] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=4
        )
    )
