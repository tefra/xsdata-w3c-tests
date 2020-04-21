from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Elt1:
    """
    :ivar elt2:
    :ivar elt3:
    :ivar elt4:
    """
    class Meta:
        name = "elt1"

    elt2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    elt3: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
    elt4: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )


@dataclass
class Root:
    """
    :ivar elt1:
    """
    class Meta:
        name = "root"

    elt1: List[Elt1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
