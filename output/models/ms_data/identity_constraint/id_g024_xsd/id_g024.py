from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Tabletype:
    """
    :ivar r:
    :ivar c:
    """
    class Meta:
        name = "tabletype"

    r: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    c: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )


@dataclass
class T(Tabletype):
    class Meta:
        name = "t"



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
