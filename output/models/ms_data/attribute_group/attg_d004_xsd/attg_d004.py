from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AttgRef:
    """
    :ivar att1:
    """
    class Meta:
        name = "attgRef"

    att1: Optional[int] = field(
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

    elem: Optional[AttgRef] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace=""
        )
    )
