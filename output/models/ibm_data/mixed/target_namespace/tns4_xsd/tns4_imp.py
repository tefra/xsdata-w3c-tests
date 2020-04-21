from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://test2"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "http://test2"

    value: Optional[int] = field(
        default=None,
    )


@dataclass
class Y:
    """
    :ivar a:
    """
    class Meta:
        name = "y"
        namespace = "http://test2"

    a: List[A] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
