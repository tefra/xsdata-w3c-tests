from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class AttRef:
    """
    :ivar aga1:
    :ivar aga2:
    """
    class Meta:
        name = "attRef"

    aga1: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    aga2: Optional[str] = field(
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
        namespace = "http://xsdtesting"

    elem: Optional[AttRef] = field(
        default=None,
        metadata=dict(
            type="Element"
        )
    )
