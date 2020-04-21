from dataclasses import dataclass, field
from typing import Optional


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
