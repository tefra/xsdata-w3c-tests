from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Rtype:
    """
    :ivar value:
    :ivar val:
    """
    class Meta:
        name = "rtype"

    value: Optional[str] = field(
        default=None,
    )
    val: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class R(Rtype):
    class Meta:
        name = "r"


@dataclass
class R2(Rtype):
    class Meta:
        name = "r2"


@dataclass
class T:
    """
    :ivar r2:
    :ivar r:
    """
    class Meta:
        name = "t"

    r2: Optional[R2] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    r: Optional[R] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar t:
    """
    class Meta:
        name = "root"

    t: List[T] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
