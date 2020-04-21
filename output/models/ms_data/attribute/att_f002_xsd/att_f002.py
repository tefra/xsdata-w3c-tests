from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AttRef:
    """
    :ivar att1:
    :ivar att2:
    """
    class Meta:
        name = "attRef"

    att1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    att2: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
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
