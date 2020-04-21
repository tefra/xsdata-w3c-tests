from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Elt1:
    class Meta:
        name = "elt1"



@dataclass
class TypeA:
    """
    :ivar elt2:
    """
    class Meta:
        name = "typeA"

    elt2: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
