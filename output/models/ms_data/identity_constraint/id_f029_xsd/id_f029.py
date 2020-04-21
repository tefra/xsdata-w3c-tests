from dataclasses import dataclass, field
from typing import List, Optional
from output.models.ms_data.identity_constraint.id_f029_xsd.id_f029a import (
    R,
)


@dataclass
class T:
    """
    :ivar r:
    :ivar val:
    """
    class Meta:
        name = "t"

    r: Optional[R] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="importNS",
            required=True
        )
    )
    val: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
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
