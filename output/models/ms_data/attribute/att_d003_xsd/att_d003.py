from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AttRef:
    """
    :ivar att1:
    """
    class Meta:
        name = "attRef"

    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            min_length=2.0,
            max_length=3.0
        )
    )


@dataclass
class Doc:
    """
    :ivar elem:
    """
    class Meta:
        name = "doc"

    elem: Optional[AttRef] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
