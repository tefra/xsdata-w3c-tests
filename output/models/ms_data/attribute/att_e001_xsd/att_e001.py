from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AttRef:
    """
    :ivar foo:
    :ivar att2:
    """
    class Meta:
        name = "attRef"

    foo: Optional[str] = field(
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
